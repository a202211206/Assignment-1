class Reservation:
def __init__(self, reservation_id, check_in_date, check_out_date, nights, rooms):
self.reservation_id = reservation_id self.check_in_date = check_in_date self.check_out_date = check_out_date self.nights = nights
self.rooms = rooms self.status = "Confirmed"
def make_reservation(self):
print(f"Reservation {self.reservation_id} has been made for {self.nights} nights.")
def cancel_reservation(self):
self.status = "Cancelled"
print(f"Reservation {self.reservation_id} has been cancelled.")
def confirm_reservation(self):
print(f"Reservation {self.reservation_id} is confirmed.")
def check_in(self):
if self.status == "Confirmed":
print(f"Check-in successful for reservation {self.reservation_id}") else:
print("Cannot check-in, reservation not confirmed.")
