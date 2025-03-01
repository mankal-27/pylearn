'''
Write a program to calculate the factorial of a given number using for loop.
'''

# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial = factorial * i
# print(f"The factorial of {num} is {factorial}")

# num = int(input("Enter a number: "))
#
# # Factorial is only defined for non-negative integers
# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# elif num == 0 or num == 1:
#     print(f"The factorial of {num} is 1")
# else:
#     factorial = 1
#     for i in range(2, num + 1):  # Start from 2 (since 1 * 1 is redundant)
#         factorial *= i
#
#     print(f"The factorial of {num} is {factorial}")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")
