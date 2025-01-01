#oops pillers  3rd types
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)

print(car1.start())
print(car1.color)

#3 types of inheritance
#single ,multi-level, Multiple inheritance

class Car: # Multi-level inheritance 
   
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, Type):
        self.Type = Type

car1 = Fortuner("diesel")
car1.start()

#Multiples inheritance
class A:
    varA ="welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class c"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

#super() is sei hum parent class ka use kar sakte hei

class Car:
    def __init__(self, Type):
        self.Type = Type 
   
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("prius", "electric")
print(car1.Type)

#static method ,class method
class person:
    name = "anonymous"

    # def changeName(self, name):
    #    person.name = name
  
    # def changeName(self, name):
    #     self.__class__.name = "rahul"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = person()
p1.changeName("rahul kumar")
print(p1.name)
print(person.name)