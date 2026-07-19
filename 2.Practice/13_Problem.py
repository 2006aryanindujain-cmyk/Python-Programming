# Write a program to detect double space in a string.

name = "Aryan is a good  boy and  "
print(name.find("  "))
print(name.replace("  ", " "))
print(name)
# Strings are immutable which means that you cannot change them by running functions on them
