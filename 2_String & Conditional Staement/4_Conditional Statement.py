# light = "yellow"

# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("look")
# else:
#     print("light is broken")

# num = 5

# if(num > 2):
#     print("greater than 2")
# elif(num > 3):
#     print("greater than 3")

# age = 24

# if(age >-18 ):
#     print("can vote") # 4  space INDENTATION ids very important
# else:
#     print("CANNOT VOTE")

#grade bsed question

marks = int(input("enter the studend marks : "))

if(marks >= 90):
    grade = 'A'
elif(marks>= 80 and marks<90):
    grade = 'B'
elif(marks >= 70 and marks < 80):
    grade = 'C'
else:
    grade = 'D'

print("grade of sudent: ", grade)
