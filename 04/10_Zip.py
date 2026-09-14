# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passsed itertor is paired together,
# and then the second item in each passed iterator are paired together.

# If the different iterators have different lengths, the iterator with the least items decide the length of the new iterator.

# Write a program to add items of 2 lists indexwise.
l1 = [1, 2, 3, 4]
l2 = [-1, -2, -3, -4]
print(zip(l1, l2))
print(list(zip(l1, l2)))
print([i + j for i, j in zip(l1, l2)])

l3 = [1, 2, print, type, input]
print(l3)


# Disadvantages of python :-
# 1. Slow.
# 2. Risky usage.
# 3. Eats up more memory.


# Lists are mutable.
a = [1, 2, 3]
b = a
print(a)
print(b)
a.append(4)
print(a)
print(b)
# a and b points to same memory location.
c = [1, 2, 3]
d = c.copy()
print(c)
print(d)
c.append(4)
print(c)
print(d)
