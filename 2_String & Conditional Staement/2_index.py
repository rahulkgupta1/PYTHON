str = "apna collage"
print(str[3])

#slicing
str = "apna collage"
print(str[5:12]) # starting 1 and ending 5 then count 4 tak [5:11]
print(str[5:]) #[5: len(str)]

print(str[-8:-1]) #[-8,-2]
print(str[-13:-8])

str2 = "i am from studying python from Apnacollege"
print(str2.endswith("ege")) # reteurn true if sttring ends with substr
print(str2.capitalize())
print(str2.replace("python","javascript"))
print(str2.find("o")) # 1st no. jo aata hei vo batata hei
print(str2.count("from"))
