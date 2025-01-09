class Marks:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark
    
    def print(self):
        self.student.print()
        print("Course:", self.course.name, "Mark:", self.mark, "Credit:", self.course.credit)

