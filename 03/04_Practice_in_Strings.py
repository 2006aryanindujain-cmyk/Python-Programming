# Find the length of a given string without using the len() function.
s = input("Enter a string:")
count = 0
for i in s:
    count += 1
print("Length of given string is", count)


# Extract username from a given email.
# Eg if the email is aryanjain@gmail.com
# then the username should be aryanjain.
a = input("Enter the email(like xyz@gmail.com):")
print("Your username is", a[0 : a.find("@")])


# Count the frequency of a particular character in a provided string.
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.
b = input("Enter a string:")
c = input("Enter the character whose whose frequency you want to know:")
# print("The frequency of a given character in a given string is", b.count(c))
count = 0
for i in b:
    if i == c:
        count += 1
print("The frequency of a given character in a given string is", count)


# Write a program which can remove a particular character from a string.
d = input("Enter a string:")
e = input("Enter the character which you want to remove from a string:")
result = ""
for i in d:
    if i != e:
        result = result + i
print(result)


# Write a program that can check whether a given string is palindrome or not.
f = input("Enter a string:")
g = f[::-1]
for i in range(0, len(f)):
    if g[i] != f[i]:
        print("Given string is not palindrome")
        break
else:
    print("Given string is palindrome")


# Write a program to count the number of words in a string without split().
h = input("Enter a string:")
L = []
j = ""
for i in h:
    if i != " ":
        j = j + i
    else:
        L.append(j)
        j = ""
L.append(j)
print(L)


# Write a python program to convert a string to title case without using the title().
k = input("Enter a string:")
l = ""
for i in k.split():
    l = l + (i[0].upper() + i[1:].lower())
print(l)

m = input("Enter a string:")
n = []
for i in m.split():
    n.append(i[0].upper() + i[1:].lower())
print(" ".join(l))


# Write a program that can convert an integer to string.
num = int(input("Enter the number:"))
digits = "023456789"
result = ""
while num != 0:
    result = result + digits[num % 10]
    num = num // 10
print(result)
print(type(result))
