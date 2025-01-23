import json, smtplib
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        with open('../info.json') as f:
            contents = json.load(f)
            self.EMAIL = contents['email']
            self.PASSWORD = contents['password']

    def send_email(self, text: str):
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=self.EMAIL, password=self.PASSWORD)
            connection.sendmail(from_addr=self.EMAIL, to_addrs=self.EMAIL, msg=text.encode())