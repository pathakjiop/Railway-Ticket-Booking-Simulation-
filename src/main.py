# src/main.py
from src.manager import TicketManager

def display_menu(available_seats):
    print("\n======================================")
    print("     RAILWAY TICKET BOOKING SYSTEM")
    print("======================================")
    print(f"Available Seats: {available_seats}")
    print("1. Book Ticket")
    print("2. View Bookings")
    print("3. Cancel Ticket")
    print("4. Exit")
    return input("Enter your choice: ").strip()

def do_book(manager: TicketManager):
    name = input("Enter Passenger Name: ").strip()
    try:
        age = int(input("Enter Age: ").strip())
        train = int(input("Enter Train Number: ").strip())
        seats = int(input("Enter Seats to Book: ").strip())
    except ValueError:
        print("Invalid numeric input.")
        return
    ok, tid = manager.book_ticket(name, age, train, seats)
    if ok:
        print(f"Booking Successful! Ticket ID: {tid}")
        print(f"Remaining Seats: {manager.available_seats}")
    else:
        print("Booking Failed: Not enough seats or invalid input.")

def do_view(manager: TicketManager):
    tickets = manager.get_all_tickets()
    if not tickets:
        print("No bookings yet.")
        return
    print("\n--- All Bookings ---")
    print(f"{'TicketID':<8} | {'Name':<12} | {'Age':<3} | {'Train':<6} | {'Seats':<5} | Time")
    print("-"*70)
    for t in tickets:
        print(f"{t.ticket_id:<8} | {t.passenger_name:<12} | {t.age:<3} | {t.train_no:<6} | {t.seats_booked:<5} | {t.booking_time}")

def do_cancel(manager: TicketManager):
    try:
        tid = int(input("Enter Ticket ID to Cancel: ").strip())
    except ValueError:
        print("Invalid Ticket ID.")
        return
    ok = manager.cancel_ticket_by_id(tid)
    if ok:
        print("Ticket cancelled successfully.")
        print(f"Remaining Seats: {manager.available_seats}")
    else:
        print("No ticket found with that ID.")

def main():
    manager = TicketManager(total_seats=50)
    while True:
        choice = display_menu(manager.available_seats)
        if choice == "1":
            do_book(manager)
        elif choice == "2":
            do_view(manager)
        elif choice == "3":
            do_cancel(manager)
        elif choice == "4":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
