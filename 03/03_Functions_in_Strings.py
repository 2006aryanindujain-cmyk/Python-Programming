# Strings in Python are immutable; any string method that returns a string will always generate
# and return a brand-new string object without modifying the original.

# Common string functions
print(len("Hello World"))
print(max("Hello World"))
print(min("Hello World"))
print(sorted("Hello World"))
print(sorted("Hello World", reverse=True))


# capitalize / title / upper / lower / swapcase
s = "hello world"
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())
print("Hello World".swapcase())


# count / find / index
h = "My name is Aryan Jain"
print("My name is Aryan Jain".count("i"))
print(h.count("i"))
print(h.count("x"))
print("My name is Aryan Jain".find("is"))
print(h.find("is"))
print(h.find("god"))
print("My name is Aryan Jain".index("is"))
print(h.index("is"))
# print(h.index("god"))    ValueError: substring not found


# endswith / startswith
print("My name is Aryan".endswith("yan"))
print("My name is Aryan".endswith("nay"))
print("My name is Aryan".startswith("My"))
print("My name is Aryan".startswith("yan"))


# format
name = "Aryan"
gender = "male"
print("Hi my name is {} and I am {}.".format(name, gender))
print("Hi my name is {1} and I am {0}.".format(gender, name))


# isalnum / isalpha / isdigit / isidentifier
print("Aryan123".isalnum())
print("Aryan".isalnum())
print("123".isalnum())
print("Aryan@123".isalnum())
print("Aryan".isalpha())
print("Aryan123".isalpha())
print("Aryan123".isdigit())
print("123".isdigit())
print("1name".isidentifier())
print("name1".isidentifier())


# Split / Join
print("hi my name is Aryan".split())
print("hi my name is Aryan".split("i"))
print(" ".join(["hi", "my", "name", "is", "Aryan"]))
print("-".join(["hi", "my", "name", "is", "Aryan"]))


# Replace
print("hi my name is Aryan".replace("Aryan", "Aadi"))
print("hi my name is Aryan".replace("Aryan123", "Aadi"))


# Strip
print("Aryan                         ".strip())
