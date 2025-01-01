class Course:
    def __init__(self, name, id,credit):
        self.name = name
        self.id = id
        self.credit =credit
        self.marks = {}
    def print(self):
        print("Name of course:", self.name, "ID of course:", self.id, "Credit of course:", self.credit)        
