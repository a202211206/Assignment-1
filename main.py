# main.py
from guest import Guest
from reservation import Reservation
from room import Room
from payment import Payment

def display_menu():
    print("\n--- Hotel Reservation System ---")
    print("1. Make a Reservation")
    print("2. Check Room Availability")
    print("3. View Reservation")
    print("4. Make Payment")
    print("5. Cancel Reservation")
    print("6. Exit")

def create_rooms():
    return [
        Room("2 Queen Beds", 101, 89.95),
        Room("King Bed", 102, 109.99),
        Room("2 Queen Beds", 103, 89.95),
        Room("Suite", 104, 159.99),
        Room("King Bed", 105, 109.99),
        Room("2 Queen Beds", 106, 89.95),
        Room("Double Bed", 107, 79.95),
        Room("Deluxe Suite", 108, 199.99),
        Room("Family Room", 109, 129.99),
        Room("Standard Room", 110, 79.95)
    ]

def find_available_room(rooms):
    for room in rooms:
        if room.check_availability():
            return room
    return None

def main():
    # Create a guest
    guest = Guest("Ted Vera", "tedvera@mac.com", "505-661-1110", "Mastercard")
    
    # Create 10 rooms
    rooms = create_rooms()
    
    # Placeholder for reservation and payment
    reservation = None
    payment = None
    
    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == '1':  # Make a reservation
            if reservation is None:
                available_room = find_available_room(rooms)
                if available_room:
                    available_room.reserve_room()
                    reservation = Reservation(15549850358, "Aug 22, 2010", "Aug 24, 2010", 2, 1)
                    reservation.make_reservation()
                    print(f"Room {available_room.room_number} reserved.")
                else:
                    print("No rooms available.")
            else:
                print("You already have a reservation.")

        elif choice == '2':  # Check room availability
            available_room = find_available_room(rooms)
            if available_room:
                print(f"Room {available_room.room_number} is available.")
            else:
                print("No rooms are available.")

        elif choice == '3':  # View reservation
            if reservation:
                guest.view_reservation(reservation)
            else:
                print("No reservation found.")

        elif choice == '4':  # Make payment
            if reservation and not payment:
                payment = Payment(52523687, 201.48, "Mastercard")
                payment.process_payment()
            else:
                print("Either no reservation found or payment has already been made.")

        elif choice == '5':  # Cancel reservation
            if reservation and reservation.status != "Cancelled":
                reservation.cancel_reservation()
                # Find the room that was reserved and make it available again
                for room in rooms:
                    if not room.availability:
                        room.availability = True
                        break
                print("Reservation cancelled and room is now available.")
            else:
                print("No active reservation to cancel.")

        elif choice == '6':  # Exit
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
