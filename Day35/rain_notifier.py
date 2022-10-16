import requests
import os
from datetime import datetime
from twilio.rest import Client

suk_params = {
    'lat': 27.724356,
    'lon': 68.822807,
    'units': 'metric',
    'appid': os.environ['OPENWEATHERMAP_API']
}

response = requests.get('http://api.openweathermap.org/data/2.5/forecast', params=suk_params)
weather_data = response.json()['list'][:5]

will_rain = False

for item in weather_data:
    weather_id = item['weather'][0]['id']

    if weather_id < 700:
        will_rain = True

        forecast = {
            'description': item['weather'][0]['description'],
            'temp': item['main']['temp'],
            'time': str(datetime.utcfromtimestamp(item['dt'] + 18000))
        }
        print(forecast)
        break

print(f"Will rain: {will_rain}")

if will_rain:
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"Bring an umbrella ☔ , forecast says {forecast['description']}\
                        it will rain on {forecast['time']}",
        messaging_service_sid='MG6dd65ad170feeee719dc13ca2c4131d4',
        to=os.environ['MY_NUM']
    )
    print('Message sent successfully')
