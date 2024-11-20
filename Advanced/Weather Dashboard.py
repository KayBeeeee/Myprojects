"""
Weather Dashboard using OpenWeatherMap API
-------------------------------------------
This project creates a custom website that displays real-time weather information for a city entered by the user.

Features:
- Fetches weather data using the OpenWeatherMap API.
- Displays temperature, weather conditions, and more.
- Responsive and easy-to-navigate web interface built with Flask.

Requirements:
- Flask (for the web server)
- Requests (for API integration)
"""

from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

# OpenWeatherMap API Key
API_KEY = 'your_openweathermap_api_key'  # Replace with your API key

# HTML Templates as strings (Embedded)
INDEX_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Dashboard</title>
</head>
<body>
    <h1>Weather Dashboard</h1>
    <form action="/weather" method="POST">
        <input type="text" name="city" placeholder="Enter city name" required>
        <button type="submit">Get Weather</button>
    </form>
</body>
</html>
"""

WEATHER_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather for {{ weather.city }}</title>
</head>
<body>
    <h1>Weather in {{ weather.city }}</h1>
    <p>Temperature: {{ weather.temperature }}°C</p>
    <p>Condition: {{ weather.description }}</p>
    <img src="{{ weather.icon }}" alt="Weather icon">
    <a href="/">Search another city</a>
</body>
</html>
"""

ERROR_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ error }}</p>
    <a href="/">Try again</a>
</body>
</html>
"""

@app.route('/')
def home():
    """
    Renders the home page with a search bar for weather information.
    """
    return render_template_string(INDEX_HTML)

@app.route('/weather', methods=['POST'])
def weather():
    """
    Fetches weather data for the requested city and displays it.
    """
    city = request.form['city']
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
        }

        return render_template_string(WEATHER_HTML, weather=weather_data)
    except requests.exceptions.RequestException:
        error_message = "Could not fetch weather data. Please try again later."
        return render_template_string(ERROR_HTML, error=error_message)

if __name__ == "__main__":
    app.run(debug=True)
