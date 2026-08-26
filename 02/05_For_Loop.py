for i in range(1, 11):
    print(i)


for i in range(1, 11, 2):
    print(i)


for i in range(10, 0, -1):
    print(i)


for i in "Kanpur":
    print(i)


# Python for loop can iterate over string, list, set, tuple, dictionary. In short, it can iterate over all data types in Python.


try:
    current_population = int(input("Enter the current population of a town:"))
    n = int(
        input(
            "Enter the number of years after which you want to know the population of a town:"
        )
    )
    p = float(input("Enter the population increasing rate per year(in %):"))
    if current_population < 0 or n < 0:
        print("Population and number of years cannot be negative")
    elif p < -100:
        print("Decline rate cannot be less than -100%.")
    else:
        for i in range(1, n + 1):
            current_population = current_population + ((p * current_population) / 100)
        print("Population of a town after", n, "years is", round(current_population))
except ValueError:
    print("Invalid input! Please enter valid numeric values.")


try:
    current_pop = int(input("Enter the current population of a town:"))
    y = int(input("Enter the number of years:"))
    per = float(input("Enter the population growth rate per year(in %):"))
    if current_pop < 0 or y < 0:
        print("Population and number of years cannot be negative")
    elif per <= -100:
        print("Decline rate cannot be less than -100%.")
    else:
        for i in range(y, 0, -1):
            print("Population in year", i, "is", round(current_pop))
            current_pop = (100 * current_pop) / (100 + per)
except ValueError:
    print("Invalid input! Please enter valid numeric values.")


# Sequence sum:- 1/1! + 2/2! + 3/3! + .....
import math

s = int(input("Enter the number"))
sum = 0
fact = 1
for i in range(1, n + 1):
    # sum = sum + (i / math.factorial(i))
    fact = fact * i
    sum = sum + (i / fact)
print("Sum is", sum)


for i in range(1, 5):
    for j in range(1, 5):
        print(i, j)


z = int(input("Enter the number of rows:"))
for i in range(1, z + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()


x = int(input("Enter the number of rows:"))
for i in range(1, x + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for k in range(i - 1, 0, -1):
        print(k, end="")
    print()


# break statement
for i in range(1, 10):
    if i == 5:
        break
    print(i)


# p = int(input("Enter the first number:"))
# q = int(input("Enter the second number:"))
# if p > q:
#     max = p
#     min = q
# else:
#     max = q
#     min = p
# for i in range(min, max + 1):
#     if i < 2:
#         continue
#     else:
#         count = 0
#         for j in range(2, int(i / 2) + 1):
#             if i % j == 0:
#                 count += 1
#                 break
#         if count == 0:
#             print(i)


lower = int(input("Enter lower range:"))
upper = int(input("Enter upper range:"))
for i in range(lower, upper + 1):
    if i < 2:
        continue
    else:
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                break
        else:
            print(i)


# continue statement
for i in range(1, 10):
    if i == 5:
        continue
    print(i)


# pass statement
for i in range(1, 10):
    pass
