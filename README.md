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
🚀 Getting Started
Prerequisites
Python 3.10+

Google Gemini API key

Installation
Clone the repository:

bash
git clone https://github.com/Shashwat2801/ai-agent-framework.git
cd ai-agent-framework
Install dependencies:

bash
pip install python-dotenv google-generativeai
Create .env file:

env
GEMINI_API_KEY=your_api_key_here
Usage
Run the agent:

bash
python main.py
Example commands:

"Calculate 15 plus 27"

"What's the weather in Paris?"

"Read the file example.txt"

🛠️ Tool Development
Adding New Tools
Create your tool function:

python
def new_tool(param1: type, param2: type) -> str:
    """Description of what the tool does."""
    # Implementation
    return "Result"
Register the tool:

python
manager.register_tool(Tool(
    name="new_tool",
    description="What this tool does",
    function=new_tool
))
Add detection logic in try_use_tools().

🌐 API Integration
This project uses Google's Gemini API for generative AI capabilities. To get an API key:

Visit Google AI Studio

Create an API key

Add it to your .env file

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some amazing feature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📧 Contact
Shashwat Mahajan
Email
GitHub
LinkedIn
