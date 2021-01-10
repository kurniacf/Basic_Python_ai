a = input("enter number: ")
b = input("enter number: ")

# check conditions
# ==, !=, >, <, >=, <=, AND, OR, NOT
# in C/C++ --> &&, ||, ``

if (b > a):
    print("b is greater than a")
elif(a > b):
    print("a is greater than b")
else:
    print("a and b are equal")

c = input("enter number: ")
# check conditions
if(a < b) or (c < a):
    print("Kondisi benar")
elif(a < b) and (a > c):
    print("A greater than B and C")
elif not (a != b and a != c and b != c):
    print("ABC is same")
