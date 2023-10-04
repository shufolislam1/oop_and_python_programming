class Bank:
    def __init__(
        self, main_balance, min_withdraw, max_withdraw, min_deposit, max_deposit
    ):
        self.main_balance = main_balance
        self.min_withdraw = min_withdraw
        self.min_deposit = min_deposit
        self.max_withdraw = max_withdraw
        self.max_deposit = max_deposit

    # def conditions(self, min_withdraw, max_withdraw, min_deposit, max_deposit):
    #     self.min_withdraw = min_withdraw
    #     self.min_deposit = min_deposit
    #     self.max_withdraw = max_withdraw
    #     self.max_deposit = max_deposit

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f"fokinni. minimum {self.min_withdraw} taka tulte hobe")
        elif amount > self.max_withdraw:
            print(f"sir apni borolok. maximum {self.max_withdraw} taka tulte parben")
        else:
            self.main_balance -= amount
            print(f"After withdrawing {amount}, your current main_balance is {self.main_balance}")

    def deposit(self, amount):
        if amount<self.min_deposit:
            print(f'vai apnake min {self.min_deposit} taka deposit korte hobe')
        elif amount>self.max_deposit:
            print(f'vai apni {self.max_deposit} takar besi ekbare rakhte parben na')
        else:
            self.main_balance += amount
            print(f"After deposit {amount}, your current main_balance is {self.main_balance}")


brack = Bank(50000,100,40000,500, 50000)
brack.withdraw(100000000)
brack.deposit(-10)

dbbl = Bank(10000,200,9000,100,50000)
dbbl.deposit(1000)
dbbl.withdraw(200)
print(dbbl.main_balance)