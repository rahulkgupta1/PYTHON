# class and Instance Attributes
class Student:
    collage_name = "ABC Collage"
    name = "anonymous" #class attr
    
    #parameterized constructor
    def __init__(self, name, marks):
        self.name = name #obj attr> class attr
        self.marks = marks
        print("adding new student in Database..")

s1 = Student("karan", 97)
print(s1.name, s1.marks)
print(s1.collage_name)

