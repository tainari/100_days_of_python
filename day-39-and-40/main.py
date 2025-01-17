#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

HOME_AIRPORT = "NYC"

# things to do
# get destinations of interest and price ceilings from google sheet
# find all routes between home airport and destinations
# find if any routes are below the cutoff
# emai if they are (send details)

destination_data = DataManager()
