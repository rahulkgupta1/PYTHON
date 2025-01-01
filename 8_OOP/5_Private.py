class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")

print(acc1.acc_no) 
#print(acc1.__acc_pass) #__ private outsider not show
print(acc1.reset_pass())

#***********************

class person:
    __name = "anonymous"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()

p1 = person()

print(p1.__hello())
print(p1.welcome())