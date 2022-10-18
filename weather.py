import requests

# Geocoding API Call format "http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}"
# API Call string for Weather Forecast "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"

API_KEY = "afae450e8d18b25dbbae347979225640"
BASE_URL = "http://api.openweathermap.org/geo/1.0/direct"
BASE_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    lat = data[0]['lat']
    lon = data[0]['lon']
    request_weather_url = f"{BASE_WEATHER_URL}?lat={lat}&lon={lon}&appid={API_KEY}"
    weather_response = requests.get(request_weather_url)
    if weather_response.status_code == 200:
        data2 = weather_response.json()
        weather = data2["weather"][0]["description"]
        print("Weather:", weather)
        temperature = data2["main"]["temp"]
        temp_in_f = 1.8 * (temperature - 273) + 32
        print("Temperature:",round(temp_in_f, 1),"degrees Fahrenheit")
    else:
        print("An error occurred in weather.")
else:
    print("An error occurred.")

