# polymorphism 4 pillers of oops
#operator overloading

print(1+3)#3
print("apna " + "collage") # concorate
print([1, 2, 3] + [4, 5, 6]) # merge\# all of this impicit overload already define hei

class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return complex(newReal, newImg)
    

num1 = complex(1,3)
num1.showNumber()     

num2 = complex(4,6)
num2.showNumber()
numm2 = num1 + num2
num2.showNumber()
# num3 = num1.add(num2) 
# num3.showNumber()

num3 = num1 - num2
num3.showNumber()
