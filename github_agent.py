import asyncio
import os
import platform
import streamlit as st
from textwrap import dedent

from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.tools.mcp import MCPTools
from mcp import StdioServerParameters

# ----------------------------
# Streamlit page config
# ----------------------------
st.set_page_config(
    page_title="🐙 GitHub MCP Agent",
    page_icon="🐙",
    layout="wide"
)

st.markdown("<h1>🐙 GitHub MCP Agent</h1>", unsafe_allow_html=True)
st.markdown(
    "Explore GitHub repositories using natural language powered by **MCP (Model Context Protocol)**."
)

# ----------------------------
# Sidebar – API Keys
# ----------------------------
with st.sidebar:
    st.header("🔑 Authentication")

    openai_key = st.text_input(
        "OpenAI API Key",
        type="password",
        help="Required for the AI agent"
    )
    if openai_key:
        os.environ["OPENAI_API_KEY"] = openai_key

    github_token = st.text_input(
        "GitHub Token",
        type="password",
        help="Create a fine-grained token at github.com/settings/tokens"
    )
    if github_token:
        os.environ["GITHUB_TOKEN"] = github_token

    st.markdown("---")
    st.markdown("### Example Queries")
    st.markdown("- Summarize this repository")
    st.markdown("- Show open issues")
    st.markdown("- What PRs need review?")
    st.markdown("- Explain the architecture")

# ----------------------------
# Main Inputs
# ----------------------------
col1, col2 = st.columns([3, 1])

with col1:
    repo = st.text_input(
        "Repository",
        value="munzahmed07/Edge-Adaptive-Trajectory",
        help="Format: owner/repo"
    )

with col2:
    query_type = st.selectbox(
        "Query Type",
        ["Issues", "Pull Requests", "Repository Activity", "Custom"]
    )

if query_type == "Issues":
    query_template = f"Show open issues in {repo}"
elif query_type == "Pull Requests":
    query_template = f"Show recent merged pull requests in {repo}"
elif query_type == "Repository Activity":
    query_template = f"Analyze repository activity and health for {repo}"
else:
    query_template = ""

query = st.text_area(
    "Your Query",
    value=query_template,
    placeholder="What would you like to know about this repository?"
)

# ----------------------------
# MCP + Agent Logic
# ----------------------------


async def run_github_agent(message: str) -> str:
    if not os.getenv("OPENAI_API_KEY"):
        return "❌ OpenAI API key not provided."

    if not os.getenv("GITHUB_TOKEN"):
        return "❌ GitHub token not provided."

    # ✅ WINDOWS-SAFE MCP COMMAND
    if platform.system() == "Windows":
        mcp_command = "npx.cmd"
    else:
        mcp_command = "npx"

    try:
        server_params = StdioServerParameters(
            command=mcp_command,
            args=["@modelcontextprotocol/server-github"],
            env={
                **os.environ,
                "GITHUB_PERSONAL_ACCESS_TOKEN": os.getenv("GITHUB_TOKEN"),
                "GITHUB_TOOLSETS": "repos,issues,pull_requests"
            }
        )

        async with MCPTools(server_params=server_params) as mcp_tools:
            agent = Agent(
                tools=[mcp_tools],
                instructions=dedent("""
                    You are a GitHub assistant.
                    - Help users explore repositories, issues, pull requests, and activity
                    - Be factual and concise
                    - Use markdown formatting
                    - Include links when useful
                """),
                markdown=True
            )

            response: RunOutput = await asyncio.wait_for(
                agent.arun(message),
                timeout=120.0
            )

            return response.content

    except asyncio.TimeoutError:
        return "❌ Request timed out."
    except Exception as e:
        return f"❌ Error: {str(e)}"

# ----------------------------
# Run Button
# ----------------------------
if st.button("🚀 Run Query", type="primary", use_container_width=True):
    if not openai_key:
        st.error("Please enter your OpenAI API key.")
    elif not github_token:
        st.error("Please enter your GitHub token.")
    elif not query:
        st.error("Please enter a query.")
    else:
        with st.spinner("Analyzing GitHub repository..."):
            full_query = query if repo in query else f"{query} in {repo}"
            result = asyncio.run(run_github_agent(full_query))

        st.markdown("### 📊 Results")
        st.markdown(result)

# ----------------------------
# Help Section
# ----------------------------
st.markdown(
    """
    ---
    ### ℹ️ How this works
    - Uses **GitHub MCP server** via `npx` 
    - MCP provides structured GitHub context
    - AI agent reasons over that context using OpenAI
    - Results are rendered in markdown
    """
)
