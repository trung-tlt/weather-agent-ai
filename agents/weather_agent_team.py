from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from tools.get_weather import get_weather
from google.adk.models.lite_llm import LiteLlm
from agents.welcome_agent import greeting_agent
from agents.farewell_agent import farewell_agent

MODEL_NAME = "openai/gpt-4o"
APP_NAME = "weather_agent_team"
USER_ID = "weather_agent_team_user_1"
SESSION_ID = "weather_agent_team_session_1"

class WeatherAgentTeam:
    def __init__(self):
        self.runner = None
        self.session = None
        self.user_id = None
        self.session_id = None
        self.session_service = None
    def init(self):
        try:
            weather_agent_team = Agent(
                model=LiteLlm(model=MODEL_NAME),
                name="weather_agent",
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
            print(f"Coortinator agent '{weather_agent_team.name}' created using model '{MODEL_NAME}'.")
            self.session_service = InMemorySessionService()
            self.user_id = USER_ID
            self.session_id = SESSION_ID
            self.session = self.session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
            print(f"Session '{SESSION_ID}' created for '{APP_NAME}' with user '{USER_ID}'.")
            runner = Runner(
                agent=weather_agent_team,
                session_service=self.session_service,
                app_name=APP_NAME
            )
            self.runner = runner
            print(f"Runner created for agent '{APP_NAME}'.")
            print("Weather Agent Coordinator is ready to use!")
        except Exception as e:
            print(f"Error creating agent: {e}")
            raise
        
        