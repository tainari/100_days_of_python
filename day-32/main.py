import datetime as dt, json, os, pandas, random, smtplib

## JSON file with my email and google app password. Not uploaded to github :)
with open("info.json") as f:
    data = json.load(f)

EMAIL = data["email"]
PASSWORD = data["password"]

with open("birthdays.csv") as f:
    birthdays = pandas.read_csv(f)

letter_templates = []
for filename in os.listdir("./letter_templates"):
    f = os.path.join("./letter_templates", filename)
    if os.path.isfile(f) and filename.endswith(".txt"):
        letter_templates.append(f)

today = dt.datetime.now()
year = today.year
month = today.month
day = today.day

for index, row in birthdays.iterrows():
    if today.month == row["month"] and today.day == row["day"]:
        letter_template = random.choice(letter_templates)
        with open(letter_template) as f:
            message = f.read()
        message = message.replace("[NAME]", row["name"])
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=row['email'], msg=message)