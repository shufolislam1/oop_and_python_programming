from Menu import *
from Restaurent import *
from Users import *
from Order import Order

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
    restaurent = Restaurent('su canteen', 500, menu)

    # create employees
    manager = Manager('Sajjad booss', 122, 'kns@dev.com', 'eskaton', 200, 'july 2020', 'core')
    restaurent.add_employee('manager', manager)

    chef = Chef('Rakib baburchi', 221, 'rakib@hasan.com', 'faridpur', 100, 'mar 2021', 'cook', 'vat')
    restaurent.add_employee('chef', chef)

    waiter = Waiter('shufol kamla', 43221, 'shufol@nihal.com', 'dhanmondi', 50, 'april 2021', 'server')
    restaurent.add_employee('waiter', waiter)


    # show employees details
    restaurent.show_employee()


    # ---------------below whole process is, customer 1 placing an order-------------
    print()
    # create customer
    customer_2 = Customer('sakib khan', 4, 'sakib@khan.com', 'banani', 100000)

    # create order
    order_2 = Order(customer_2, [burger_1, drink_1])

    # place an order
    customer_2.place_order(order_2)

    # resturent er nijero hiseb rakhte hobe saradin e kotogula order hoise. tai restaurent e add_order korte hobe
    restaurent.add_order(order_2) 

    # --------------------ei porjonto-----------------------------------------


    # --------------now custtomer_1 paying for order_1-----------------------

    restaurent.recieve_payment(order_2, 600, customer_2)
    print('Revenue and balance after first customer ',restaurent.revenue, restaurent.balance)
    


    # ---------------below whole process is, customer 2 placing an order-------------
    print()
    # create customer
    customer_2 = Customer('sakib al hasan', 4, 'sakib@khan.com', 'banani', 100000)

    # create order
    order_2 = Order(customer_2, [burger_1, pizza_2, drink_1])

    # place an order
    customer_2.place_order(order_2)

    # resturent er nijero hiseb rakhte hobe saradin e kotogula order hoise. tai restaurent e add_order korte hobe
    restaurent.add_order(order_2) 

    # --------------------ei porjonto-----------------------------------------


    # --------------now customer_2 paying for order_2-----------------------

    restaurent.recieve_payment(order_2, 6000, customer_2)
    print('Revenue and balance after second customer ',restaurent.revenue, restaurent.balance)

    # pay rent
    print()
    restaurent.pay_expense(restaurent.rent, 'rent expense')
    print('after rent,', 'revenue:',restaurent.revenue, 'balance:', restaurent.balance, 'expense:', restaurent.expense)

    # pay salary
    print()
    restaurent.pay_salary(chef)
    print('after salary given to chef,', 'revenue:',restaurent.revenue, 'balance:', restaurent.balance, 'expense:', restaurent.expense)
# call the main
if __name__ == '__main__':
    main()