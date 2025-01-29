## Duplicated from Day 40 and adjusted to send to self

import os, smtplib
from dotenv import load_dotenv

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, message: str = "Subject:Test\n\nTesting testing 1 2 3"):
        load_dotenv()
        self.SMTP = os.getenv("SMTP_ADDRESS")
        self.EMAIL = os.getenv("EMAIL")
        self.PASSWORD = os.getenv("PASSWORD")
        self.send_email(text=message)

    def send_email(self, text: str):
        with smtplib.SMTP(self.SMTP, 587) as connection:
            connection.starttls()
            connection.login(user=self.EMAIL, password=self.PASSWORD)
            connection.sendmail(from_addr=self.EMAIL, to_addrs=self.EMAIL, msg=text.encode())

if __name__ == "__main__":
    notification_manager = NotificationManager()