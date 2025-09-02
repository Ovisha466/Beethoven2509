# flight.py

class Flight:
    def __init__(self, id, airline, origin, destination, departure_time, arrival_time, seats, price):
        self.id = id
        self.airline = airline
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.seats = seats
        self.price = price

    def __str__(self):
        return (f"[id={self.id}, airline={self.airline}, origin={self.origin}, "
                f"destination={self.destination}, departure={self.departure_time}, "
                f"arrival={self.arrival_time}, seats={self.seats}, price={self.price}]")

    def __repr__(self):
        return self.__str__()