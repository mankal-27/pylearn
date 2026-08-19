# Sets
s = set()
print(s)
s.add(1)
print(s)
s.add(2)
print(s)
s.add(3)
print(s)
s.add(1)
print(s)
s.remove(1)
print(s)

# Union
a = {1, 2, 3}
b = {2, 3, 4}
c = a.union(b)
print(c)

# Intersection
a = {1, 2, 3}
b = {2, 3, 4}
c = a.intersection(b)
print(c)

# Difference
a = {1, 2, 3}
b = {2, 3, 4}
c = a.difference(b)
print(c)

# Symmetric Difference
a = {1, 2, 3}
b = {2, 3, 4}
c = a.symmetric_difference(b)
print(c)

# Subset
a = {1, 2, 3}
b = {2, 3, 4}
c = a.issubset(b)
print(c)

# Superset
a = {1, 2, 3}
b = {2, 3, 4}
c = a.issuperset(b)
print(c)

# Disjoint
a = {1, 2, 3}
b = {2, 3, 4}
c = a.isdisjoint(b)
print(c)

# Frozenset
a = {1, 2, 3}
b = frozenset(a)
print(b)

# Set Comprehension
a = {1, 2, 3, 4, 5}
b = {x for x in a if x % 2 == 0}
print(b)

# Dictionary Comprehension
a = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
b = {x: y for x, y in a.items() if x % 2 == 0}
print(b)

# List Comprehension
a = [1, 2, 3, 4, 5]
b = [x for x in a if x % 2 == 0]
print(b)