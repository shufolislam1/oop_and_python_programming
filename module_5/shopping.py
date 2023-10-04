class Shopping:
    def __init__(self, buyer_name):
        self.name = buyer_name
        self.cart = []

    def add_to_cart(self, item_name, price, quantity):
        # self.item_name = item_name
        # self.price = price
        # self.quantity = quantity
        products = {"item": item_name, "price": price, "quantity": quantity}
        self.cart.append(products)

    def checkout(self, recived_amount):
        total_bill = 0
        for items in self.cart:
            total_bill += items["price"] * items["quantity"]
        if total_bill > recived_amount:
            print(f"You need to give more {total_bill-recived_amount} taka")
        elif total_bill < recived_amount:
            print(f"Here's your change {recived_amount-total_bill} taka")

    def remove_from_cart(self, item):
        pass


shufol = Shopping("shufol")
shufol.add_to_cart("alu", 50, 10)
shufol.add_to_cart("dim", 12, 12)
shufol.add_to_cart("dal", 120, 10)

# print(shufol.cart)
shufol.checkout(5000)
