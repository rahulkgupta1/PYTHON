# i = 1
# while i <= 100:
#       print("Hello"),
#       i+= 1

# i = 100
# while i>= 1:
#     print(i)
#     i-= 1

# n = 1
# a = int(input("enter the number: "))
# while n<= 10:
#     print("table of no. : ", a*n)
#     n += 1

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print(nums[0])
# print(nums[1])
# print(nums[2]) #so on

# i = 0
# while i<= len(nums):
#      print(nums[i])
#      i+= 1

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x= 36

i = 0
while i< len(nums):
    if(nums[i] == x):
        print("FOUND AT IDX", i)
        break
    else:    
        print("finding..")
    i+= 1
