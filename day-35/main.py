import json, os, requests, smtplib

URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ['OWM_API_KEY']
NYC_LAT = 40.712776
NYC_LNG = -74.009371
## Rennes, France latlong info because it was raining at the time of testing this script :)
# LAT = 48.114700
# LNG =  -1.679400
PARAMS = {
    "lat": NYC_LAT,
    "lon": NYC_LNG,
    "appid": API_KEY
}

result = requests.get(URL, params=PARAMS)
weather_data = result.json()['list']
will_rain = False
for item in weather_data[:5]:
    for condition in item['weather']:
        if condition['id'] < 600: # team no umbrella for snow
            will_rain = True
            print("It's raining!")
            break

if will_rain:
    ## JSON file with my email and google app password. Not uploaded to github :)
    with open("../info.json") as f:
        data = json.load(f)
    EMAIL = data["email"]
    PASSWORD = data["password"]
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg="Subject: It'll rain today! \n\n Take an umbrella!")