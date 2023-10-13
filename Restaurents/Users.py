from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, phone_num, email, address) -> None:
        self.name = name
        self.phone_num =phone_num
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, phone_num, email, address,  name, money) -> None:
        self.wallet = money
        # here __order is a private attribute which can not be accessed without getter
        self.__order = None
        super().__init__(name, phone_num, email, address)

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

class Employee(User):
    def __init__(self, name, phone_num, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone_num, email, address)
        self.salary = salary
        self.due = salary
        self.starting_date = starting_date
        self.department = department
    
    def recieve_salary(self):
        self.due = 0

class Chef(Employee):
    def __init__(self, name, phone_num, email, address, salary, starting_date, department, cooking_item) -> None:
        super().__init__(name, phone_num, email, address, salary, starting_date, department)
        self.cooking_item = cooking_item

class Waiter(Employee):
    def __init__(self, name, phone_num, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone_num, email, address, salary, starting_date, department)
        self.tips_earning = 0

    def take_order(self, order):
        pass

    def transfer_order_to_chef(self, order):
        pass

    def serve_food(self, order):
        pass

    def recieve_tips(self, amount):
        self.tips_earning += amount


class Manager(Employee):
    def __init__(self, name, phone_num, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone_num, email, address, salary, starting_date, department)
        