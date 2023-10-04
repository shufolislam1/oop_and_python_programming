class Shopping:
    def __init__ (self, buyer_name):
        self.name = buyer_name
        self.cart = []

    def add_to_cart(self, item_name, price, quantity):
        # self.item_name = item_name
        # self.price = price
        # self.quantity = quantity
        products = {'item': item_name, 'price': price, 'quantity': quantity}
        self.cart.append(products)
    
    def checkout(self, recived_amount):
        pass

shufol = Shopping('shufol')
shufol.add_to_cart('alu',50,10)
shufol.add_to_cart('dim',12,12)
shufol.add_to_cart('dal',120,10)

print(shufol.cart)