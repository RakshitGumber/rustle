from dotenv import load_dotenv
import os

load_dotenv()

WEATHER_API = os.getenv("WEATHER_API")
BASE_URL = "https://api.weatherapi.com/v1"
