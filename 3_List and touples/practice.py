# a = input("name he favourte movies: ")
# b = input("name he favourte movies: ")
# c = input("name he favourte movies: ")
# list = [a, b, c]
# print(list)


list = [1, 2, 3]
list1 = [1, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not pelidrome")  