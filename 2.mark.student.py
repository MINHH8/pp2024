class Student:

    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob
    def print(self):
        print("Name of student :", self.name, "ID of student:", self.id, "Date of birth:", self.dob)

class Course:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.marks = {}
    def print(self):
        print("Name of course:", self.name, "ID of course:", self.id)        


def studentInfo(stdlst):
    n = int(input("Enter number of students: "))
    for i in range(n):
        print(f"Information of student {i+1}: ")
        student_id= input("ID of student: ")
        student_name= input("Name of student: ")
        student_Dob= input ("Date of birth: ")
        student =Student(student_name, student_id, student_Dob)
        stdlst.append(student)

def courseInfo(cslst):
    n1= int(input("Enter number of courses:"))
    for i in range(n1):
        print(f"Information of Course {i+1}: ")
        course_id= input("ID of course: ")
        course_name= input("Name of course: ")
        course =Course(course_name, course_id)
        cslst.append(course)

def std_list(stdlst):
    for student in stdlst:
        student.print()

def course_list(cslst):
    for course in cslst:
        course.print()


class marks(Student, Course):
    def __init__(self, name,id,dob,course,mark):
        super().__init__(name, id, dob)
        self.course = course
        self.mark = mark        
    def print(self):
        super().print()
        print("Course:", self.course.name, "Mark:", self.mark)


def mark_info(stdlst, cslst):
    course_id = input("Enter course ID: ")
    course = next((c for c in cslst if c.id == course_id), None)
    if course is None:
        print("Course not found")
        return

    for student in stdlst:
        mark = input(f"Enter mark for student {student.name} [{student.id}]: ")
        course.marks[student.id] = mark
        Marks = marks(student.name, student.id, student.dob, course, mark)
        Marks.print()

if __name__ == "__main__":
    stdlst = []
    cslst = []
while True:
        Opt = int(
            input("""
        [Student mark management]
        1. Add student information
        2. Add course information
        3. List of students
        4. List of courses
        5. add mark
        6. Exit
        Opt:
        """
        )
        )
                
        if Opt == 1:
            studentInfo(stdlst)
        elif Opt == 2:
            courseInfo(cslst)
        elif Opt == 3:       
            std_list(stdlst)    
        elif Opt== 4:
            course_list(cslst)
        elif Opt == 5:
            mark_info(stdlst, cslst)
        elif Opt == 6:
            break