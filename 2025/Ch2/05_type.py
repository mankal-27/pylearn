# Type Casting

a = 1
b = 5.22
c = "Manju"
d = True
e = None

print(f"a is {type(a)}")
print(f"b is {type(b)}")
print(f"c is {type(c)}")
print(f"d is {type(d)}")
print(f"e is {type(e)}")

print("******************")
print("Type Casting")
a = str(a)
b = int(b)
c = float(c) # this will not work
d = bool(d)
e = None

print(f"a is {type(a)}")
print(f"b is {type(b)}")
print(f"c is {type(c)}")
print(f"d is {type(d)}")
print(f"e is {type(e)}")