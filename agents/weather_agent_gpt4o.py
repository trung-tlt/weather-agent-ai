from google.adk.agents import Agent
from tools.get_weather import get_weather
from google.adk.models.lite_llm import LiteLlm

MODEL_NAME = "openai/gpt-4o"
APP_NAME = "weather_agent_gpt4o"

class WeatherAgentGPT4o:
    def __init__(self):
        self.agent = None
        self.create_agent()
        
    def create_agent(self):
        try:
            self.agent = Agent(
                model=LiteLlm(model=MODEL_NAME),
                name=APP_NAME,
                description="A helpful assistant that can provide weather information for a given city.",
                instruction="You are a helpful weather assistant powered by GPT-4o. "
                        "Use the 'get_weather' tool for city weather requests. "
                        "Clearly present successful reports or polite error messages based on the tool's output status.",
                tools=[get_weather])
            print(f"Agent '{APP_NAME}' created using model '{MODEL_NAME}'.")
        except Exception as e:
            print(f"Error creating agent: {e}")
            raise