'''
Write a program to find the sum of first n natural numbers using while loop.
'''

n = int(input("Enter a number: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    total = (n * (n + 1)) // 2  # Using integer division
    print(f"Sum of first {n} natural numbers: {total}")
