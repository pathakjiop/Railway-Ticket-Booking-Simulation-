# src/manager.py
import os
from src.ticket import Ticket
from typing import List

DATA_FILE = os.path.join("data", "tickets.csv")

class TicketManager:
    def __init__(self, total_seats: int = 50):
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.tickets: List[Ticket] = []
        self.next_ticket_id = 1
        os.makedirs("data", exist_ok=True)
        self.load_from_file()

    def load_from_file(self):
        if not os.path.exists(DATA_FILE):
            return
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    t = Ticket.from_csv_row(line)
                    if t:
                        self.tickets.append(t)
                        if t.ticket_id >= self.next_ticket_id:
                            self.next_ticket_id = t.ticket_id + 1
                        self.available_seats -= t.seats_booked
        except Exception as e:
            print(f"Failed to load data: {e}")

    def save_to_file(self):
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                for t in self.tickets:
                    f.write(t.to_csv_row() + "\n")
        except Exception as e:
            print(f"Failed to save data: {e}")

    def book_ticket(self, name: str, age: int, train_no: int, seats: int) -> (bool, int):
        if seats <= 0:
            return False, -1
        if seats <= self.available_seats:
            t = Ticket(self.next_ticket_id, name, age, train_no, seats)
            self.tickets.append(t)
            self.available_seats -= seats
            self.next_ticket_id += 1
            self.save_to_file()
            return True, t.ticket_id
        else:
            return False, -1

    def get_all_tickets(self):
        return list(self.tickets)

    def cancel_ticket_by_id(self, ticket_id: int) -> bool:
        for t in self.tickets:
            if t.ticket_id == ticket_id:
                self.tickets.remove(t)
                self.available_seats += t.seats_booked
                self.save_to_file()
                return True
        return False

    def find_ticket_by_name(self, name: str):
        return [t for t in self.tickets if t.passenger_name.lower() == name.lower()]
