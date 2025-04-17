from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from tools.get_weather import get_weather
from google.adk.models.lite_llm import LiteLlm

MODEL_NAME = "openai/gpt-4o"
APP_NAME = "weather_agent_gpt4o"
USER_ID = "user_gpt4o_1"
SESSION_ID = "session_gpt4o_1"

class WeatherAgentGPT4o:
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
                name="weather_agent_gpt4o",
                description="A helpful assistant that can provide weather information for a given city.",
                instruction="You are a helpful weather assistant powered by DeepSeek. "
                        "Use the 'get_weather' tool for city weather requests. "
                        "Clearly present successful reports or polite error messages based on the tool's output status.",
                tools=[get_weather]),
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
            print("Weather Agent DeepSeek is ready to use!")
        except Exception as e:
            print(f"Error creating agent: {e}")
            raise
        
        