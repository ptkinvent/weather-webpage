from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from weather.weather_client import WeatherClient

bp = Blueprint('weather', __name__)

@bp.route('/')
def index():
    client = WeatherClient()
    return render_template('weather/index.html',
        curr_temp=client.get_current_temperature(),
        low_temp=client.get_low_temperature(),
        high_temp=client.get_high_temperature(),
        sunset=client.get_sunset_time(),
        sunrise=client.get_sunrise_time(),
        feels_like_temp=client.get_feels_like_temperature(),
        pressure=client.get_pressure(),
        humidity=client.get_humidity(),
        wind_speed=client.get_wind_speed(),
        )
