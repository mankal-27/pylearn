'''
Write a program to find the greatest of four numbers entered by the user
'''

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))
d = int(input("Enter another number: "))
print(max(a, b, c, d))

# this will give the greatest number

print(min(a, b, c, d))

# this will give the smallest number
# dont use max and min
if(a > b and a > c and a > d):
    print(a)
elif(b > a and b > c and b > d):
    print(b)
elif(c > a and c > b and c > d):
    print(c)
elif(d > a and d > b and d > c):
    print(d)