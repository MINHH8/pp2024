import math
import numpy as np
import curses

class Student:

    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob
    def print(self):
        print("Name of student :", self.name, "ID of student:", self.id, "Date of birth:", self.dob)

class Course:
    def __init__(self, name, id,credit):
        self.name = name
        self.id = id
        self.credit =credit
        self.marks = {}
    def print(self):
        print("Name of course:", self.name, "ID of course:", self.id, "Credit of course:", self.credit)        


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

def std_list(stdlst):
    for student in stdlst:
        student.print()

def course_list(cslst):
    for course in cslst:
        course.print()


class Marks:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark
    
    def print(self):
        self.student.print()
        print("Course:", self.course.name, "Mark:", self.mark, "Credit:", self.course.credit)


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


def calculate_gpa(marks_list, student_id):
    total_points = []
    total_credits = []
    

    for mark in marks_list:
        if mark.student.id == student_id:
            total_points.append(mark.mark * mark.course.credit)
            total_credits.append(mark.course.credit)

    if total_credits:
        total_points_array = np.array(total_points)
        total_credits_array = np.array(total_credits)
        gpa = float(total_points_array.sum() / total_credits_array.sum())
        print(f"Average GPA for student ID {student_id}: {gpa:.2f}")
        gpa_list.append(gpa)
    else:
        print(f"No credits available to calculate GPA for student ID {student_id}.")

def avg_gpa( stdlst,mrk_list):
    student_id = input("Enter student ID to calculate GPA: ")
    student_exists = any(student.id == student_id for student in stdlst)

    if not student_exists:
        print("Student not found.")
        return

    calculate_gpa(mrk_list, student_id)
def sort_GPA(gpa_list):
    n = len(gpa_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if gpa_list[j] < gpa_list[j+1]:
                gpa_list[j], gpa_list[j+1] = gpa_list[j+1], gpa_list[j]

def print_sorted_gpa(gpa_list):
    sort_GPA(gpa_list)
    print("Sorted GPA list:", gpa_list)


def main(stdscr):
    curses.start_color()  # Bắt đầu sử dụng màu
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.clear()
    stdscr.addstr(0, 0, "Hello, welcome to student system( Enter to continue)!", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)

if __name__ == "__main__":
    stdlst = []
    cslst = []
    mrk_list =[]
    gpa_list=[]
while True:
        Opt = int(
            input("""
        [Student mark management]
        1. Add student information
        2. Add course information
        3. List of students
        4. List of courses
        5. Add mark
        6. List mark
        7. GPA
        8. Sort GPA
        9. Exit
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
            mark_info( cslst,stdlst, mrk_list)
        elif Opt == 6:
            mark_list(mrk_list)
        elif Opt==7:
            avg_gpa(stdlst,mrk_list)
        elif Opt == 8:    
            print_sorted_gpa(gpa_list)
        elif Opt == 9:
            break