from School import School, Classroom
from Persons import Student

def main():
    # create brand new school
    school_1 = School('singuria', 'Tangail')

    # create classrooms and append them in school 
    eight = Classroom('eight')
    school_1.add_classrom(eight)

    nine = Classroom('nine')
    school_1.add_classrom(nine)

    ten = Classroom('ten')
    school_1.add_classrom(ten)


    # create student and add students in classroom through student_admission
    nihal = Student('nihal', eight)
    school_1.student_admission(nihal)

    shakib = Student('shakib', eight)
    school_1.student_admission(shakib)

    rakib = Student('rakib', eight)
    school_1.student_admission(rakib)

    sajjad = Student('sajjad', eight)
    school_1.student_admission(sajjad)

    
    print(school_1)
if __name__ == '__main__':
    main()