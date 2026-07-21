# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
# use key as their names. Assume that the names are unique.

d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})


print(d)


# If the names of 2 friends are same,then, the values entered later will be updated.
# If languages of two friends are same, then, nothing will happen. The values can be same.
