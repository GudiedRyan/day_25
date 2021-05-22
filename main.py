#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch

dm = DataManager()
nm = NotificationManager()
fs = FlightSearch()


sheet_data = dm.get_data()

# No longer nee to use this, as the code are now updated.
def update_codes():
    for location in sheet_data["prices"]:
        if location["iataCode"] == "":
            code = fs.add_code(location["city"])
            location["iataCode"] = code
    dm.send_data(sheet_data)


def find_flights():
    for location in sheet_data["prices"]:
        cheapest_flight = fs.find_flights(location["iataCode"])
        try:
            if cheapest_flight.price < location["lowestPrice"]:
                nm.send_email(message=f"Subject: Cheap Flight! \n\nFlight to {cheapest_flight.destination_city} for only for {cheapest_flight.price} leaving on {cheapest_flight.out_date}!")
        except AttributeError:
            print("No flights available")
find_flights()