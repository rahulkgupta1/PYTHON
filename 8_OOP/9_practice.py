class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

c1 = circle(21)
print(c1.area())
print(c1.perimeter()) 

#************
class Employes:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept = ", self.dept)
        print("salary =", self.salary)

class Engineer(Employes):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")



engg1 = Engineer("Elon Musk", 48)
engg1.showDetails()
#**************************************

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price

odr1 = Order("chips", 20)
odr2 = Order("tea", 15)

print(odr1 > odr2)
