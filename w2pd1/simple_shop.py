class Product:
    def __init__(self, p_name, p_price, available = True) -> None:
        self.name = p_name
        self.price = p_price
        self.available = available

class Shop:
    def __init__(self) -> None:
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
        # this method add products using product class to the shop class

    def buy_product(self, p_name):
        for product in self.products:
            print(product)
            if product.name == p_name and product.available:
                # product.available  = False
                return 'congrats!sucesfull'
            return 'not available'
        
        # used to buy a product and check whether this product is available or not. If you successfully buy a product, then throw a Congress message.

p1 =  Product('alu', 100)
p2 =  Product('dim', 180)
p3 =  Product('dal', 200)

shop = Shop()

shop.add_product(p1)
shop.add_product(p2)
shop.add_product(p3)

# res1 = shop.buy_product('alu')
# res2 = shop.buy_product('dal')
# print(res1)
# print(res2)