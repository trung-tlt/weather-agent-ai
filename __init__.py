import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm # For multi-model support
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types # For creating message Content/Parts

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore")

import logging
logging.basicConfig(level=logging.ERROR)

print("Libraries imported.")

# --- IMPORTANT: Replace placeholders with your real API keys ---

# Gemini API Key (Get from Google AI Studio: https://aistudio.google.com/app/apikey)
#os.environ["GOOGLE_API_KEY"] = "GOOGLE_API_KEY" # <--- REPLACE

# OpenAI API Key (Get from OpenAI Platform: https://platform.openai.com/api-keys)
#os.environ['OPENAI_API_KEY'] = 'OPENAI_API_KEY' # <--- REPLACE

# Anthropic API Key (Get from Anthropic Console: https://console.anthropic.com/settings/keys)
#os.environ['ANTHROPIC_API_KEY'] = 'ANTHROPIC_API_KEY' # <--- REPLACE


# --- Verify Keys (Optional Check) ---
print("API Keys Set:")
print(f"Google API Key set: {'Yes' if os.environ.get('GOOGLE_API_KEY') and os.environ['GOOGLE_API_KEY'] != 'YOUR_GOOGLE_API_KEY' else 'No (REPLACE PLACEHOLDER!)'}")
print(f"OpenAI API Key set: {'Yes' if os.environ.get('OPENAI_API_KEY') and os.environ['OPENAI_API_KEY'] != 'YOUR_OPENAI_API_KEY' else 'No (REPLACE PLACEHOLDER!)'}")
print(f"Anthropic API Key set: {'Yes' if os.environ.get('ANTHROPIC_API_KEY') and os.environ['ANTHROPIC_API_KEY'] != 'YOUR_ANTHROPIC_API_KEY' else 'No (REPLACE PLACEHOLDER!)'}")
print(f"Anthropic API Key set: {'Yes' if os.environ.get('DEEPSEEK_API_KEY') and os.environ['DEEPSEEK_API_KEY='] != 'YOUR_DEEPSEEK_API_KEY=' else 'No (REPLACE PLACEHOLDER!)'}")

# Configure ADK to use API keys directly (not Vertex AI for this multi-model setup)
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"


# @markdown **Security Note:** It's best practice to manage API keys securely (e.g., using Colab Secrets or environment variables) rather than hardcoding them directly in the notebook. Replace the placeholder strings above.
MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash-exp"

# Note: Specific model names might change. Refer to LiteLLM/Provider documentation.
MODEL_GPT_4O = "openai/gpt-4o"
MODEL_CLAUDE_SONNET = "anthropic/claude-3-sonnet-20240229"


print("\nEnvironment configured.")
