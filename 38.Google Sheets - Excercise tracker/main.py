import requests
from datetime import datetime

API_URL = 'https://680.mockapi.io/api/v1/'

habits = ['Running', 'Reading', 'Meditation', 'Yoga', 'Cooking']
date_today = datetime.now().strftime('%d-%m-%Y')

for habit in habits:
    payload = {
        'habit': habit,
        'date': date_today,
        'status': 'Completed'
    }
    
    response = requests.post(API_URL, json=payload)
    
    if response.status_code == 201:
        print(f'Successfully logged {habit} for {date_today}')
    else:
        print(f'Failed to log {habit}: {response.status_code} - {response.text}')

def view_habits():
    response = requests.get(f'{API_URL}habits')
    
    if response.status_code == 200:
        habits_data = response.json()
        for habit in habits_data:
            print(f"{habit['date']}: {habit['habit']} - {habit['status']}")
    else:
        print(f'Failed to retrieve habits: {response.status_code} - {response.text}')

view_habits()