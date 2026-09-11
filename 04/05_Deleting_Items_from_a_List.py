# del
l = [1, 2, 3, 4, 5]
print(l)
# del l
# print(l)   NameError: name 'l' is not defined
del l[-1]
print(l)
del l[1:3]
print(l)


# remove
l1 = [1, 2, 3, 4, 5]
l1.remove(5)
print(l1)


# pop
l2 = [1, 2, 3, 4, 5]
l2.pop(0)
print(l2)
l2.pop()
print(l2)


# clear
l3 = [1, 2, 3, 4, 5]
l3.clear()
print(l3)
