import os
import requests
from twilio.rest import Client

APPID = os.environ.get("appid") # this is the appid basically a key which we first need to generate on the
                                           # API website to get the data from the API endpoint
ACCOUNT_SID = os.environ.get("account_sid")


AUTH_TOKEN = os.environ.get("auth_token") # setting the variable as an environment variable. but now we cannot run the
# code from here we have to run it from terminal.

parameters = {
    "lat": 20.260599,
    "lon": 75.136803,
    'cnt': 4,
    "appid": appid
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params= parameters)
response.raise_for_status()
data = response.json()
# print (data["list"])

is_raining = False
for hour_data in data["list"]:
   weather_id = hour_data["weather"][0]["id"]
   if weather_id > 700:
       is_raining = True
if is_raining:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is going to rain today",
        from_="+12623798378",
        to="+917045355760",
    )


    print(message.body)
