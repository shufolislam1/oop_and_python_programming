# eikhane cart holo instance attribute. that means eita sobai access korte parbe na 
class Shop:
    def __init__(self, buyer_name):
        self.cart=[]
        self.buyer = buyer_name

    def add_to_cart(self, item):
        self.cart.append(item)

shufol = Shop('shufol')
shufol.add_to_cart('watch')
shufol.add_to_cart('sunglass')
print(shufol.cart)

nihal = Shop('nihal')
nihal.add_to_cart('juta')
nihal.add_to_cart('mari')
print(nihal.cart)

#   eikhane cart holo class instance. that means sobai access pabe. kind of global scope er moto

# class Shop:
#     cart=[]
#     def __init__(self):
#         pass
#     def add_to_cart(self, item):
#         self.cart.append(item)

# shufol = Shop()
# shufol.add_to_cart('watch')
# shufol.add_to_cart('sunglass')
# print(shufol.cart)

# nihal = Shop()
# nihal.add_to_cart('juta')
# nihal.add_to_cart('mari')
# print(nihal.cart)