import os
import requests
from twilio.rest import Client

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
weather_params = {
    "lat": 49.895077,
    "lon": -97.138451,
    "appid": api_key,
    "exclude": "current,minutely,daily",
    "cnt": 4,
    "units": "metric"
}
response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella or maybe just have fun!",
            from_='+19033548044',
            to='+14312763707'
        )
    print(message.status)
