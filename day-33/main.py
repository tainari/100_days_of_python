import datetime, json, requests, smtplib, time

SUNSET_URL = "https://api.sunrise-sunset.org/json"
ISS_URL = "http://api.open-notify.org/iss-now.json"

NYC_LAT = 40.712776
NYC_LNG = -74.009371

sunset_parameters = {
    "lat": NYC_LAT,
    "lng": NYC_LNG,
    'formatted': 0
}


def iss_is_overhead():
    response = requests.get(url=ISS_URL)
    response.raise_for_status()
    iss_lat = float(response.json()["iss_position"]["latitude"])
    iss_lng = float(response.json()["iss_position"]["longitude"])
    return abs(NYC_LAT - iss_lat) < 5 and abs(NYC_LNG - iss_lng) < 5

def is_night():
    response = requests.get(SUNSET_URL, params=sunset_parameters)
    sunrise_today = int(response.json()['results']["sunrise"].split("T")[1].split("+")[0].split(":")[0])
    sunset_today = int(response.json()['results']["sunset"].split("T")[1].split("+")[0].split(":")[0])
    current_hour = datetime.datetime.now().hour
    return current_hour > sunset_today or current_hour < sunrise_today

while True:
    if iss_is_overhead():
        if is_night(): ## nested IF statements aren't great I guess
            ## JSON file with my email and google app password. Not uploaded to github :)
            with open("info.json") as f:
                data = json.load(f)
            EMAIL = data["email"]
            PASSWORD = data["password"]
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg="Subject: The ISS is overhead! \n \n Look up!")
        else:
            print("ISS is overhead... but you can't see it!")
    else:
        print("Not overhead. Checking again...")
    time.sleep(60)
