#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch

dm = DataManager()
nm = NotificationManager()
fs = FlightSearch()


sheet_data = dm.get_data()
users_data = dm.get_users()

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
                message = f"Subject: Cheap Flight! \n\nFlight to {cheapest_flight.destination_city} for only for {cheapest_flight.price} leaving on {cheapest_flight.out_date}! There are {cheapest_flight.stop_overs} stop overs!"
                link = f"https://www.google.co.uk/flights?hl=en#flt={cheapest_flight.origin_airport}.{cheapest_flight.destination_airport}.{cheapest_flight.out_date}*{cheapest_flight.destination_airport}.{cheapest_flight.origin_airport}.{cheapest_flight.return_date}"
                for user in users_data["users"]:
                    nm.send_email(
                        to_addrs = user["email"],
                        message=f"{message}\n\n{link}"
                        )
        except AttributeError:
            print("No flights available")
            continue


def add_user():
    dm.add_user()


find_flights()