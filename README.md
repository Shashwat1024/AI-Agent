# 🤖 AI Agent

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![AI](https://img.shields.io/badge/AI-Generative%20Agent-orange.svg)

A modular AI agent with tool integration, built from scratch using Google's Gemini API. This system allows for dynamic tool registration and execution with natural language processing capabilities.

## ✨ Key Features

| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| 🔧 Tool System         | Dynamic registration and execution of custom tools with parameter detection |
| 🧮 Math Operations     | Built-in calculator for arithmetic calculations                            |
| 🌦️ Weather Lookup      | Simulated weather information retrieval                                    |
| 📂 File Operations     | Read local files through natural language commands                         |
| 🧩 Extensible Design   | Easy to add new tools and functionality                                   |
| 🔐 API Integration     | Secure Gemini API integration with environment variables                  |

## 🏗️ Architecture Overview
AI_Agent/
│
├── main.py # Core agent logic and tool management
├── .env # Configuration (API keys)
├── tools/ # Tool implementations
│ ├── math_tools # Calculator functions
│ ├── web_tools  # Weather/API integrations
│ └── file_tools # File operations
└── README.md # Project documentation


## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Google Gemini API key

### Installation
1. Clone the repository:
```bash
git clone https://github.com/Shashwat2801/ai-agent-framework.git
cd ai-agent-framework

```
2. Install Dependencies:
```bash
pip install python-dotenv google-generativeai

```
3. Create .env file:
```bash
GEMINI_API_KEY=your_api_key_here

```
Usage
Run the Agent:
```bash
uv/python main.py

```
### Example Commands:
- "Calculate 15 plus 27"

- "What's the weather in Paris?"

- "Read the file example.txt"


### 🌐 API Integration
This project uses Google's Gemini API for generative AI capabilities. To get an API key:

- Visit Google AI Studio

- Create an API key

- Add it to your .env file
