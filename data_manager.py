import requests
import os
from pprint import pprint

class DataManager:
    
    def __init__(self):
        self.sheety_headers = {
            "Authorization": os.environ["sheety_25"]
        }
        self.get_url = "https://api.sheety.co/ea3ed7eba60791731d14bf1ec05768a8/flightDeals/prices"

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
        