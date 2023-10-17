import random

class Person:
    def __init__(self, name) -> None:
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject) -> None:
        super().__init__(name)
        self.subject = subject

    def teach(self):
        pass

    def __repr__(self) -> str:
        return f'{self.name} : {self.subject}'

    def take_exam(self, subject, students):
        for student in students:
            marks = random.randint(0,100)
            # Set marks for each student for given sub

class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.__id = None
        self.marks = {}
        self.grade = None
        self.classroom = classroom

    @property
    def id(self):
        return self
    
    @id.setter
    def id(self, value):
        self.__id = value 