'''
Write a recursive function to calculate the sum of first n natural numbers.
'''

def sum_natural(n):
    if n <= 0:
        return 0  # Base case: Sum of first 0 natural numbers is 0
    elif n == 1:
        return 1  # Base case: Sum of first 1 natural number is 1
    else:
        return n + sum_natural(n - 1)  # Recursive call

n = int(input("Enter a number: "))
print(f"Sum of first {n} natural numbers is {sum_natural(n)}")
