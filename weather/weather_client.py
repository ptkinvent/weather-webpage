import os
import requests
import json
import time

class WeatherClient():
    def __init__(self):
        api_key = os.environ.get('PRIVATE_API_KEY')
        q = 'berkeley,ca,usa'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&units=imperial&appid={api_key}'
        response = requests.get(url)
        self.data = json.loads(response.text)

    def get_current_temperature(self):
        temp = self.data['main']['temp']
        return self.format_temperature(temp)

    def get_high_temperature(self):
        temp = self.data['main']['temp_max']
        return self.format_temperature(temp)

    def get_low_temperature(self):
        temp = self.data['main']['temp_min']
        return self.format_temperature(temp)

    def get_sunrise_time(self):
        sunrise = self.data['sys']['sunrise']
        return self.format_time(sunrise)

    def get_sunset_time(self):
        sunset = self.data['sys']['sunset']
        return self.format_time(sunset)

    def get_feels_like_temperature(self):
        temp = self.data['main']['feels_like']
        return self.format_temperature(temp)

    def get_pressure(self):
        pressure = self.data['main']['pressure']
        return self.format_pressure(pressure)

    def get_humidity(self):
        humidity = self.data['main']['humidity']
        return self.format_humidity(humidity)

    def get_wind_speed(self):
        wind_speed = self.data['wind']['speed']
        return self.format_wind_speed(wind_speed)

    def format_temperature(self, temp):
        return f'{round(temp)}° F'

    def format_time(self, t):
        t = time.strftime('%I:%M %p %Z', time.localtime(t))
        return f'{t}'

    def format_pressure(self, pressure):
        return f'{pressure} Pa'

    def format_humidity(self, humidity):
        return f'{humidity}%'

    def format_wind_speed(self, wind_speed):
        return f'{round(wind_speed)} mph'
