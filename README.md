# 🚆 **Railway Ticket Booking Simulation**

### *A Teaching Evaluation Component (TEC) Project — Software Engineering (5IT03)*

---

## 🧩 **Introduction**

The **Railway Ticket Booking Simulation** is a Python-based application that mimics the basic operations of a railway reservation system.
It allows users to **book**, **view**, and **cancel** train tickets through a simple console interface (and optionally, a Streamlit GUI for cloud demonstration).

This project demonstrates **software engineering principles** such as:

* Modular program design
* Data persistence (via CSV file or database)
* Input validation and data management
* Basic flow control and system simulation

The project is designed for **academic submission** under the **Software Engineering (5IT03)** course at **SSGMCE, Shegaon**.

---

## 🎯 **Objectives**

* To simulate real-world railway ticket booking operations in a simplified environment.
* To implement core programming concepts such as lists, file handling, loops, and conditional logic.
* To provide a hands-on understanding of system design and report documentation as per TEC standards.

---

## ⚙️ **Features**

✅ Book railway tickets (user enters name, age, train number, and number of seats).
✅ View all current bookings in a formatted table.
✅ Cancel ticket by Ticket ID and automatically update available seats.
✅ Persistent data storage using a CSV file.
✅ Displays available seats dynamically.
✅ (Optional) Graphical user interface using Streamlit.

---

## 🧠 **System Workflow**

```
Start → Display Main Menu
     ├── Book Ticket → Check Seats → Confirm Booking
     ├── View All Bookings
     ├── Cancel Ticket → Find Ticket → Update Seats
     └── Exit
```

---

## 🗂️ **File Structure**

```
Railway_Ticket_Booking_Python/
│
├── src/
│   ├── ticket.py        # Ticket class (data model)
│   ├── manager.py       # Core booking logic & persistence
│   └── main.py          # Console menu & main program
│
├── data/
│   └── tickets.csv      # Auto-created file for saving bookings
│
├── README.md            # Project documentation (this file)
└── requirements.txt     # Streamlit dependency (if GUI used)
```

---

## 💻 **How to Run the Console Version**

### **Step 1:** Clone or Download

```bash
git clone https://github.com/<yourusername>/Railway_Ticket_Booking_Python.git
cd Railway_Ticket_Booking_Python
```

### **Step 2:** Run Program

```bash
python -m src.main
```

## 👨‍💻 **Team Members**

| Roll No | Name             |
| ------- | ---------------- |
| 35      | Atharv Pathak    |
| 68      | Shlok Rathi |



---

## 🏁 **Conclusion**

The Railway Ticket Booking Simulation successfully demonstrates the application of software engineering concepts in building a modular and functional system. It covers all phases of software development — requirement analysis, design (block diagram), implementation (Python), and testing.
This project is ideal for academic evaluation, showcasing practical programming, structured documentation, and teamwork.
