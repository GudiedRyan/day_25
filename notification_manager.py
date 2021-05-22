import smtplib
import os
import requests

class NotificationManager:
    
    def __init__(self):
        self.email_address = "yesmanvong@gmail.com"
        self.password = os.environ["yesmanvongpass"]
        
    def send_email(self, message: str):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.email_address, password=self.password)
            connection.sendmail(
                from_addr=self.email_address,
                to_addrs="gudiedryan@gmail.com",
                msg=message
            )
        print("Message sent")