class Student:

    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob
    def print(self):
        print("Name of student :", self.name, "ID of student:", self.id, "Date of birth:", self.dob)
