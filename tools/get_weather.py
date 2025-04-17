# @title Define the get_weather Tool
def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city (e.g., "Hanoi", "HoChiMinh", "Danang").

    Returns:
        dict: A dictionary containing the weather information.
              Includes a 'status' key ('success' or 'error').
              If 'success', includes a 'report' key with weather details.
              If 'error', includes an 'error_message' key.
    """
    # Best Practice: Log tool execution for easier debugging
    print(f"--- Tool: get_weather called for city: {city} ---")
    city_normalized = city.lower().replace(" ", "") # Basic input normalization

    # Mock weather data for simplicity
    mock_weather_db = {
        "hanoi": {"status": "success", "report": "The weather in Hanoi is sunny with a temperature of 25°C."},
        "hochiminh": {"status": "success", "report": "It's cloudy in HoChiMinh with a temperature of 15°C."},
        "danang": {"status": "success", "report": "Danang is experiencing light rain and a temperature of 18°C."},
    }

    # Best Practice: Handle potential errors gracefully within the tool
    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return {"status": "error", "error_message": f"Sorry, I don't have weather information for '{city}'."}