# flight_manager.py

flights = []

def create_flight(flight):
    """Add a new flight."""
    global flights
    if len(flights) == 0:
        flight.id = 1
    else:
        flight.id = flights[-1].id + 1
    flights.append(flight)

def read_all_flights():
    return flights

def read_flight_by_id(id):
    try:
        id = int(id)  # make sure ID is integer
    except ValueError:
        return None

    for flight in flights:
        if flight.id == id:
            return flight
    return None

def update_flight(flight):
    old_flight = read_flight_by_id(flight.id)
    if old_flight is None:
        return
    old_flight.airline = flight.airline
    old_flight.origin = flight.origin
    old_flight.destination = flight.destination
    old_flight.departure_time = flight.departure_time
    old_flight.arrival_time = flight.arrival_time
    old_flight.seats = flight.seats
    old_flight.price = flight.price

def delete_flight_by_id(id):
    flight = read_flight_by_id(id)
    if flight:
        flights.remove(flight)