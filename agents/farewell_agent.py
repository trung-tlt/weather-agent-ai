from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import tools.greeting as greeting

farewell_agent = None
MODEL_NAME = "openai/gpt-4o"
try:
    farewell_agent = Agent(
        model=LiteLlm(model="openai/gpt-4o"),
        name="farewell_agent",
        instruction="You are the Farewell Agent. Your ONLY task is to provide a friendly farewell to the user. ",
        description="Handles simple farewells using the 'say_goodbye' tool.",
        tools=[greeting.say_goodbye])
    print(f"Creating agent {farewell_agent.name} using model {MODEL_NAME}")
except Exception as e:
    print(f"Error creating farewell agent: {e}")
