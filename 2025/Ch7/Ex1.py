'''
Write a program to print multiplication table of a given number using for loop
'''

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

#use while loop

num = int(input("Enter a number: "))
i = 1
while(i < 11):
    print(f"{num} * {i} = {num * i}")
    i = i + 1