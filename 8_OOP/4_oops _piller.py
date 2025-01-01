#4 piller Abstraction, Encapsulation, 
 # Abraction => Hiding the Implementation details of a class and only showing the essential feaures to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluch = False

    def start(self):
        self.cluch = True
        self.acc = True
        print("car started..")

car1 = Car()
car1.start()

#Encapsulation => Wrapping data and functions into a single units(object)


#*********Practice**********

class account:

    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    
    def debit(self, amount):
        self.balance -= amount
        print("RS", amount, "was debit")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("RS", amount, "was credit")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance    



acc1 = account(10000, 12345)
acc1.debit(1000)
acc1.credit(2000)
acc1.credit(40000)
acc1.debit(1000)


# del ketword
class student:
    def __init__(self, name):
        self.name = name

s1 = student("shradha" )
print(s1.name)
del s1.name
print(s1.name)
