# # import random

# # # Dummy data for available buses
# # # Dummy data for available buses
# # BUSES = [
# #     {"id": "B001", "company": "Shabiby", "from": "Dar es Salaam", "to": "Mwanza", "time": "08:00 AM", "price": 45000},
# #     {"id": "B002", "company": "Kiliman", "from": "Dar es Salaam", "to": "Mwanza", "time": "09:30 AM", "price": 47000},
# #     {"id": "B003", "company": "ABC", "from": "Dar es Salaam", "to": "Arusha", "time": "10:00 AM", "price": 40000},
# #     {"id": "B004", "company": "Mwakyusa Express", "from": "Dar es Salaam", "to": "Dodoma", "time": "06:00 AM", "price": 30000},
# #     {"id": "B005", "company": "Kilimanjaro Express", "from": "Arusha", "to": "Moshi", "time": "07:30 AM", "price": 15000},
# #     {"id": "B006", "company": "Super Feo", "from": "Mwanza", "to": "Kahama", "time": "02:00 PM", "price": 22000},
# #     {"id": "B007", "company": "BM Luxury", "from": "Dodoma", "to": "Mbeya", "time": "05:00 AM", "price": 38000},
# #     {"id": "B008", "company": "Dar Express", "from": "Dar es Salaam", "to": "Tanga", "time": "12:00 PM", "price": 25000},
# #     {"id": "B009", "company": "Safari Line", "from": "Arusha", "to": "Dar es Salaam", "time": "09:00 PM", "price": 55000},
# #     {"id": "B010", "company": "Princess Muro", "from": "Mwanza", "to": "Dar es Salaam", "time": "06:00 PM", "price": 50000},
# #     {"id": "B011", "company": "Green Star", "from": "Moshi", "to": "Arusha", "time": "08:15 AM", "price": 14000},
# #     {"id": "B012", "company": "Upendo Express", "from": "Mbeya", "to": "Iringa", "time": "01:00 PM", "price": 12000},
# #     {"id": "B013", "company": "Bunda Coach", "from": "Kahama", "to": "Shinyanga", "time": "03:30 PM", "price": 18000},
# #     {"id": "B014", "company": "NBS Luxury", "from": "Dodoma", "to": "Dar es Salaam", "time": "07:00 AM", "price": 35000},
# #     {"id": "B015", "company": "Classic Bus", "from": "Iringa", "to": "Mbeya", "time": "04:45 PM", "price": 16000},
# # ]


# # def search_buses(query: dict) -> str:
# #     """Simulate search for buses based on from/to city."""
# #     from_city = query.get("from")
# #     to_city = query.get("to")

# #     results = [b for b in BUSES if b["from"].lower() == from_city.lower() and b["to"].lower() == to_city.lower()]

# #     if not results:
# #         return f"No buses found from {from_city} to {to_city}."

# #     output = "Available buses:\n"
# #     for bus in results:
# #         output += f"- {bus['company']} ({bus['id']}): {bus['time']} @ {bus['price']} TZS\n"
# #     return output.strip()

# # def book_bus(data: dict) -> str:
# #     """Simulate booking a bus seat."""
# #     bus_id = data.get("bus_id")
# #     name = data.get("name", "Passenger")

# #     bus = next((b for b in BUSES if b["id"] == bus_id), None)
# #     if not bus:
# #         return f"Bus with ID {bus_id} not found."

# #     seat_number = random.randint(1, 40)
# #     return (
# #         f"Booking confirmed!\n"
# #         f"Passenger: {name}\n"
# #         f"Bus: {bus['company']} ({bus['id']})\n"
# #         f"From: {bus['from']} To: {bus['to']}\n"
# #         f"Time: {bus['time']}\n"
# #         f"Seat No: {seat_number}\n"
# #         f"Price: {bus['price']} TZS\n"
# #     )
# # def cancel_booking(data: dict) -> str:
# #     """Simulate cancelling a bus booking."""
# #     booking_id = data.get("booking_id")
# #     # In a real application, you would check if the booking ID exists
# #     return f"Booking with ID {booking_id} has been successfully cancelled."



# import random
# from datetime import datetime, timedelta

# # Store bookings in memory
# BOOKINGS = {}

# def generate_buses(from_city: str, to_city: str, n: int = 4) -> list:
#     """Generate n random buses for any route."""
#     companies = ["Shabiby", "Kiliman", "ABC", "Mwakyusa Express", "Super Feo", 
#                  "BM Luxury", "Dar Express", "Safari Line", "Princess Muro", "Green Star"]
    
#     buses = []
#     for i in range(n):
#         bus_id = f"{from_city[:2].upper()}{to_city[:2].upper()}{random.randint(100,999)}"
#         company = random.choice(companies)
#         # Generate a random time within next 12 hours
#         time = (datetime.now() + timedelta(hours=random.randint(1,12))).strftime("%I:%M %p")
#         price = random.randint(15000, 60000)
#         buses.append({
#             "id": bus_id,
#             "company": company,
#             "from": from_city,
#             "to": to_city,
#             "time": time,
#             "price": price
#         })
#     return buses

# # Store last searched buses to allow booking
# LAST_SEARCHED_BUSES = []

