# implicit vs explicit
print(5 + 5.6)  # Example of implicit typecasting
print(type(5), type(5.6))
# print(4 + '4')               #Error because integer and string cannot add  together

# explicit
int("4")  # str -> int
# int(4+5j)                    #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
str(5)  # int -> str
float(4)  # int -> float


a = input("Enter the first number:")
b = input("Enter second number:")
# res = a + b
res = int(a) + int(b)
print(res)
print(type(a), type(b))


a = int(input("Enter the first number:"))
b = int(input("Enter second number:"))
res = a + b
print(res)
print(type(a), type(b))
