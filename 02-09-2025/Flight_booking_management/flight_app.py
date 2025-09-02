# flight_app.py

from flight_manager import (
    create_flight,
    read_all_flights,
    read_flight_by_id,
    update_flight,
    delete_flight_by_id
)
from flight import Flight

def menu():
    message = '''
Flight Booking Management System
1 - Add Flight
2 - View All Flights
3 - View Flight by ID
4 - Update Flight
5 - Delete Flight
6 - Exit
Your choice: '''
    choice = int(input(message))

    if choice == 1:
        id = int(input("Flight ID: "))
        airline = input("Airline: ")
        origin = input("Origin: ")
        destination = input("Destination: ")
        departure_time = input("Departure Time: ")
        arrival_time = input("Arrival Time: ")
        seats = int(input("Seats: "))
        price = float(input("Price: "))

        flight = Flight(-1, airline, origin, destination, departure_time, arrival_time, seats, price)
        create_flight(flight)
        print("Flight added successfully.")

    elif choice == 2:
        flights = read_all_flights()
        if not flights:
            print("No flights available.")
        else:
            for f in flights:
                print(f)
    elif choice == 3:
        try:
           id = int(input("Enter Flight ID: ").strip())
           flight = read_flight_by_id(id)
           if flight:
              print(flight)
           else:
              print("Flight not found.")
        except ValueError:
           print("Invalid input. Please enter a numeric ID.")

    elif choice == 4:
        id = int(input("Enter Flight ID to update: "))
        old_flight = read_flight_by_id(id)
        if not old_flight:
            print(" Flight not found.")
        else:
            airline = input("Airline: ")
            origin = input("Origin: ")
            destination = input("Destination: ")
            departure_time = input("Departure Time: ")
            arrival_time = input("Arrival Time: ")
            seats = int(input("Seats: "))
            price = float(input("Price: "))

            new_flight = Flight(id, airline, origin, destination, departure_time, arrival_time, seats, price)
            update_flight(new_flight)
            print("Flight updated successfully.")

    elif choice == 5:
        id = int(input("Enter Flight ID to delete: "))
        flight = read_flight_by_id(id)
        if not flight:
            print("Flight not found.")
        else:
            confirm = input("Are you sure you want to delete this flight? (y/n): ")
            if confirm.lower() == 'y':
                delete_flight_by_id(id)
                print("Flight deleted successfully.")

    return choice

def menus():
    choice = menu()
    while choice != 6:
        choice = menu()
    print("Thank you for using the Flight Booking Management System!")

if __name__ == "__main__":
    menus()