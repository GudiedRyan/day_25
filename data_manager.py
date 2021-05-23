import requests
import os
from pprint import pprint

class DataManager:
    
    def __init__(self):
        self.sheety_headers = {
            "Authorization": os.environ["sheety_25"]
        }
        self.get_url = "https://api.sheety.co/ea3ed7eba60791731d14bf1ec05768a8/flightDeals/prices"
        self.users_url = "https://api.sheety.co/ea3ed7eba60791731d14bf1ec05768a8/flightDeals/users"

    def get_data(self):
        response = requests.get(url=self.get_url, headers=self.sheety_headers)
        return response.json()
    
    def send_data(self, data):
        for location in data["prices"]:
            new_data = {
                "price": {
                    "iataCode": location["iataCode"],
                }
            }
            response = requests.put(url=f"{self.get_url}/{location['id']}", json=new_data, headers=self.sheety_headers)
            pprint(response.json())

    def add_user(self):
        first_name = input("First name: ")
        last_name = input("Last name: ")
        user_email = input("Email: ")
        user_email_conf = input("Type email again for confirmation: ")
        if user_email != user_email_conf:
            print("Sorry, these emails do not match. Please try again.")
            return None
        user_data = {
            "user": {
                "firstname": first_name,
                "lastname": last_name,
                "email": user_email
            }
        }
        response = requests.post(url=self.users_url, json=user_data, headers=self.sheety_headers)
        pprint(response.json())
        return response.json()

    def get_users(self):
        response = requests.get(url=self.users_url, headers=self.sheety_headers)
        return response.json()