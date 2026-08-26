# Arithmetic operators
print(5 + 6)  # Addition
print(5 - 6)  # Subtraction
print(5 * 6)  # Multiplication
print(5 / 2)  # Division
print(5 // 2)  # Integer Division
print(5 % 2)  # Modulous
print(5**2)  # Power of operator


# Relational operators
print(4 > 5)  # Greater than
print(4 < 5)  # Less than
print(4 >= 5)  # Greater than or equal to
print(4 <= 5)  # Less than or equal to
print(4 == 5)  # Equal to
print(4 != 5)  # Not equal to


# Logical operators
print(1 and 0)  # AND operator
print(1 or 0)  # OR operator
print(not 1)  # NOT operator


# Bitwise operators
print(1 & 2)  # Bitwise AND
print(1 | 2)  # Bitwise OR
print(~1)  # Bitwise NOT
print(1 ^ 2)  # Bitwise XOR
print(1 << 2)  # Left Shift
print(1 >> 2)  # Right Shift


# Assignment operators
a = 2
a += 2
a -= 2
a *= 2
a /= 2
a %= 2
a //= 2


# Membership operators
print("D" in "Delhi")
print("D" not in "Kanpur")
print(1 in [2, 3, 4, 5, 6])
print(1 not in [1, 2, 3, 4, 5])


# Find the sum of a 3-digit number entered by the user.
number = int(input("Enter a 3-digit number: "))
a = number % 10
number = number // 10
b = number % 10
number = number // 10
c = number % 10
print("Sum is ", a + b + c)
