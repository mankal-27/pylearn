'''
Can we have a set with 18 (int) and '18' (str) as a value in it?
'''

a = {18, '18'}
print(a)

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print(s)
print(len(s))

s = {}
print(type(s))


s = {8, 7, 12, "Harry", (1, 2)}  # ✅ This will work
print(s)

s = {8,7,12,'manju', [1,2]}
print(s)
