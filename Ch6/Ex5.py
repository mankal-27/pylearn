'''
Write a program which finds out whether a given name is present in a list or not.
'''

name = input("Enter a name: ")
names = ["Manju", "Abhishek", "Srikar", "Manoj"]
if name in names:
    print(f"{name} is present in the list")
else:
    print(f"{name} is not present in the list")