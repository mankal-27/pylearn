'''
. Write a program to print the following star pattern.
 *
***
***** for n = 3
'''

n = int(input("Enter the number of rows: "))

for i in range(n):
    spaces = n - i - 1  # Number of spaces before stars
    stars = 2 * i + 1   # Number of stars in each row
    print(" " * spaces + "*" * stars)
