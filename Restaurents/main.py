from Menu import *
from Restaurent import *
from Users import *

def main():
    # create menu object
    menu = Menu()

    # add burger
    burger_1 = Burger('chicken Burger', 500, 'chicken', ['bread', 'chicken'])
    menu.add_menu_item('burger', burger_1)

    burger_2 = Burger('Beef Burger', 800, 'Beef', ['Beef', 'Bread'])
    menu.add_menu_item('burger', burger_2)

    # add pizza
    pizza_1 = Pizza('shutki Pizza', 1200, 'xl', ['shutki', 'onion'])
    menu.add_menu_item('pizza', pizza_1)

    pizza_2 = Pizza('Alu Pizza', 800, 'xxl', ['Alu', 'onion'])
    menu.add_menu_item('pizza', pizza_2)

    # add drinks
    drink_1 = Drinks('speed', 30, True)
    menu.add_menu_item('drinks', drink_1)

    drink_2 = Drinks('Drinko', 40, True)
    menu.add_menu_item('drinks', drink_2)

    # show menu items
    menu.show_menu()

    # create restaurent
    restaurent = Restaurent('su canteen', 1500, menu)

    # create employees
    manager = Manager('Sajjad booss', 122, 'kns@dev.com', 'eskaton', 2000, 'july 2020', 'core')
    restaurent.add_employee('manager', manager)

    chef = Chef('Rakib baburchi', 221, 'rakib@hasan.com', 'faridpur', 1000, 'mar 2021', 'cook', 'vat')
    restaurent.add_employee('chef', chef)

    waiter = Waiter('shufol kamla', 43221, 'shufol@nihal.com', 'dhanmondi', 500, 'april 2021', 'server')
    restaurent.add_employee('waiter', waiter)


    # show employees details
    restaurent.show_employee()

# call the main
if __name__ == '__main__':
    main()