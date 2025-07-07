import requests
import datetime
import smtplib
import time

LAT = -0.114441
LONG = 37.668558

EMAIL = 'appbreweryinfo@gmail.com'
PASSWORD = 'appbrewery123'

def is_overhead():
    """Check if the ISS is currently overhead."""
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data['iss_position']['latitude'])
    iss_long = float(data['iss_position']['longitude'])
    
    # Check if the ISS is within 5 degrees of the specified latitude and longitude
    return LAT - 5 <= iss_lat <= LAT + 5 and LONG - 5 <= iss_long <= LONG + 5

parameters = {
    'lat': LAT,
    'lng': LONG,
    'formatted': 0
}

def is_night():
    """Check if it is currently night time at the specified location."""
    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
    sunset = data['results']['sunset'].split('T')[1].split(':')[0]
    
    time_now = datetime.datetime.now()
    return not (int(sunrise) <= time_now.hour < int(sunset))

while True:
    time.sleep(60)
    print("Checking if the ISS is overhead and if it's night time...")
    if is_overhead() and is_night():
        connection = smtplib.SMTP('smtp.gmail.com', 587)
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject:Look Up!\n\nThe ISS is currently overhead and it's night time. Go outside and look up!"
        )
        connection.close()