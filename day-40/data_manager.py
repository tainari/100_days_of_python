import json, requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # Continuing to use JSON so that I don't have six million env variables
        with open("../info.json") as f:
            info = json.load(f)
        sheety_workout_endpoint = info["sheety_flight_endpoint"]
        sheety_headers = {
            "Authorization": info["sheety_flight_token"],
        }
        response = requests.get(sheety_workout_endpoint, headers=sheety_headers)
        self.data = response.json()['prices']