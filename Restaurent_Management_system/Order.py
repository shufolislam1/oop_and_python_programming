class Order:
    def __init__(self, customer, ordered_items) -> None:
        self.customer = customer
        self.items = ordered_items
        total = 0
        for item in ordered_items:
            total += item.price
        self.bill = total
