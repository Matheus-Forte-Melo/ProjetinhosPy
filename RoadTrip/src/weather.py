import requests


class Weather:

    def __init__(self):
        api_key = '24f327610dbe9fd97ec8cc75735176be'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={"jaragua do sul"}&appid={api_key}'

        self.weather_dict = requests.get(url).json()

    def get_weather(self):
        weather = self.weather_dict['weather'][0]['main']
        return weather

    def get_temperature(self):
        temperature = self.weather_dict['main']['feels_like'] - 273.15
        return temperature
