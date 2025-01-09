from domains import Student,Course,Marks
import math
import os
from zipfile import ZipFile


def studentInfo(stdlst):
    n = int(input("Enter number of students: "))
    with open('D:\\minh\python\pw5\student_infor.txt', 'w') as f:
        for i in range(n):
            print(f"Information of student {i+1}: ")
            student_id= input("ID of student: ")
            student_name= input("Name of student: ")
            student_Dob= input ("Date of birth: ")
            student =Student(student_name, student_id, student_Dob)
            stdlst.append(student)
            f.write(f"ID: {student.id}, Name: {student.name}, Date of Birth: {student.dob}\n")



def courseInfo(cslst):
    n1= int(input("Enter number of courses:"))
    with open('D:\\minh\python\pw5\course_infor.txt', 'w') as f1:
        for i in range(n1):
            print(f"Information of Course {i+1}: ")
            course_id= input("ID of course: ")
            course_name= input("Name of course: ")
            course_credit= int(input("Credit of course: "))
            course =Course(course_name, course_id, course_credit)
            cslst.append(course)
            f1.write(f"ID: {course.id}, Name: {course.name}, Credit: {course.credit}\n")

def mark_info( cslst,stdlst, mrk_list):
    course_id = input("Enter course ID: ")
    course = next((c for c in cslst if c.id == course_id), None)
    if course is None:
        print("Course not found")
        return
    with open('D:\\minh\python\pw5\mark_infor.txt', 'a+') as f2:
        for student in stdlst:
                mark = float(input(f"Enter mark for student {student.name} [{student.id}]: "))
                mark_round= math.floor(mark*10)/10
                course.marks[student.id] = mark_round
                marks = Marks(student, course,mark_round )
                mrk_list.append(marks)
                f2.write(f"ID course:{marks.course.id}, Id student:{marks.student.id}, Mark: {marks.mark}\n")


def mark_list(mrk_list):
        for mark in mrk_list:
            mark.print()


def std_list(stdlst):
    for student in stdlst:
        student.print()

def course_list(cslst):
    for course in cslst:
        course.print()


# Danh sách các file .txt cần ghép
text_files = [
    'D:\\minh\python\pw5\student_infor.txt',  
    'D:\\minh\python\pw5\mark_infor.txt',  
    'D:\\minh\python\pw5\course_infor.txt'   
]

# Tên file chứa nội dung đã ghép
merged_filename = 'D:\\minh\python\pw5\merged_file'
# Tên file zip sẽ được tạo
zip_filename = 'D:\\minh\python\pw5\student.dat.zip'
with open(merged_filename, 'w') as merged_file:

    for file_path in text_files:
        with open(file_path, 'r') as f:
            content = f.read()
            merged_file.write(f"{os.path.basename(file_path)}\n")
            merged_file.write(content + "\n\n")

#  Nén file mới vào zip
with ZipFile(zip_filename,  'w+') as zip_file:
    zip_file.write(merged_filename)
    zip_file.close() # giải phóng tài nguyên, ngăn ngừa lỗi, tính toàn vẹn dữ liệu

