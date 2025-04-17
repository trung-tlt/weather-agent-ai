# AI Assistant Project

This is a Python-based AI assistant project that utilizes the [Google ADK](https://developers.google.com/adk) and [LiteLLM](https://github.com/BerriAI/litellm) libraries to interact with large language models such as OpenAI and Anthropic.

---

## 🚀 Getting Started

Follow the steps below to set up your development environment and run the project.

### 1. Clone the repository

```bash
git clone git@github.com:trung-tlt/weather-agent-ai.git
cd weather-agent-ai
```
### 2. Set up a virtual environment
```
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Set your API keys

Before running the project, make sure you export the required environment variables:
```
export OPENAI_API_KEY="your-openai-api-key"
export ANTHROPIC_API_KEY="your-anthropic-api-key"
```
|💡 You can also add these to a .env file and load them using python-dotenv if preferred.

### 5. Run the project
```
python main.py
```
<img width="1470" alt="Screenshot 2025-04-17 at 3 19 34 PM" src="https://github.com/user-attachments/assets/479f024c-1064-4f2e-b5b0-1dd4252d6d31" />

---

### Dependencies
- `google-adk`: Google’s Agent Development Kit
- `litellm`: Unified interface to call LLMs including OpenAI, Anthropic, etc.
