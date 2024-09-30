class Payment:
def __init__(self, payment_id, amount, payment_type):
self.payment_id = payment_id self.amount = amount self.payment_type = payment_type self.payment_status = "Pending"
def process_payment(self):
self.payment_status = "Completed"
print(f"Payment {self.payment_id} of {self.amount} has been processed.")
def refund_payment(self):
self.payment_status = "Refunded"
print(f"Payment {self.payment_id} has been refunded.")
