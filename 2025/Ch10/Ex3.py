'''
Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?
'''

class A:
    a = 10

obj = A()
obj.a = 0
print(A.a)