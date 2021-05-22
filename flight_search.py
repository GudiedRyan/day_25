import os
import requests
import datetime
from flight_data import FlightData

class FlightSearch:
    
    def __init__(self):
        self.url = "#"
        self.api_key = os.environ["kiwi_key"]
        self.url = "https://tequila-api.kiwi.com"
        self.url_search = "https://tequila-api.kiwi.com/v2/search"
        self.headers = {
            "apikey": self.api_key
        }
        self.now = datetime.datetime.now()
        self.six_months = self.now + datetime.timedelta(days=180)

    def add_code(self, city:str):
        query_params = {
            "term": city,
            "location_types": "city"
        }
        
        response = requests.get(url=f"{self.url}/locations/query", headers=self.headers, params=query_params)
        return response.json()["locations"][0]["code"]

    def find_flights(self, city):
        search_params = {
            "fly_from": "LON",
            "fly_to": city,
            "date_from": self.now.strftime("%d/%m/%Y"),
            "date_to": self.six_months.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=self.url_search, params=search_params, headers=self.headers)
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            print("No available flights, sorry")
            return None

        fd = FlightData(
            price=data['price'], 
            origin_city=data['cityFrom'], 
            desintation_city=data['cityTo'], 
            out_date=data["route"][0]["local_departure"].split("T")[0], 
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{fd.destination_city}: £{fd.price}")
        return fd