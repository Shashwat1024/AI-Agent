# AI-Agent
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![AI](https://img.shields.io/badge/AI-Generative%20Agent-orange.svg)

A modular AI agent framework with tool integration, built from scratch using Google's Gemini API. This system allows for dynamic tool registration and execution with natural language processing capabilities.

---

## ✨ Key Features

| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| 🔧 Tool System         | Dynamic registration and execution of custom tools with parameter detection |
| 🧮 Math Operations     | Built-in calculator for arithmetic calculations                            |
| 🌦️ Weather Lookup      | Simulated weather information retrieval                                    |
| 📂 File Operations     | Read local files through natural language commands                         |
| 🧩 Extensible Design   | Easy to add new tools and functionality                                   |
| 🔐 API Integration     | Secure Gemini API integration with environment variables                  |

---

## 🏗️ Architecture Overview

```python
AI_Agent/
│
├── main.py                # Core agent logic and tool management
├── .env                   # Configuration (API keys)
├── tools/                 # Tool implementations
│   ├── math_tools.py      # Calculator functions
│   ├── web_tools.py       # Weather/API integrations
│   └── file_tools.py      # File operations
└── README.md              # Project documentation
