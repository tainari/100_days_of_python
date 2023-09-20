import requests, sys
from twilio.rest import Client

APIKEY = sys.argv[1]
account_sid = sys.argv[2]
auth_token = sys.argv[3]

# NOTE TO SELF: THE OTHER WAY TO DO IT.
# IN COMMAND LINE: export OWS_API_KEY=key_goes_here_no_quotations
# IN PYTHON: APIKEY = os.environ.get("OWS_API_KEY")
# And then do the same for the others

CITY = "New York,NY"
NYC_LAT = 40.730610  # 63.4305 - Trondheim, where it was raining when I was testing this code
NYC_LONG = -73.935242  # 10.3951 - Trondheim, where it was raining when I was testing this code

BASE_URL = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": NYC_LAT,
    "lon": NYC_LONG,
    "appid": APIKEY,
}

# API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={NYC_LAT}&lon={NYC_LONG}&appid={APIKEY}"#f"http://api.openweathermap.org/geo/1.0/direct?q={CITY}&limit=5&appid={APIKEY}"

result = requests.get(BASE_URL, params=parameters)
next_12_hours = result.json()['hourly'][:12]

will_rain = False
for a in next_12_hours:
    if int(a['weather'][0]['id']) < 600:
        # print("It's gonna rain!")
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+18885992395',
        body="It's gonna rain today!",
        to='+16465888715'
    )
