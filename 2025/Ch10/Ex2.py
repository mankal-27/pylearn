'''
Write a class “Calculator” capable of finding square, cube and square root of a
number.
'''

class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num ** 2

    def cube(self):
        return self.num ** 3

    def square_root(self):
        return self.num ** 0.5

    def __str__(self):
        return f"Number: {self.num} , Square: {self.square()} , Cube: {self.cube()} , Square Root: {self.square_root()}"

num = int(input("Enter a number: "))
c = Calculator(num)
print(c)