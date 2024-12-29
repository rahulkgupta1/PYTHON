cites = ["delhi", "mumbai", "noida", "pune", "chennai"]
heros = ["thor", "ironmen", "captain", "shaktiman"]

def print_len(list):
    print(len(list))

print_len(cites)
print_len(heros)

heros = ["thor", "ironmen", "captain", "shaktiman"]

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heros)
print()

#factourial revision
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)

n = 5

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact)

cal_fact(6)


# Q5
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(73)

# homework
num = int(input("enter the number: "))

def value (num):
    if(num % 2 == 0 ):
         print("string Even")
    else:
        print("string odd")

value(num)

    