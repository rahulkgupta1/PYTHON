# nums = [1, 2,3,4,5]

# for val in nums:
#    print(val)  

# str = "apnacollage"

# for char in str:
#     if(char == 'o'):
#         print("O found")
#         break
#     print(char)
# print("END")

#**********practice***************#

# list = [1, 4, 9, 16, 25, 36, 49, 81, 100]
# obj = 0
# while obj <= len(list):
#     print(list[obj])
#     obj += 1
# for el in list: #for loop
#     print(el)

tup = (1, 4, 9, 16, 25, 36, 49, 81, 100, 4)
x = 4
idx= 0
for el in tup:
    if(el == x):
        print("FOUNDED and index is : ", idx)
        idx+=1
        
    else:
        print("NOT Founded")
print("end the loop")




