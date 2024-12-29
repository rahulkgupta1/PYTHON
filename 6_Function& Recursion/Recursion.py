#RECURSIVE function
def show(n):
    if(n == 0): # base case
        return
    print(n)
    show(n-1)
    print("END")

show(5) #5, 4 = n-1, 3 = n-2, 2 = n-3, 1


#factorial  N! = (N-1)! * N
#(N-1)! = (N-2)! * N-1
def fact(n):
    if(n == 1 or n == 0):
       return 1 
    return fact(n-1) * n

print(fact(6))
#*****************practice ***********

# def calc_sum(n):
#     if(n == 0):
#         return 0
   
#     return calc_sum(n-1) + n

# sum = calc_sum(10)
# print(sum)



def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "litchi", "apple", "banna"]

print_list(fruits)
    