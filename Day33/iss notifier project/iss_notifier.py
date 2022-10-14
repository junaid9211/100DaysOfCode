import requests
from datetime import datetime
import smtplib
from email.message import EmailMessage
import os
import time

MY_POSITION = {
    'latitude': 27.724356,
    'longitude': 68.822807
}

# Step 1: get latitude and longitude of iss
response = requests.get('http://api.open-notify.org/iss-now.json')
iss_data = response.json()['iss_position']

ISS_POSITION = {
    'latitude': float(iss_data['latitude']),
    'longitude': float(iss_data['longitude'])
}

# Step 2: get your sunset time
params = {
    'lat': MY_POSITION['latitude'],
    'lng': MY_POSITION['longitude'],
    'formatted': 0
}
response = requests.get('https://api.sunrise-sunset.org/json', params=params)
SUNRISE = int(response.json()['results']['sunrise'].split('T')[1].split(':')[0])
SUNSET = int(response.json()['results']['sunset'].split('T')[1].split(':')[0])



def check_position():
    # if iss lat/lng is +5 or -5 my lat/lng  then return True
    good_latitude = MY_POSITION['latitude'] - 5 < ISS_POSITION['latitude'] < MY_POSITION['latitude'] + 5
    good_longitude = MY_POSITION['longitude'] - 5 < ISS_POSITION['longitude'] < MY_POSITION['longitude'] + 5

    return good_latitude and good_longitude


def check_time():
    # if the time is between sunset and sunrise then good
    hour = datetime.now().hour
    return (hour >= SUNSET) or (hour <= SUNRISE)


def send_email():
    email = os.environ['GMAIL1']
    password = os.environ['GMAIL1_PASS']

    msg = EmailMessage()
    msg['Subject'] = 'Look up 👆'
    msg['From'] = email
    msg['To'] = email
    msg.set_content('ISS is up in the sky, go check it out')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as conn:
        conn.login(email, password)
        conn.send_message(msg)


# email me if my lat/lng matches with the lat/lng of iss, and it is the time between sunset and sunrise
while True:
    if check_position() and check_time():
        send_email()

    time.sleep(60)
