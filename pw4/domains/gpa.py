import numpy as np
gpa_list=[]
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
