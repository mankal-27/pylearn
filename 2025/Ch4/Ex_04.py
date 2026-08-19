#Write a program to sum a list with 4 numbers.

a = [1,2,3,4]
print(sum(a))

#sum of numbers in a list without using sum method

a = [1,2,3,4]
sum = 0
for i in a:
    sum = sum + i
print(sum)