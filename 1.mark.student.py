def Input():
    n = int(input("Enter number of students: "))
    Student_list=[]
    for i in range(n):
        print(f"Information of student {i+1}: ")
        student_id= input("ID of student: ")
        student_name= input("Name of student: ")
        student_Dob= input ("Date of birth: ")
        students_info={"Student Name": student_name,"Student ID": student_id,"Date of birth": student_Dob}
        Student_list.append(students_info)
    print("\nList of Students:")
    for student in Student_list:
        print(student)

    n1= int(input("Enter number of courses:"))
    Course_list=[]
    for i in range(n1):
        print(f"Information of Course {i+1}: ")
        course_id= input("ID of course: ")
        course_name= input("Name of course: ")
        courses_info={"Course Name": course_name,"Course ID": course_id}
        Course_list.append(courses_info)
    print("\nList of Courses:")
    for index,value in enumerate(Course_list):
        print(f"{index+1}: {value['Course Name']} (ID: {value['Course ID']})")
    choice= int(input("Pick a course you want to see score: "))
    if 1<=choice <= len(Course_list):
        print("You selected:", Course_list[choice - 1])
    else:
        print("Enter again")
    print(f"Mark of student in course {choice}:")
    mark_list=[]
    for i in range(n):
        mark= int(input(f"Score of student {i+1}: "))
        mark_info= {"Student Name":  Student_list[i]['Student Name'], "mark": mark}
        mark_list.append(mark_info)
    return Student_list, Course_list, mark_list

def listing():
    Student_list, Course_list, mark_list = Input()
    print("\nFinal List of Students:")
    for student in Student_list:
        print(student)

    print("\nFinal List of Courses:")
    for course in Course_list:
        print(course)

    print("\nMarks of Students in course you selected:")
    for mark in mark_list:
        print(mark)

listing()