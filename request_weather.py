from dotenv import load_dotenv
import requests
import os

load_dotenv()
API = os.getenv("API_KEY")


def get_data():
    weather_data = dict()

    url = f"https://api.openweathermap.org/data/2.5/forecast?q=kiev&appid={API}"
    result = requests.get(url=url).json()["list"]
    for i in range(25):
        weather_data[i] = result[i]

    return weather_data
