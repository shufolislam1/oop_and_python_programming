class Calculator:
    brand = 'casio'
    model = 'fs990'

    def add(self, num1, num2):
        return num1+num2
    
    def sub(self, num1, num2):
        return num1-num2
    
    def mul(self, num1, num2):
        return num1*num2
    
    def div(self, num1, num2):
        return num1/num2
    
my_calc = Calculator()

first = my_calc.add(5,6)
second = my_calc.sub(5,6)
third = my_calc.mul(5,6)
fourth = my_calc.div(5,6)

print(first, second, third, fourth)