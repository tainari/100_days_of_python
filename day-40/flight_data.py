class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, data: dict, direct: bool = True):
        self.is_direct = direct
        self.price = data[0]['price']['total']
        self.depart_airport = data[0]['itineraries'][0]['segments'][0]['departure']['iataCode']
        self.outbound_date = data[0]['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
        if direct:
            self.arrive_airport = data[0]['itineraries'][0]['segments'][0]['arrival']['iataCode']
        else:
            self.stopover_airport = data[0]['itineraries'][0]['segments'][0]['arrival']['iataCode']
            self.arrive_airport = data[0]['itineraries'][0]['segments'][1]['arrival']['iataCode']
        self.inbound_date = data[0]['itineraries'][0]['segments'][0]['arrival']['at'].split('T')[0]

    def format_data(self):
        stopover_text = ""
        if not self.is_direct:
            stopover_text = f" with a stopover in {self.stopover_airport}"
        text = f"""Subject:Low price alert! {self.depart_airport}-->{self.arrive_airport}\n\n
        ${self.price} to fly from {self.depart_airport} to {self.arrive_airport}. Depart {self.outbound_date}; arrive {self.arrive_airport}{stopover_text}.
        Remember to search "NYC" for the departure airport; this trip may fly out of one NYC airport and land in another.
        """
        return text
