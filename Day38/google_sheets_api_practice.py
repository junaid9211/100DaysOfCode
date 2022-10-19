import requests
import os
from datetime import datetime

# a simple workout tracking script that uses sheety API to save workout logs to google sheets

# step 1: get data from nutritionix
APP_ID = os.environ['NUTRITIONIX_ID']
APP_KEY = os.environ['NUTRITIONIX_KEY']

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
}

text = input('Tell me which exercise you did: ')

query = {
    "query": text,
    "gender": "male",
    "age": 21
}

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
response = requests.post(nutritionix_endpoint, json=query, headers=headers)
exercise_data = [(i['name'], i['duration_min'], i['nf_calories']) for i in response.json()['exercises']]


# step 2: put that data in google sheet
date = datetime.now().strftime('%Y/%m/%d')
time = datetime.now().strftime('%X')

sheety_endpoint = 'https://api.sheety.co/dafa774f083c116fb50765a2137c954f/workoutTracking/workouts'

for exercise, duration, calories in exercise_data:
    data = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise,
            'duration': str(duration),
            'calories': str(calories)
        }
    }

    try:
        response = requests.post(url=sheety_endpoint, json=data, auth=(os.environ['SHEETY_USERNAME'], os.environ['SHEETY_PASSWORD']))
        response.raise_for_status()
    except:
        print('failed to upload data, please try again')
    else:
        print(f'Uploaded data: {response.json()}')