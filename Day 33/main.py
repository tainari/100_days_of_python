import datetime, requests, smtplib, sys
import time

SENDING_EMAIL = "ola.jacunski@gmail.com"
try:
    PASSWORD = sys.argv[1]
except IndexError:
    print("Please enter a password.")
    quit()

NYC_LAT = 40.730610
NYC_LONG = -73.935242
NYC_POSITION = (NYC_LAT,NYC_LONG)

response = requests.get("http://api.open-notify.org/iss-now.json")

satellite_latitude = float(response.json()['iss_position']['latitude'])
satellite_longitude = float(response.json()['iss_position']['longitude'])
position = (satellite_latitude,satellite_longitude)

response = requests.get(f"https://api.sunrise-sunset.org/json?lat={NYC_LAT}&lng=-{NYC_LONG}&date=today&formatted=0")
sunrise = datetime.datetime.strptime(response.json()['results']['sunrise'],"%Y-%m-%dT%H:%M:%S+00:00").time()#.split("T")[1].split("+")[0]
sunset = datetime.datetime.strptime(response.json()['results']['sunset'],"%Y-%m-%dT%H:%M:%S+00:00").time()#.split("T")[1].split("+")[0]

now = datetime.datetime.now().time()#.split(" ")[1].split(".")[0]

def is_night():
    return now < sunrise or now > sunset

def is_overhead():
    return (abs(satellite_latitude-NYC_LAT) < 5 and abs(satellite_longitude-NYC_LONG) < 5)
def check_location():
    if is_night() and is_overhead():
        send_email()
    else:
        print("Not yet.")
def send_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user="ola.jacunski", password=PASSWORD)
        connection.sendmail(
            from_addr=SENDING_EMAIL,
            to_addrs="alexandra.jacunski@gmail.com",
            msg=f"Subject: Look up!\n\nThere are worlds to conquer. The ISS is in your sky!"
        )

#better to run this on the minute on a server but needs must
while True:
    check_location()
    time.sleep(60)



# ERROR CHEAT SHEET
# 1XX - hold on
# 2XX - here you go
# 3XX - go away
# 4XX - I (the website) screwed up
# 5XX - You (the coder) screwed up