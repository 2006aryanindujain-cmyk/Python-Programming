# Arithmetic(+,*) :-
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
print(l1 + l2)  # Concatenation/Merging
print(l1 * 3)
print(l2 * 3)


# Membership Operators :-
l3 = [1, 2, 3, 4, 5]
l4 = [1, 2, 3, 4, [5, 6]]
print(5 in l3)
print(5 not in l3)
print(5 in l4)
print([5, 6] in l4)


# Loops :-
l5 = [1, 2, 3, 4, 5]
l6 = [1, 2, 3, 4, [5, 6]]
l7 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
for i in l5:
    print(i)
for i in l6:
    print(i)
for i in l7:
    print(i)
