from google.adk.runners import Runner
import asyncio
from google.genai import types # For creating message Content/Parts
from agents.weather_agent_gpt4o import WeatherAgentGPT4o
from agents.weather_agent_claude import WeatherAgentClaude
from agents.weather_agent_team import WeatherAgentTeam

async def call_agent_async(query: str,runner: Runner,session_id:str,user_id:str):
  """Sends a query to the agent and prints the final response."""
  print(f"\n>>> User Query: {query}")

  # Prepare the user's message in ADK format
  content = types.Content(role='user', parts=[types.Part(text=query)])

  final_response_text = "Agent did not produce a final response." # Default

  # Key Concept: run_async executes the agent logic and yields Events.
  # We iterate through events to find the final answer.
  async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
      # You can uncomment the line below to see *all* events during execution
      # print(f"  [Event] Author: {event.author}, Type: {type(event).__name__}, Final: {event.is_final_response()}, Content: {event.content}")

      # Key Concept: is_final_response() marks the concluding message for the turn.
      if event.is_final_response():
          if event.content and event.content.parts:
             # Assuming text response in the first part
             final_response_text = event.content.parts[0].text
          elif event.actions and event.actions.escalate: # Handle potential errors/escalations
             final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
          # Add more checks here if needed (e.g., specific error codes)
          break # Stop processing events once the final response is found

  print(f"<<< Agent Response: {final_response_text}")
    
async def main():
   
   # agent1 = WeatherAgentGPT4o()
   # agent1.create_agent()
   # await call_agent_async("What is the weather like in Hanoi?",agent1.runner,agent1.session_id,agent1.user_id)

   # agent2 = WeatherAgentClaude()
   # agent2.create_agent()
   # await call_agent_async("What is the weather like in Dong Nai?",agent2.runner,agent2.session_id,agent2.user_id)

   agent_team = WeatherAgentTeam()
   agent_team.init()
   await call_agent_async("Hello?",agent_team.runner,agent_team.session_id,agent_team.user_id)
   await call_agent_async("What is the weather like in Hanoi?",agent_team.runner,agent_team.session_id,agent_team.user_id)
   await call_agent_async("Thank you!",agent_team.runner,agent_team.session_id,agent_team.user_id)
 
if __name__ == "__main__":
    asyncio.run(main())

