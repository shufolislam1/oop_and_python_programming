from Menu import *
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


# call the main
if __name__ == '__main__':
    main()