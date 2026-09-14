# len/min//max/sorted :-
l1 = [2, 1, 5, 7, 0]
print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1))
print(sorted(l1, reverse=True))


# count :-
l2 = [1, 2, 3, 1, 2, 4, 3, 2, 5]
print(l2.count(1))


# index :-
l3 = [1, 2, 1, 3, 4, 1, 5]
print(l3.index(1))


# reverse => it permanently reverses the list.
l4 = [2, 1, 5, 7, 0]
l4.reverse()
print(l4)


# sort vs sorted :-
l5 = [2, 1, 5, 7, 0]
print(l5)
print(sorted(l5))
print(l5)
l5.sort()
print(l5)


# copy(makes shallow copy) :-
l6 = [2, 1, 5, 7, 0]
print(l6)
print(id(l6))
l7 = l6.copy()
print(l7)
print(id(l7))
