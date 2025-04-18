from google.adk.runners import Runner
import asyncio
from google.genai import types # For creating message Content/Parts
from agents.weather_agent_gpt4o import WeatherAgentGPT4o
from agents.weather_agent_claude import WeatherAgentClaude
from agents.weather_agent_team import WeatherAgentTeam
from google.adk.sessions import InMemorySessionService

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
   # Initialize session service for memory storage
   session_service = InMemorySessionService()
   
   # Initialize agents
   weatherAgentGPT4o = WeatherAgentGPT4o()
   session1 = session_service.create_session(app_name="weather_agent_gpt4o", user_id="user_gpt4o_1", session_id="session_gpt4o_1")
   runner1 = Runner(agent=weatherAgentGPT4o.agent, session_service=session_service, app_name="weather_agent_gpt4o")
   await call_agent_async("What is the weather like in Hanoi?", runner1, session1.id, session1.user_id)

   weatherAgentClaude = WeatherAgentClaude()
   session2 = session_service.create_session(app_name="weather_agent_claude", user_id="user_claude_1", session_id="session_claude_1")
   runner2 = Runner(agent=weatherAgentClaude.agent, session_service=session_service, app_name="weather_agent_claude")
   await call_agent_async("What is the weather like in HoChiMinh?", runner2, session2.id, session2.user_id)

   agent_team = WeatherAgentTeam()
   session3 = session_service.create_session(app_name="weather_agent_team", user_id="user_team_1", session_id="session_team_1")
   runner3 = Runner(agent=agent_team.agent, session_service=session_service, app_name="weather_agent_team")
   await call_agent_async("Hello?",runner3,session3.id,session3.user_id)
   await call_agent_async("What is the weather like in Hanoi?",runner3,session3.id,session3.user_id)
   await call_agent_async("Thank you!",runner3,session3.id,session3.user_id)
 
if __name__ == "__main__":
    asyncio.run(main())

