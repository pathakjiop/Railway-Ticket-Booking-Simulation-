# src/ticket.py
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Ticket:
    ticket_id: int
    passenger_name: str
    age: int
    train_no: int
    seats_booked: int
    booking_time: str = None

    def __post_init__(self):
        if self.booking_time is None:
            self.booking_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_csv_row(self):
        return f"{self.ticket_id},{self.passenger_name},{self.age},{self.train_no},{self.seats_booked},{self.booking_time}"

    @staticmethod
    def from_csv_row(row: str):
        parts = row.strip().split(",")
        if len(parts) < 6:
            return None
        tid = int(parts[0])
        name = parts[1]
        age = int(parts[2])
        train = int(parts[3])
        seats = int(parts[4])
        time = parts[5]
        return Ticket(tid, name, age, train, seats, time)
