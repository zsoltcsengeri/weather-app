import requests
import streamlit as st
import json


@st.cache_data(ttl=86400)
def fetch_weather(city: str):
    """
    Fetch weather data for a given city using the OpenWeather API.
    The result is cached for 24 hours (86400 seconds).

    Args:
        city (str): The name of the city to fetch the weather for.

    Returns:
        dict: The JSON response from the OpenWeather API.
    """
    API_KEY = st.secrets["openweather"]["api_key"]
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,  # Dynamically pass the city name here
        "units": "metric",
        "appid": API_KEY,
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()


# Example usage
data = fetch_weather("London")
print(json.dumps(data, indent=4))  # Pretty-print with indentation
