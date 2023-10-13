class Food:
    def __init__(self, food_name, price) -> None:
        self.name = food_name
        self.price = price

class Burger(Food):
    def __init__(self, food_name, price, meat, ingredients) -> None:
        self.meat = meat
        self.ingredients = ingredients
        super().__init__(food_name, price)

class Pizza(Food):
    def __init__(self, food_name, price, size, toppings) -> None:
        self.size = size
        self.toppings = toppings
        super().__init__(food_name, price)

class Drinks(Food):
    def __init__(self, food_name, price, isCold = True) -> None:
        self.isCold = isCold
        super().__init__(food_name, price)


# composition . "has a" relation, not "is a" relation
class Menu:
    def __init__(self) -> None:
        self.burgers = []
        self.pizzas = []
        self.drinks = []

    def add_menu_item(self, item_type, item):
        if item_type == 'burger':
            self.burgers.append(item)
        elif item_type =='pizza':
            self.pizzas.append(item)
        elif item_type == 'drinks':
            self.drinks.append(item)
    
    def remove_pizza(self, pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)
        
    def show_menu(self):
        for burger in self.burgers:
            print(f'Name: {burger.name} and price {burger.price}')
        
        for pizza in self.pizzas:
            print(f'Name: {pizza.name} and price {pizza.price}')

        for drink in self.drinks:
            print(f'Name: {drink.name} and price {drink.price}')

