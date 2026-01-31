# 🐙 GitHub MCP Agent

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![OpenAI](https://img.shields.io/badge/OpenAI-API-black)
![MCP](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-purple)
![GitHub](https://img.shields.io/badge/GitHub-API-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

> 🚀 **Portfolio Project**
> An AI agent that uses **Model Context Protocol (MCP)** to explore GitHub repositories using natural language.

---

## 📌 Overview

The **GitHub MCP Agent** is an Agentic AI application that allows users to query GitHub repositories in plain English. Instead of scraping data or using static RAG pipelines, this project uses **Model Context Protocol (MCP)** to interact with GitHub as a structured, tool-based context source.

The agent dynamically reasons over repositories, issues, pull requests, and activity using live GitHub data.

---

## 🧠 Why MCP?

Traditional approaches:

* ❌ Web scraping (fragile)
* ❌ Static RAG (outdated context)

This project uses **MCP**, which enables:

* ✅ Live tool-based access to GitHub
* ✅ Structured context (repos, issues, PRs)
* ✅ Clear separation between reasoning and data access
* ✅ Safer, auditable agent behavior

---

## ✨ Features

* 🔍 Query GitHub repositories using natural language
* 🐞 Explore issues and discussions
* 🔀 Analyze pull requests
* 📊 Inspect repository activity and health
* 🤖 Agent powered by OpenAI + MCP tools
* 🪟 Windows-compatible (no Docker required)

---

## 🧰 Tech Stack

* **Python 3.10+**
* **Streamlit** – UI
* **OpenAI API** – LLM reasoning
* **Agno Framework** – Agent orchestration
* **Model Context Protocol (MCP)** – Tool-based context
* **GitHub MCP Server** – GitHub integration via `npx`

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/munzahmed07/github-mcp-agent.git
cd github-mcp-agent
```

---

### 2️⃣ Create & activate environment (Conda recommended)

```bash
conda create -n ai_agent_env python=3.10 -y
conda activate ai_agent_env
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Install Node.js (required for MCP)

Download and install **Node.js LTS** from:
👉 [https://nodejs.org](https://nodejs.org)

Verify:

```bash
node --version
npx --version
```

---

### 5️⃣ Install GitHub MCP server

```bash
npm install -g @modelcontextprotocol/server-github
```

---

## 🔑 API Keys

This app requires:

* **OpenAI API Key**
* **GitHub Fine-grained Token** (read-only access)

You can paste both directly into the Streamlit sidebar when the app runs.

---

## ▶️ Run the App

```bash
streamlit run github_agent.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧪 Example Queries

* "Summarize this repository"
* "Show open issues"
* "What pull requests need review?"
* "Explain the architecture"
* "Analyze recent repository activity"

---

## 📁 Project Structure

```
github-mcp-agent/
├── github_agent.py
├── requirements.txt
└── README.md
```

---

## 📜 License

MIT License

---


