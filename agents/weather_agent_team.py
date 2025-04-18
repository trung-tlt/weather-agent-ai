from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from tools.get_weather import get_weather_with_context
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
                description="Main agent: Provides weather (state-aware unit), delegates greetings/farewells, saves report to state.",
                instruction="You are the main Weather Agent. Your job is to provide weather using 'get_weather_stateful'. "
                    "The tool will format the temperature based on user preference stored in state. "
                    "Delegate simple greetings to 'greeting_agent' and farewells to 'farewell_agent'. "
                    "Handle only weather requests, greetings, and farewells.",
                tools=[get_weather_with_context],
                sub_agents=[greeting_agent, farewell_agent],
                output_key="last_weather_report")
            
            print(f"Coordinator agent '{APP_NAME}' created using model '{MODEL_NAME}'.")
            print("Weather Agent Coordinator is ready to use!")
        except Exception as e:
            print(f"Error creating agent: {e}")
            raise
        
        