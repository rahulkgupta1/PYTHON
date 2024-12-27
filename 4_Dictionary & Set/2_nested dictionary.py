student = {
    "name" : "rahul kumar",
    "subject" : {
        "phy" : 97,
        "chem": 98,
        "math": 95,
    }
}

#nested dictionary

# print(student)
# print(student.keys())
# print(list(student.keys()))
# print(student.values())
# print(student.items())

print(student["name"]) #error
# error me nichei ka other code worknahi kaga so get use kare ge
print(student.get("name2")) #no error -> None

student.update({"city" : "delhi"})
print(student)

new_dict = {"name" : "neha kumar", "age": 16}
student.update(new_dict)
print(student)

