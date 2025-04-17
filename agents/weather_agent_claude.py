from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from tools.get_weather import get_weather
from google.adk.models.lite_llm import LiteLlm

MODEL_NAME = "anthropic/claude-3-5-sonnet-20240620"
APP_NAME = "weather_agent_claude"
USER_ID = "user_claude_1"
SESSION_ID = "session_claude_1"

class WeatherAgentClaude:
    def __init__(self):
        self.runner = None
        self.session = None
        self.user_id = None
        self.session_id = None
        self.session_service = None
    def create_agent(self):
        try:
            weather_agent = Agent(
                model=LiteLlm(model=MODEL_NAME),
                name="weather_agent_claude",
                description="A helpful assistant that can provide weather information for a given city.",
                instruction="You are a helpful weather assistant powered by Claude. "
                        "Use the 'get_weather' tool for city weather requests. "
                        "Clearly present successful reports or polite error messages based on the tool's output status.",
                tools=[get_weather])
            print(f"Agent '{weather_agent.name}' created using model '{MODEL_NAME}'.")
            self.session_service = InMemorySessionService()
            self.user_id = USER_ID
            self.session_id = SESSION_ID
            self.session = self.session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
            print(f"Session '{SESSION_ID}' created for '{APP_NAME}' with user '{USER_ID}'.")
            runner = Runner(
                agent=weather_agent,
                session_service=self.session_service,
                app_name=APP_NAME
            )
            self.runner = runner
            print(f"Runner created for agent '{APP_NAME}'.")
            print("Weather Agent Claude is ready to use!")
        except Exception as e:
            print(f"Error creating agent: {e}")
            raise
        
        