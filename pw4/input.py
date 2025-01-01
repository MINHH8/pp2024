from domains import Student,Course,Marks
import math
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
        course_credit= int(input("Credit of course: "))
        course =Course(course_name, course_id, course_credit)
        cslst.append(course)

def mark_info( cslst,stdlst, mrk_list):
    course_id = input("Enter course ID: ")
    course = next((c for c in cslst if c.id == course_id), None)
    if course is None:
        print("Course not found")
        return
    for student in stdlst:
        mark = float(input(f"Enter mark for student {student.name} [{student.id}]: "))
        mark_round= math.floor(mark*10)/10
        course.marks[student.id] = mark_round
        marks = Marks(student, course,mark_round )
        mrk_list.append(marks)

def mark_list(mrk_list):
        for mark in mrk_list:

            mark.print()


def std_list(stdlst):
    for student in stdlst:
        student.print()

def course_list(cslst):
    for course in cslst:
        course.print()