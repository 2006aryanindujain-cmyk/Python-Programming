L = [1, [2, [[3], [4]], 5], [1, 2]]

# Positive Indexing :-
print(L[0])
print(L[1])
print(L[1][1])
print(L[1][1][0])

# Negative Indexing :-
print(L[-1])
print(L[-1][0])
print(L[-2][1])
print(L[-2][1][0])

# Slicing :-
l = [1, 2, 3, 4, 5, 6]
print(l[-3:])
print(l[0::2])
print(l[-5:-2:2])
