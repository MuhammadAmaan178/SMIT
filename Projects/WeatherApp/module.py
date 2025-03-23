import requests

# Function to get weather data
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  # `units=metric` gives temperature in Celsius
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']

        main = data['main']
        temperature = main['temp']
        temp_min = main['temp_min']
        temp_max = main['temp_max']
        pressure = main['pressure']
        humidity = main['humidity']
        sea_level = main['sea_level']

        sys = data['sys']
        country = sys['country']

        wind_speed = data['wind']['speed']

        return city,country,weather_description, temperature,temp_min,temp_max,pressure,humidity,sea_level,wind_speed
    else:
        return None