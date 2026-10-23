from abc import ABC, abstractmethod

# --- ABSTRACTION & INHERITANCE ---
class Passenger(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @abstractmethod
    def get_discount_percentage(self):
        pass

    def get_passenger_type(self):
        return self.__class__.__name__.replace("Passenger", "")

class RegularPassenger(Passenger):
    def get_discount_percentage(self):
        return 0.0

class StudentPassenger(Passenger):
    def get_discount_percentage(self):
        return 0.10

# --- CLASS & OBJECT & ENCAPSULATION ---
class Flight:
    def __init__(self, flight_code, airline, source, destination, seats, base_fare):
        self._flight_code = flight_code
        self._airline = airline
        self._source = source
        self._destination = destination
        self._available_seats = seats
        self._base_fare = base_fare

    @property
    def flight_code(self):
        return self._flight_code
    
    @property
    def available_seats(self):
        return self._available_seats

    @property
    def base_fare(self):
        return self._base_fare

    def can_book(self, ticket_count):
        return ticket_count <= self._available_seats

    def confirm_seats(self, ticket_count):
        self._available_seats -= ticket_count

    def display(self):
        print(f"{self._flight_code} | {self._airline} | {self._source} to {self._destination} | Seats: {self._available_seats} | Fare: {self._base_fare}")

class Booking:
    booking_counter = 100

    def __init__(self, passenger, flight, ticket_count):
        Booking.booking_counter += 1
        self.booking_id = f"BK{Booking.booking_counter}"
        self.passenger = passenger
        self.flight = flight
        self.ticket_count = ticket_count
        self.base_fare_per_ticket = flight.base_fare
        self.subtotal = self.base_fare_per_ticket * ticket_count
        # POLYMORPHISM - same method on different objects
        self.discount_amount = self.subtotal * passenger.get_discount_percentage()
        self.final_amount = self.subtotal - self.discount_amount

class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Kiran Air", "Mumbai", "Bengaluru", 15, 3500),
            Flight("PH303", "Kiran Air", "Pune", "Hyderabad", 25, 3000)
        ]
        self.bookings = []
        self.last_booking = None

    def find_flight_by_code(self, code):
        for f in self.flights:
            if f.flight_code.lower() == code.lower():
                return f
        return None

    def display_flights(self):
        print("\n--- Available Flights ---")
        for f in self.flights:
            f.display()

    def validate_booking_details(self, flight_code, name, age, ticket_count):
        if not self.find_flight_by_code(flight_code):
            return False, "Booking failed: Flight code does not exist."
        if not name or not name.strip():
            return False, "Booking failed: Passenger name cannot be blank."
        if age <= 0:
            return False, "Booking failed: Age must be greater than 0."
        if ticket_count <= 0:
            return False, "Booking failed: Ticket count must be greater than 0."
        flight = self.find_flight_by_code(flight_code)
        if not flight.can_book(ticket_count):
            return False, f"Booking failed: Not enough seats available. Available: {flight.available_seats}"
        return True, ""

    def calculate_fare(self, booking):
        # Already calculated in Booking class
        return booking.final_amount

    def confirm_booking(self, booking):
        booking.flight.confirm_seats(booking.ticket_count)
        self.bookings.append(booking)
        self.last_booking = booking

    def display_summary(self, booking):
        print("\nBooking confirmed!")
        print(f"Booking ID: {booking.booking_id}")
        print(f"Flight: {booking.flight.flight_code} | {booking.flight._source} to {booking.flight._destination}")
        print(f"Passenger: {booking.passenger.name}")
        print(f"Passenger type: {booking.passenger.get_passenger_type()}")
        print(f"Tickets: {booking.ticket_count}")
        print(f"Base fare per ticket: {booking.base_fare_per_ticket}")
        print(f"Subtotal: {booking.subtotal}")
        print(f"{booking.passenger.get_passenger_type()} discount ({int(booking.passenger.get_discount_percentage()*100)}%): {int(booking.discount_amount)}")
        print(f"Final amount: {int(booking.final_amount)}")

    def view_booking(self):
        if not self.last_booking:
            print("\nNo booking found. Please book a flight first.")
            return
        self.display_summary(self.last_booking)

    def run(self):
        while True:
            print("\nWelcome to Kiran Air Booking")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")
            try:
                choice = int(input("Enter choice: ").strip())
            except:
                print("Invalid choice. Please try again.")
                continue

            if choice == 1:
                self.display_flights()
            elif choice == 2:
                code = input("Enter flight code: ").strip()
                name = input("Enter passenger name: ").strip()
                try:
                    age = int(input("Enter age: ").strip())
                    p_type = input("Passenger type (Regular/Student): ").strip()
                    tickets = int(input("Enter number of tickets: ").strip())
                except:
                    print("Booking failed: Invalid age or ticket number.")
                    continue
                
                valid, msg = self.validate_booking_details(code, name, age, tickets)
                if not valid:
                    print(msg)
                    print("No booking was created. Available seats remain unchanged.")
                    continue

                flight = self.find_flight_by_code(code)
                if p_type.lower() == "student":
                    passenger = StudentPassenger(name, age)
                else:
                    passenger = RegularPassenger(name, age)
                
                booking = Booking(passenger, flight, tickets)
                self.confirm_booking(booking)
                self.display_summary(booking)

            elif choice == 3:
                self.view_booking()
            elif choice == 4:
                print("Thank you for using Kiran Air Booking!")
                break
            else:
                print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    system = FlightBookingSystem()
    system.run()