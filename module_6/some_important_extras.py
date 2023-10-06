class Person:
    def __init__(self, name:str, age:int) -> None:
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")  #this is a way to check type of arguments which is important sometime
        self.name = name
        self.age = age

    def valoChele(self):
        raise NotImplementedError

class Shufol(Person):
    def __init__(self, name, age, weight) -> None:
        self.weight = weight
        super().__init__(name, age)

    def valoChele(self):  #this had to be created
        print("yes")

s1 = Person('shu',20)
print(s1.age)

# print(isinstance(s1,Person)) #True
# print(isinstance(s1,Shufol)) #True
# # print(issubclass(s1,Shufol)) #gives error. because s1 is not a class, it's an object/instance of shufol class
# print(issubclass(Shufol, Person)) #True

# s1.valoChele()  #this will raise an error if we don't create valoChele method in Shufol class. because it's parent classe's valoChele method want it annd if we don't it will arise a NotImplementedError