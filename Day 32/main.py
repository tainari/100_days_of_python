import csv, datetime, random, re, smtplib, sys

RANDOM_SUBJECTS = ["Hello","Howdy","Hey hey hey", "Hey girl heyyyyyy"]
RANDOM_CONTENT = ["You look fab","Love the hair today","Is that outfit new?","omg great earrings"]
SENDING_EMAIL = "pythola@hotmail.com"
try:
    PASSWORD = sys.argv[1]
except IndexError:
    print("Please enter a password.")
    quit()

today = datetime.datetime.today()
todays_day = today.day
todays_month = today.month
todays_year = today.year

with open("birthdays.csv") as f:
    rd = csv.reader(f)
    next(rd,None)
    for name, email, year, month, day in rd:
        if int(month) == todays_month and int(day) == todays_day:
            letter_choice = random.choice([1,2,3])
            with open(f'letter_templates/letter_{letter_choice}.txt') as f:
                content = ('').join(f.readlines()) + f"\n\nP.S. {random.choice(RANDOM_CONTENT)}"
                content = re.sub("\[NAME\]", name, content)
                print(content)
            with smtplib.SMTP("smtp.office365.com", 587) as connection:
                connection.starttls()
                connection.login(user="pythola@hotmail.com", password=PASSWORD)
                connection.sendmail(
                    from_addr=SENDING_EMAIL,
                    to_addrs=email,
                    msg=f"Subject: Happy Birthday!\n\n{content}"
                )




