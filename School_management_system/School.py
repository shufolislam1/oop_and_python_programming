class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        # composition
        self.classrooms = {}

    def add_classrom(self, classroom):
        self.classrooms[classroom.name] = classroom

    
    def add_teacher(self, teacher, subject):
        if subject in self.teachers:
            self.teachers[subject] = teacher
    
    def student_admission(self, student):
        className = student.classroom.name
        if className in self.classrooms:
            self.classrooms[className].add_student(student)
        else:
            print(f'No classroom named {className} ')

    def __repr__(self) -> str:
        print('----------All Classrooms----------')
        for key, val in self.classrooms.items():
            print(key)

        print('----------All Students----------')
        eight = self.classrooms['eight']
        # print(len(eight.students))
        for student in eight.students:
            print(student.name)


        return ''
    

class Classroom:
    def __init__(self, name) -> None:
        self.name = name
        # composition
        self.students = []
        self.subject = []


    def add_student(self, student):
        serial_id = f'{self.name}-{len(self.students)+1}'
        student.id = serial_id
        self.students.append(student)

    def __str__(self) -> str:
        return f'{self.name}-{len(self.students)+1}'
    
    # TODO: get top students by sorting
    def get_top_students(self):
        pass