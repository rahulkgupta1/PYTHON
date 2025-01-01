a = 10
b = 20

sum = a+b
print(sum)
diff = a-b
print(diff)
                

# function kei bajah sei redundancycy decrese hoti hei and reusability increase
# meanss procedural(oneby one karke) sei functional programing me badh gaye  
# next step aab Object oriented programming

class student:
    name = "Rahul kumar"
    
s1 = student()
print(s1.name)

s2 = student()
print(s2.name)

class Car:
    color = "blue"
    brand = "Ody"

car1 = Car()
print(car1.color)
print(car1.brand)

#**********--init function

# class student:
#     def __init__(self):
#         print(self)
#         print("adding new student in database..")
#     name = "Rahul kumar"
    
# s1 = student()
# print(s1)


class student:
    def __init__(self, fullname):
        self.name = fullname      
        print("adding new student in database..")
    
# self ki madat sei different data ya variable ko store kar sakte hei   
s1 = student("karan")
print(s1.name) # karan

s2 = student("arjun")
print(s2.name)


#**********learning __int__ constructor

class Student:

    #default contructiors
    #def __init__(self):
    #    pass

    
    #parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")

s1 = Student("karan", 97)
print(s1.name, s1.marks)

s2 = Student("arjun", 87)
print(s2.name, s2.marks)