# def search_buses(query: dict) -> str:
#     """Search available buses dynamically based on from/to city."""
#     global LAST_SEARCHED_BUSES
#     from_city = query.get("from")
#     to_city = query.get("to")

#     if not from_city or not to_city:
#         return "Please provide both departure and destination cities."

#     # Generate random bus options
#     results = generate_buses(from_city, to_city, n=random.randint(3,5))
#     LAST_SEARCHED_BUSES = results  # store for booking

#     output = f"Available buses from {from_city} to {to_city}:\n"
#     for bus in results:
#         output += f"- {bus['company']} ({bus['id']}): {bus['time']} @ {bus['price']} TZS\n"

#     return output.strip()

# def book_bus(data: dict) -> str:
#     """Book a bus seat from last searched buses."""
#     bus_id = data.get("bus_id")
#     name = data.get("name", "Passenger")

#     global LAST_SEARCHED_BUSES
#     bus = next((b for b in LAST_SEARCHED_BUSES if b["id"] == bus_id), None)
#     if not bus:
#         return f"Bus with ID {bus_id} not found. Make sure you searched first."

#     # Simulate seat booking
#     seat_number = random.randint(1, 40)
#     BOOKINGS[bus_id] = {"passenger": name, "seat": seat_number, "bus": bus}

#     return (
#         f"Booking confirmed!\n"
#         f"Passenger: {name}\n"
#         f"Bus: {bus['company']} ({bus['id']})\n"
#         f"From: {bus['from']} To: {bus['to']}\n"
#         f"Time: {bus['time']}\n"
#         f"Seat No: {seat_number}\n"
#         f"Price: {bus['price']} TZS\n"
#     )

# def cancel_booking(data: dict) -> str:
#     """Cancel a previously booked bus."""
#     booking_id = data.get("booking_id")
#     if booking_id in BOOKINGS:
#         del BOOKINGS[booking_id]
#         return f"Booking with ID {booking_id} has been successfully cancelled."
#     return f"No booking found with ID {booking_id}."








































import random
from datetime import datetime, timedelta

# Store bookings
BOOKINGS = {}
LAST_SEARCHED_BUSES = []

def generate_buses(from_city: str, to_city: str, n: int = 4) -> list:
    """Generate n random buses for demo purposes (mock data)."""
    companies = [
        "Shabiby", "Kiliman", "ABC", "Mwakyusa Express", 
        "Super Feo", "BM Luxury", "Dar Express", 
        "Safari Line", "Princess Muro", "Green Star"
    ]
    
    buses = []
    for _ in range(n):
        bus_id = f"{from_city[:2].upper()}{to_city[:2].upper()}{random.randint(100,999)}"
        company = random.choice(companies)
        time = (datetime.now() + timedelta(hours=random.randint(1,12))).strftime("%I:%M %p")
        price = random.randint(15000, 60000)
        buses.append({
            "id": bus_id,
            "company": company,
            "from": from_city.title(),
            "to": to_city.title(),
            "time": time,
            "price": price
        })
    return buses

def search_buses(query: dict) -> str:
    """Search available buses based on route."""
    global LAST_SEARCHED_BUSES
    from_city = query.get("from")
    to_city = query.get("to")
    travel_date = query.get("date")

    if not from_city or not to_city:
        return "Please provide both departure and destination cities."

    results = generate_buses(from_city, to_city, n=random.randint(3,5))
    LAST_SEARCHED_BUSES = results

    output = f" Available buses from {from_city.title()} to {to_city.title()} on {travel_date}:\n"
    for bus in results:
        output += f"- {bus['company']} ({bus['id']}): {bus['time']} @ {bus['price']} TZS\n"

    return output.strip()

def book_bus(data: dict) -> str:
    """Book a bus seat from last searched buses."""
    bus_id = data.get("bus_id")
    passenger_name = data.get("name", "Passenger")
    phone_number = data.get("phone", "N/A")

    global LAST_SEARCHED_BUSES
    bus = next((b for b in LAST_SEARCHED_BUSES if b["id"] == bus_id), None)
    if not bus:
        return f"Bus with ID {bus_id} not found. Please search again."

    seat_number = random.randint(1, 40)
    BOOKINGS[bus_id] = {
        "passenger": passenger_name,
        "phone": phone_number,
        "seat": seat_number,
        "bus": bus
    }

    return (
        f" Booking Confirmed!\n"
        f"Passenger: {passenger_name}\n"
        f"Phone: {phone_number}\n"
        f"Bus: {bus['company']} ({bus['id']})\n"
        f"Route: {bus['from']} → {bus['to']}\n"
        f"Departure: {bus['time']}\n"
        f"Seat No: {seat_number}\n"
        f"Price: {bus['price']} TZS\n"
        f"Booking Ref: {bus_id}\n"
    )

def cancel_booking(data: dict) -> str:
    """Cancel a booking by booking ID."""
    booking_id = data.get("booking_id")
    if booking_id in BOOKINGS:
        del BOOKINGS[booking_id]
        return f" Booking with ID {booking_id} has been successfully cancelled."
    return f" No booking found with ID {booking_id}."
