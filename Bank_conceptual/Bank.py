from abc import ABC, abstractmethod

class Account(ABC):
    accounts = []

    def __init__(self, name, accountNumber, password, type) -> None:
        self.name = name
        self.accountNumber = accountNumber
        self.password = password
        self.type = type
        self.balance = 0

        Account.accounts.append(self)

    def deposit(self, amount):
        if amount>=0:
            self.balance += amount
        else:
            print('\nInvalid amount\n')

    def withdraw(self, amount):
        if amount>=0 and amount<=self.balance:
            self.balance -= amount
        else:
            print('\nInvalid amount\n')

    def updateInfo(self, name):
        self.name = name

    # method overloading (calling same method name but with different argument)
    def updateInfo(self, name, password):
        self.name = name
        self.password = password

    @abstractmethod
    def showInfo(self):
        pass

class SavingsAccount(Account):
    def __init__(self, name, accountNumber, password, interestRate) -> None:
        super().__init__(name, accountNumber, password, type='savings')
        self.iRate = interestRate

    def showInfo(self):
        print(f'\nAccount owner\' name is : {self.name}')
        print(f'\nAccount Number : {self.accountNumber}')
        print(f'\nAccount type : {self.type}')
        print(f'\nAccount balance : {self.balance}')


    def applyInterest(self):
        totalInterest = self.balance*(self.iRate/100)
        print(f'Applied interest of {totalInterest}')
        self.deposit(totalInterest)

class SpecialAccount(Account):
    def __init__(self, name, accountNumber, password, limit) -> None:
        super().__init__(name, accountNumber, password, type='special')
        self.limit = limit

# this is another method overloading which can do special withdraw
    def withdraw(self, amount):
        if amount>=0 and amount<= self.limit:
            self.balance -= amount
        else:
            print('\nInvalid amount\n')

    def showInfo(self):
        print(f'\nAccount owner\' name is : {self.name}')
        print(f'\nAccount Number : {self.accountNumber}')
        print(f'\nAccount type : {self.type}')
        print(f'\nAccount balance : {self.balance}')

currentUser = None

while(True):
    if currentUser == None:
        print('\nNo User Logged in !\n')
        choice = input('\nLogin or Register? (L/R)')

        if choice == 'R':
            pass