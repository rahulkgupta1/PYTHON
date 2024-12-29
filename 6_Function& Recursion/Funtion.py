# a = 1
# b = 2

# sum = a + b
# print(sum)


# #more lines of code 

# a = 10
# b = 22

# sum = a + b
# print(sum)

# #more lines of code 

# a = 12
# b = 6

# sum = a + b
# print(sum)

# baar baarsame code ko ek baar likh do usii ko function kahte hei

def cal_sum(a, b): # parameters
    sum = a + b
    print(sum)
    return sum 
cal_sum(2,10) # call function, argument
cal_sum(12,17) # direct kam code me sahi way me punara like bad programmer
  
def print_hello():
    print("hello")

print(print_hello())
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()

# average of 3 numbers

def calc_avg(a, b, c):
    sum = a + b + c 
    avg = sum/3
    print(avg)
    return avg

calc_avg(98, 97, 95)

#*********print function
#print("apnacollage", "Rahul kumar gupta") # sep = " "
#print("apnacollage") # sep = " "
#print("Raul kumar gupta") #end = "\n"

print("apnacollage",end=" ") 
print("Raul kumar gupta") 

# defoult para meter 
# def cal_prod(a=1, b=1):
#     print(a*b)
#     return a * b

# cal_prod() 
def cal_prod(a, b=1):
    print(a*b)
    return a * b

cal_prod(1) # 1 
 
