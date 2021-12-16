import requests
import os
from twilio.rest import Client
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12399325376',
                     to=''
                 )

print(message.sid)
para = {
    "lat":"21.1667",
    "lon":"72.8333",
    "appid":"cfef4084e39fda188ddd5a51b68c6095"
}
api = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?",params=para)
data = api.json()
data = data['hourly']
for n in range(0,12):
    if data[n]['weather'][0]["main"] == "Rain":
        print("oh no oh no oh no no no")

