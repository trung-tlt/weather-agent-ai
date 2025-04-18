from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from tools.get_weather import get_weather
from agents.welcome_agent import greeting_agent
from agents.farewell_agent import farewell_agent

MODEL_NAME = "openai/gpt-4o"
APP_NAME = "weather_agent_team"

class WeatherAgentTeam:
    def __init__(self):
        self.agent = None
        self.create_agent()
        
    def create_agent(self):
        try:
            self.agent = Agent(
                model=LiteLlm(model=MODEL_NAME),
                name=APP_NAME,
                description="The main coordinator agent. Handles weather requests and delegates greetings/farewells to specialists.",
                instruction="You are the main Weather Agent coordinating a team. Your primary responsibility is to provide weather information. "
                    "Use the 'get_weather' tool ONLY for specific weather requests (e.g., 'weather in Hanoi'). "
                    "You have specialized sub-agents: "
                    "1. 'greeting_agent': Handles simple greetings like 'Hi', 'Hello'. Delegate to it for these. "
                    "2. 'farewell_agent': Handles simple farewells like 'Thank you', 'Bye', 'See you'. Delegate to it for these. "
                    "Analyze the user's query. If it's a greeting, delegate to 'greeting_agent'. If it's a farewell, delegate to 'farewell_agent'. "
                    "If it's a weather request, handle it yourself using 'get_weather'. "
                    "For anything else, respond appropriately or state you cannot handle it.",
                tools=[get_weather],
                sub_agents=[greeting_agent, farewell_agent])
            
            print(f"Coortinator agent '{APP_NAME}' created using model '{MODEL_NAME}'.")
            print("Weather Agent Coordinator is ready to use!")
        except Exception as e:
            print(f"Error creating agent: {e}")
            raise
        
        