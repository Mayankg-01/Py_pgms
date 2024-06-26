class Student:
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        print("adding new student in DB..")
    

s1 = Student("Mayank",80)
print(s1.name,s1.marks)

s2 = Student("Arjun",88)
print(s2.name,s2.marks)