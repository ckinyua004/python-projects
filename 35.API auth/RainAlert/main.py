import requests
from twilio.rest import Client

api_key = '69f04e4613056b159c2761a9d9e664d2'
account_sid = 'fibj40r829b3498bf439b439b03445'
auth_token = 'viroqwf40if49034hf09qw34fh09h34'

parameters = {
    'lat': 51.507351,
    'lon': -0.127758,
    'appid': api_key
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast')
print(response.status_code)
response.raise_for_status()
data = response.json()

will_rain = False
for hour_data in data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print('Bring an umbrella')
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body = 'It will rain.',
            from_ = '+15017122661',
            to = '+1543143242'
        )
    
    print(message.status)