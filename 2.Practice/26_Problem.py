# Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Harry", [1, 2]}
s[4][0] = 9
# No, you cannot change the values inside a list which is contained in a set, as sets are immutable and lists are not hashable.
