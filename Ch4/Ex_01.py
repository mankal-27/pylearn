#Write a program to store seven fruits in a list entered by the user.

fruits = []
for i in range(7):
    fruit = input("Enter a fruit: ")
    fruits.append(fruit)
print(fruits)