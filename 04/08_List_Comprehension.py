# List comprehension provides a concise way of creating lists.
# newlist=[expression for item in iterable if condition == True]

# Advantages of list comprehension :-
# 1. More time-efficient and space-efficient than loops.
# 2. Required fewer lines of code.
# 3. Transforms iterative statement into a formula.

# Add 1 to 10 numbers to a list.
l1 = [i for i in range(1, 11)]
print(l1)


# Scalar multiplication on a vector.
v = [2, 3, 4]
s = -3
print([s * i for i in v])


# Add squares.
l2 = 1, 2, 3, 4, 5
l3 = [i**2 for i in l2]
print(l3)


# Print all numbers divisible by 5 in the range of 1 to 50.
l4 = [i for i in range(1, 51) if i % 5 == 0]
print(l4)


# Find languages which starts with letter p.
languages = ["java", "python", "php", "c", "javascript"]
print([language for language in languages if language.startswith("p")])


# Add new list from my_fruits and item if the fruit exists in basket and also starts with 'a'.
basket = ["apple", "guava", "cherry", "banana"]
my_fruits = ["apple", "kiwi", "grape", "banana"]
print([fruit for fruit in my_fruits if fruit in basket if fruit.startswith("a")])


# Print a (3,3) matrix using list comprehension.
print([[i * j for i in range(1, 4)] for j in range(1, 4)])


# Cartesian Products.
p = [1, 2, 3, 4]
q = [5, 6, 7, 8]
print([i * j for i in p for j in q])
