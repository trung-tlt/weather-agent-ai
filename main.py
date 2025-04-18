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

  final_response_text = "Agent did not produce a final response."

  async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
      # print(f"  [Event] Author: {event.author}, Type: {type(event).__name__}, Final: {event.is_final_response()}, Content: {event.content}")

      if event.is_final_response():
          if event.content and event.content.parts:
             # Assuming text response in the first part
             final_response_text = event.content.parts[0].text
          elif event.actions and event.actions.escalate: # Handle potential errors/escalations
             final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
          # Add more checks here if needed (e.g., specific error codes)
          break # Stop processing events once the final response is found

  print(f"<<< Agent Response: {final_response_text}")

async def GetWeatherInformationWithContextAsync(session_service):
    initial_state = {
      "user_preference_temperature_unit": "Celsius"
   }

    agent_team = WeatherAgentTeam()
    session_service.create_session(
       app_name="weather_agent_team", 
       user_id="user_team_1", 
       session_id="session_team_1", 
       state=initial_state
   )
    runner3 = Runner(agent=agent_team.agent, session_service=session_service, app_name="weather_agent_team")
   
    print("\n--- Testing State: Temp Unit Conversion & output_key ---")

   # 1. Check weather (Uses initial state: Celsius)
    print("--- Turn 1: Requesting weather in Hanoi (expect Celsius) ---")
    await call_agent_async(query= "What's the weather in Hanoi?",runner=runner3,user_id="user_team_1",session_id="session_team_1")

   # 2. Update state preference to Fahrenheit
    print("\n--- Updating State: Setting unit to Fahrenheit ---")
    try:
         # Get the current session
          current_session = session_service.get_session(
             app_name="weather_agent_team", 
             user_id="user_team_1", 
             session_id="session_team_1"
         )
         # Create a new session with updated state
          new_state = dict(current_session.state)
          new_state["user_preference_temperature_unit"] = "Fahrenheit"
          updated_session = session_service.create_session(
             app_name="weather_agent_team",
             user_id="user_team_1",
             session_id="session_team_1",
             state=new_state
         )
          print(f"--- Session state updated. Current 'user_preference_temperature_unit': {updated_session.state['user_preference_temperature_unit']} ---")
    except Exception as e:
          print(f"--- Error updating session state: {e} ---")

   # 3. Check weather again (Tool should now use Fahrenheit)
    print("\n--- Turn 2: Requesting weather in Danang (expect Fahrenheit) ---")
    await call_agent_async(query= "Tell me the weather in Danang.",
                           runner=runner3,
                           user_id="user_team_1",
                           session_id="session_team_1"
                           )

   # 4. Test basic delegation (should still work)
    print("\n--- Turn 3: Sending a greeting ---")
    await call_agent_async(query= "Hi!",
                           runner=runner3,
                           user_id="user_team_1",
                           session_id="session_team_1"
                           )
    
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

   await GetWeatherInformationWithContextAsync(session_service)
 
if __name__ == "__main__":
    asyncio.run(main())

