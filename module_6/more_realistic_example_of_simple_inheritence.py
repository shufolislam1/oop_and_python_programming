# eikhane ceicketer class e init ar eat method sob class er jonno samne.mane jara cricketer class ke inherit korbe arki


class Crickter:
    def __init__(self, name, country, age, jercyNum) -> None:
        self.name = name
        self.country = country
        self.age = age
        self.jercyNum = jercyNum

    def eat(self):
        print("only healthy foods")

class Shakib(Crickter):
    def __init__(self, name, country, age, jercyNum, DOB) -> None:
        self.DOB = DOB
        super().__init__(name, country, age, jercyNum)

    def pracTime(self):
        print("5 hours a day")

class Tamim(Crickter):
    def __init__(self, name, country, age, jercyNum, city) -> None:
        self.city = city
        super().__init__(name, country, age, jercyNum)
    
    def travel(self):
        print("5 days a month")

class Musi(Crickter):
    def __init__(self, name, country, age, jercyNum, weight):
        self.weight = weight
        super().__init__(name, country, age, jercyNum)



# Create instances of Shakib and Tamim
shakib = Shakib("Shakib Al Hasan", "Bangladesh", 34, 75, "March 24, 1987")
tamim = Tamim("Tamim Iqbal", "Bangladesh", 32, 28, "Chittagong")
mushi = Musi('mushi', 'bd', 35, 15, 58)

# Call the eat() method on instances of Shakib and Tamim
shakib.eat()  # This will print "only healthy foods"
tamim.eat()   # This will also print "only healthy foods"
mushi.eat()