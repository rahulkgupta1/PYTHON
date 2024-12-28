#print(range(5))

#for el in range(10): #range(stop) 
 #   print(el)

# for el in range(2,10): #range(start, stop) 
#     print(el)

# for el in range(2, 10, 2): #range(start, stop, step) 
#     print(el)


#range(start?,stop,step?)

#********practice***************//

# for el in range(1,101):
#     print(el)

# for el in range(100,0,-1):
#     print(el)

# x = int(input("enter the no. :"))
# for el in range(1, 11):
#     print(el*x)


#pass statement => pass is a null statement that does nothing. It is used as a placeholder for future code

for i in range(5):
    pass

if i>5:
    pass

print("some usefull work")
#*************practice *******

# n = 5

# sum = 0
# for i in range(1, n+1):
#     sum += i

# print("total sum =", sum)

n = 7
sum = 0
i = 1
while i <= n:
    sum+= i
    i+= 1
print("total sum =", sum)    

# factorial 
n = 7
fact = 1
i = 1
while i <= n:
    fact *= i
    i+= 1
print("factorial", fact)  

n = 3

fact = 1
for el in range(1,n+1):
    fact *= el
print("factoril :", fact)    



