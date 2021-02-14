# Raspberry Pi Weather Server #

Simple web server that lives on a Raspberry Pi and displays the current weather on an RGB LED matrix.

## Build and Run ##
```
sudo apt install python3-flask
export FLASK_APP=weather
export FLASK_ENV=development
export PRIVATE_API_KEY=<OpenWeatherMap API key>
flask run
```
