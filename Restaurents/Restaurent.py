class Restaurent:
    def __init__(self, name, rent, menue = []) -> None:
        self.name = name
        self.chef = None
        self.waiter = None
        self.manager = None
        self.rent = rent
        self.menu = menue
        self.revenue = 0  #saradin e total_bikri. eikhane theke expense bad jabe na. revenue amount e kokhono hat dea jabe na. meeans revenue theke minus kora jabe na
        self.expense = 0  #saradin e total expense(salary, distributor soho bivinno lok der tk dewa)
        self.balance = 0  # balance = revenue - expense. revenue te jokhon tk add hobe tokhon balance ew tk add hobe. last e just expense ta minus korte hobe
        self.profit = 0

    def add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee

        elif employee_type == 'waiter':
            self.waiter = employee

        elif employee_type == 'manager':
            self.manager = employee
    
    def recieve_payment(self, order, amount, customer):
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
        
    def pay_expense(self, amount, description):
        # checking if expense amount is less than balance. mane balance er chey to ar expense amount dewa jabe na
        if amount < self.balance:
        # if self.balance > amount:
            self.expense += amount #koto expense holo seta hisab rakha
            self.balance -= amount #remaining balance koto thaklo ta hisab rakha
            print(f'Expense {amount} for {description}')

        else:
            print(f'Not enough money to pay {amount}')

    def pay_salary(self, employee):
        if employee.salary < self.balance:
            employee.recieve_salary()

    def show_employee(self):
        print()
        print('--------------Showing Employees------------')
        print()
        if self.chef is not None:
            print(f'Chef : {self.chef.name} with salary {self.chef.salary}')
        if self.manager is not None:
            print(f'manager : {self.manager.name} with salary {self.manager.salary}')
        if self.waiter is not None:
            print(f'waiter : {self.waiter.name} with salary {self.waiter.salary}')
