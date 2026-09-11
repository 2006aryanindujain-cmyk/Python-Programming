# List is a data type where you can store multiple items under 1 name. More technically, lists act
# like dynamic arrays which means you can add more items on the fly.

# L=[20, 'Jessa', 35.75, [30, 60, 90]]

# Arrays v/s lists :-
# -> Fixed v/s dynamic size.
# -> Speed of execution is less in list compared to array.
# -> Convenience => heterogeneous.
# -> List occupy more memory than array.

# l = [1, 2, 3]
# print(id(l))
# print(id(l[0]))
# print(id(l[1]))
# print(id(l[2]))
# print(id(1))
# print(id(2))
# print(id(3))
# The built-in function id() is used to retrieve the unique memory address (identity) of an object,
# which these operators internally compare.
# id(): A function that returns an integer representing an object's unique memory address.
# Python lists can store items of different data types because they are heterogeneous by default
# and internally implemented as an array of pointers (references).

# Characteristics :-
# 1. Ordered.
# 2. Changable/Mutable.
# 3. Heterogeneous.
# 4. Can have duplicates.
# 5. Are dynamic.
# 6. Can be nested.
# 7. Items can be accessed.
# 8. Can contain any kind of objects in python.

# l1 = [1, 2, 3]
# l2 = [3, 2, 1]
# print(l1 == l2)
# print(l1[0])

# Creating a list :-

# 1. Empty :-
print([])

# 2.1D :-
print([1, 2, 3, 4, 5])  # Homogeneous

# 3.2D :-
print([1, 2, 3, [4, 5]])  # Homogeneous

# 4.3D :-
print([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # Homogeneous

# 5. Heterogeneous :-
print([1, True, 5.6, 5 + 6j, "Hello"])

# 6. Using Type Conversion :-
print(list("Hello"))
