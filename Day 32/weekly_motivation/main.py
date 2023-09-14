import smtplib, datetime, sys, random

SENDING_EMAIL = "ola.jacunski@gmail.com"#"pythola@hotmail.com"
try:
    PASSWORD = sys.argv[1]
except IndexError:
    print("Please enter a password.")
    quit()

todays_day = datetime.datetime.now().weekday()
if todays_day == 3:
    with open("quotes.txt") as f:
        lines = f.readlines()
        quotation = random.choice(lines)
    print(quotation)
    #with smtplib.SMTP("smtp.office365.com",587, timeout=60) as connection:
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=60) as connection:
        connection.starttls()
        connection.login(user="ola.jacunski", password=PASSWORD)
        connection.sendmail(
            from_addr=SENDING_EMAIL,
            to_addrs="alexandra.jacunski@gmail.com",
            msg=f"Subject: Today's inspo\n\n{quotation}"
        )