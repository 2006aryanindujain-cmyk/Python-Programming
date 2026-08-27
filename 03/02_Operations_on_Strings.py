# Arithmetic operations
print("New" + " " + "Delhi")
print("Delhi" * 5)


# Relational operations
print("delhi" == "delhi")
print("delhi" != "delhi")
print("delhi" > "mumbai")
print("delhi" < "mumbai")
print("delhi" >= "mumbai")
print("delhi" <= "mumbai")
# In Python, strings are compared lexicographically using the ASCII / Unicode numerical values of their characters, evaluated character-by-character from left to right.
print("mumbai" > "pune")
# 'A'–'Z' : 65 to 90
# 'a'–'z' : 97 to 122
# Uppercase letters always have smaller numerical values than lowercase letters
print("Pune" > "pune")


# Logical operations
print("Hello" and "World")
print("Hello" or "World")
print("" and "World")
print("" or "World")
print(not "")
print(not "Hello")


# Loops on strings
# String in python is iterable.
for i in "Hello":
    print(i)
for i in "Kanpur":
    print("Delhi")


# Membership operations
print("D" in "Delhi")
print("K" in "Kanpur")
print("D" not in "Kanpur")
print("K" not in "Delhi")
