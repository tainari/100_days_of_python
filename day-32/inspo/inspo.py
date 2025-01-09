import datetime as dt, json, random, smtplib

## JSON file with my email and google app password. Not uploaded to github :)
with open("info.json") as f:
    data = json.load(f)

with open("quotes.txt") as f:
    quotes = f.readlines()


EMAIL = data["email"]
PASSWORD = data["password"]

today = dt.datetime.now().weekday()
if today == 2:
    message = f"""Subject: Inspirational quote of the day\n\n    
    {random.choice(quotes).encode('ascii', 'ignore').decode('ascii')}
    """
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=message)