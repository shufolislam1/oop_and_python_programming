# encaptulation --> hide details.
# ekta capsul er vitor jemon gura gura ossudh hide kore, oirokom chinta kora jete pare
# access modifier: public(python e by default sob public), protected("_" die protected), private("__" die private) mean kore.

""" 
-----------------------------------------------------------------------
Encapsulation is about controlling access to an object's internal state
-----------------------------------------------------------------------
"""

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.balance = balance  # Public attribute

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount

    def get_account_number(self):
        return self.__account_number  # Private attribute accessed via a method

# Usage
account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(200)
print("Account Number:", account.get_account_number())  #class er vitorei arekta method er maddhome acccess kora jabe. jehetu "__account_number" private attribute

# print(account.__account_number)   #eivabe acccess kora jabe na. jehetu "__account_number" private attribute
print("Balance:", account.balance)

# In this example, the __account_number attribute is encapsulated within the BankAccount class, and it can only be accessed using the get_account_number method.