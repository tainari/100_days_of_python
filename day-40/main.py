from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

HOME_AIRPORT = "NYC"

destination_data = DataManager()
notification_manager = NotificationManager()

flight_search = FlightSearch()
for destination in destination_data.price_data[-1:]:
    destination_city = destination['city']
    destination_airport = destination['iataCode']
    max_price = destination['lowestPrice']
    results = flight_search.check_route_price(destination_airport, max_price)['data']
    if results:
        flight_data = FlightData(results)
        notification_manager.send_email(flight_data.format_data(), destination_data.user_data)
    else:
        results = flight_search.check_route_price(destination_airport, max_price, nonstop=False)['data']
        if results:
            flight_data = FlightData(results, direct=False)
            notification_manager.send_email(flight_data.format_data(), destination_data.user_data)