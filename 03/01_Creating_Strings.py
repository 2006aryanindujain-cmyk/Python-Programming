# Strings are sequence of characters.
# In Python specifically, strings are a sequence of unicode characters.


# Creating Strings
s = "Hello"
print(s)
a = 'Hello'
print(a)
b = '''Hello'''
print(b)
c = str('Hello')
print(c)


# Accessing substrings from a string
# Positive indexing(starting with 0)
d = "Hello World"
print(d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8], d[9], d[10])
# print(d[11])    IndexError: string index out of range
# Negative indexing
print(d[-1], d[-2], d[-3], d[-4], d[-5], d[-6], d[-7], d[-8], d[-9], d[-10], d[-11])
# Slicing
print(d[0:5])
print(d[0:11:2])
print(d[11:0:-2])
print(d[::-1])


# Editing and Deleting in Strings
w = "Hello World"
# w[0] = "h"   TypeError: 'str' object does not support item assignment
# Python things are immuutable(cannot change after creation)
del w
# print(w)   NameError: name 'w' is not defined
x = "Hello World"
# del x[-1:-5:2]
# print(x)     TypeError: 'str' object does not support item deletion
