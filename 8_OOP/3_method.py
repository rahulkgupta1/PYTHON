# class Student:
#     collage_name = "ABC Collage"
    
#     def __init__(self, name, marks):
#         self.name = name 
#         self.marks = marks

#     def welcome(self):
#         print("welcome student", self.name)

#     def get_marks(self):
#         return self.marks


# s1 = Student("karan", 97)
# s1.welcome()
# print(s1.get_marks())


#********practice***************

# class student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
       
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#             print("hi", self.name, "your avg score is:", sum/3)

    
# s1 = student("karan", [99, 98, 97])
# s1.get_avg()
# s1.name = "Rahul"
# s1.get_avg()

# **********statics methods****** don't use self parameter (at class level)

class student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod 
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
            print("hi", self.name, "your avg score is:", sum/3)

    
s1 = student("karan", [99, 98, 97])
s1.get_avg()
s1.hello()

#*********corect way to get  1 out put ******
#class student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
       
#     def get_avg(self):
#         total = sum(self.marks)
#         avg = total/3
#         print("hi", self.name, "your avg score is:", avg)

    
# s1 = student("karan", [99, 98, 97])
# s1.get_avg()****///
#output hi karan your avg score is: 98.0


