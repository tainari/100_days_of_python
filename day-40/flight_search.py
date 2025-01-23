import datetime, json, requests

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.start_airport = "NYC"
        with open("../info.json") as f:
            info = json.load(f)
        self._client_id = info["amadeus_api_key"],
        self._client_secret = info["amadeus_api_secret"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "grant_type": "client_credentials"
        }
        response = requests.post(TOKEN_ENDPOINT, headers=headers, data=body)
        return response.json()['access_token']


    def check_route_price(self, destination_airport: str, max_price: int, nonstop: bool = True):
        headers = {"Authorization": f"Bearer {self._token}"}
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
        in_six_months = datetime.datetime.now() + datetime.timedelta(days=180)
        query = {
            "originLocationCode": self.start_airport,
            "destinationLocationCode": destination_airport,
            "departureDate": tomorrow.strftime("%Y-%m-%d"),
            "returnDate": in_six_months.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if nonstop else "false",
            "maxPrice": max_price,
            "currencyCode": "USD",
            "max": 10
        }
        response = requests.get(
            url = FLIGHT_SEARCH_ENDPOINT,
            headers = headers,
            params = query
        )
        if response.status_code != 200:
            print("There was a problem with the query. Please check the destination airport IATA code.")
            return None

        return response.json()
