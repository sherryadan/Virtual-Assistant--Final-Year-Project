import requests
from datetime import datetime

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        return f"The weather in {city} is {weather_description}. Temperature: {temperature}°C. Humidity: {humidity}%."
    else:
        return "Could not fetch weather information."

def get_current_datetime():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    return f"The current date is {current_date} and the current time is {current_time}."

def main():
    # API key for OpenWeatherMap
    api_key = "820304a266c4ebb8b69309f3d1fa5c6d"
    city = "Lahore"  # You can change this to any city

    # Get current date and time
    current_datetime = get_current_datetime()
    print(current_datetime)

    # Get current weather
    weather_info = get_weather(api_key, city)
    print(weather_info)

if __name__ == "__main__":
    main()
