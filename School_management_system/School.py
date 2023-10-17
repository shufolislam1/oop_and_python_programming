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
    
    def student_admission(self, student, classroom_name):
        if classroom_name in self.classrooms:
            self.classrooms[classroom_name].add_student(student)
        else:
            print(f'No classroom named {classroom_name} ')

class Classroom:
    def __init__(self, name) -> None:
        self.name = name
        # composition
        self.students = []

    def add_student(self, student):
        serial_id = f'{self.name}-{len(self.students)+1}'
        student.id = serial_id
        student.classroom = self.name
        self.students.append(student)

    def __str__(self) -> str:
        return f'{self.name}-{len(self.students)+1}'
    
    # TODO: get top students by sorting
    def get_top_students(self):
        pass