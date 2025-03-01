'''
Write a program to find whether a given number is prime or not.
'''
import math

num = int(input("Enter a number: "))

# Edge cases
if num < 2:
    print(f"{num} is not a prime number")
else:
    flag = False
    for i in range(2, int(math.sqrt(num)) + 1):  # Check up to √num
        if num % i == 0:
            flag = True
            break

    if flag:
        print(f"{num} is not a prime number")
    else:
        print(f"{num} is a prime number")
