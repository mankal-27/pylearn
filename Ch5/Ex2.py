'''
Write a program to input eight numbers from the user and display all the unique
numbers (once).
'''

a = set()
for i in range(8):
    num = int(input("Enter a number: "))
    a.add(num)
print(a)
