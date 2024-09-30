class Guest:
    def __init__(self, guest_name, email, phone, payment_info):
        self.guest_name = guest_name
        self.email = email
        self.phone = phone
        self.payment_info = payment_info

    def view_reservation(self, reservation):
        print(f"Viewing reservation for {self.guest_name}: {reservation.reservation_id}, Status: {reservation.status}")

    def make_payment(self, amount):
        print(f"Payment of {amount} made by {self.guest_name}.")
