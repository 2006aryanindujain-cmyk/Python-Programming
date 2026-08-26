email = input("Enter email: ")
password = input("Enter password: ")
if email == "aryanjain@gmail.com" and password == "12345678":
    print("Login")
elif email != "aryanjain@gmail.com" and password == "12345678":
    print("Invalid email id")
    email = input("Enter email again: ")
    if email == "aryanjain@gmail.com":
        print("Login")
    else:
        print("Invalid email")
elif email == "aryanjain@gmail.com" and password != "12345678":
    print("Invalid password")
    password = input("Enter password again: ")
    if password == "12345678":
        print("Login")
    else:
        print("Incorrect password")
else:
    print("Invalid email id and password")
    email = input("Enter email again: ")
    password = input("Enter password again: ")
    if email == "aryanjain@gmail.com" and password == "12345678":
        print("Login")
    else:
        print("Login restricted")


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a < b:
#     if a < c:
#         print(a, "is smallest number")
#     else:
#         print(c, "is smallest number")
# else:
#     if b < c:
#         print(b, "is smallest number")
#     else:
#         print(c, "is smallest number")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a == b == c:
    print("All three number are equal")
elif a < b and a < c:
    print(a, "is smallest number")
elif b < c:
    print(b, "is smallest number")
else:
    print(c, "is smallest number")


print(
    "This calculator can do addition, subtraction, multiplication, divison, integer divison, modulous operation."
)
print("Which operation you want to perform?")
op = input("Enter the operator: ")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if op == "+":
    print("Addition of given two numbers is:", a + b)
elif op == "-":
    print("Subtraction of given two numbers is:", a - b)
elif op == "*":
    print("Multiplication of two given numbers is:", a * b)
elif op == "/":
    print("Divison of two given numbers is:", a / b)
elif op == "//":
    print("Integer division number of two given numbers is:", a // b)
elif op == "%":
    print("Modulous of two given numbers is:", a % b)
else:
    print("Invalid choice")
