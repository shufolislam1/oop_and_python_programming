# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Intermediate class inheriting from Animal
class Mammal(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound

    def ap(self):  #eikhane ajaira nam disi ejonno je nam jekono kisu hote pare but method thaktei hobe. jehetu animal e ache
        return f"{self.name} says {self.sound}"

# Derived class inheriting from Mammal
class Dog(Mammal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof!")
        self.breed = breed

    def shu(self):  #eikhane ajaira nam disi ejonno je nam jekono kisu hote pare but method thaktei hobe. jehetu animal e ache
        return f"{self.name} is a {self.breed} dog."


# Creating objects
my_dog = Dog("Buddy", "Golden Retriever")

# Using methods
print(my_dog.shu())  # Output: Buddy is a Golden Retriever dog.
print(my_dog.ap())     # Output: Buddy says Woof!



"""

The Dog class indirectly inherits from the Animal class through the Mammal class.

Here's the inheritance hierarchy:

1. Animal is the base class.
2. Mammal is an intermediate class that inherits from Animal.
3. Dog is the derived class that inherits from Mammal.

So, even though Dog doesn't directly inherit from Animal, it inherits the characteristics of Animal through the chain of inheritance: Animal -> Mammal -> Dog.

In other words, any attributes or methods defined in the Animal class are part of the inheritance hierarchy and can be accessed through the Dog class, thanks to the intermediate class Mammal.

"""