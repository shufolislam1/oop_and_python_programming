from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name) -> None:
        self.name = name

class Customer(User):
    def __init__(self, name,money) -> None:
        self.wallet = money
        # here __order is a private attribute which can not be accessed without getter
        self.__order = None
        super().__init__(name)

    #This is getter 
    @property
    def order(self):
        return self.__order
    
    # This is setter
    @order.setter
    def order(self, new_order):
        self.__order = new_order  #setting the value of private attribute "__order", via setter

    # setter er maddhome to ekbar order set/place korrlam. abar arekta method keno?
    def place_order(self, order):
        self.order = order
        print(f'Person named {self.name} placed and order {self.items}')

    def consume_food(self, order):
        print(f'{self.name} item food {self.items}')

    def pay_for_order(self, amount):
        pass
    def give_tips(self, tips_amount):
        pass
    def write_reviews(self, stars):
        pass

