import requests
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "f4b85b43229c9533232a8803096419fa"
weather_params = {
    "lat": 49.895077,
    "lon": -97.138451,
    "appid": api_key,
    "exclude": "current,minutely,daily",
    "cnt": 4,
    "units": "metric"
}
city_name = "winnipeg,canada"
response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
