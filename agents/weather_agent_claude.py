from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from tools.get_weather import get_weather

MODEL_NAME = "anthropic/claude-3-5-sonnet-20240620"
APP_NAME = "weather_agent_claude"
class WeatherAgentClaude:
    def __init__(self):
        self.agent = None
        self.create_agent()
    
    def create_agent(self):
        try:
            self.agent = Agent(
                model=LiteLlm(model=MODEL_NAME),
                name=APP_NAME,
                description="A helpful assistant that can provide weather information for a given city.",
                instruction="You are a helpful weather assistant powered by Claude. "
                        "Use the 'get_weather' tool for city weather requests. "
                        "Clearly present successful reports or polite error messages based on the tool's output status.",
                tools=[get_weather])
            print(f"Agent '{APP_NAME}' created using model '{MODEL_NAME}'.")
        except Exception as e:
            print(f"Error creating agent: {e}")
            raise
        
        