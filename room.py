class Room:
def __init__(self, room_type, room_number, price_per_night):
self.room_type = room_type self.room_number = room_number self.price_per_night = price_per_night self.availability = True
def check_availability(self): return self.availability
def reserve_room(self): if self.availability:
self.availability = False
print(f"Room {self.room_number} reserved.") else:
print(f"Room {self.room_number} is not available.")
