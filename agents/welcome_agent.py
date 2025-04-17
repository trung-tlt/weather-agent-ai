from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import tools.greeting as greeting

greeting_agent = None
MODEL_NAME = "openai/gpt-4o"
try:
    greeting_agent = Agent(
        model=LiteLlm(model=MODEL_NAME),
        name="greeting_agent",
        instruction="You are the Greeting Agent. Your ONLY task is to provide a friendly greeting to the user. "
                    "Use the 'say_hello' tool to generate the greeting. "
                    "If the user provides their name, make sure to pass it to the tool. "
                    "Do not engage in any other conversation or tasks.",
        description="Handles simple greetings and hellos using the 'say_hello' tool.", # Crucial for delegation
        tools=[greeting.say_hello]
    )
    print(f"Creating agent {greeting_agent.name} using model {MODEL_NAME}")
except Exception as e:
    print(f"Error creating greeting agent: {e}")