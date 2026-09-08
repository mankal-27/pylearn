price = 19.99
print(id(price))

price = 24.99
print(id(price))

cart = ["apple", "carrot", "kiwi"]
items = cart

print(id(cart))
print(id(items))
print(cart is items)

cart1 = ["apple", "carrot", "kiwi"]
items1 = cart1
items1.append("eggs")

print(id(cart1))
print(cart1)
print(id(items1))
print(items1)

#Rebiniding VS Mutating
cart2 = ["apple", "bread"]
items2 = cart2

cart2 = ["new", "list"]

print(cart2)
print(id(cart2))
print(items2)
print(id(items2))

#Multiple Assignment 
name, email, age = "Manjunath", "mnkalkutagi@gmail.com", 35
print(name)
print(email)
print(age)

#chain assignments
cart_a = cart_b = []
cart_a.append("apple")
print(cart_b)

#swapping values
first_item = "wireless mouse"
second_item = "USB cable"


print(first_item)
print(second_item)
first_item, second_item = second_item, first_item
print(f"*" * 10)
print(first_item)
print(second_item)

#Augmented Assignment

total = 0
total += 19.99
total += 24.99
total += 9.99
print(round(total,2))

# Numeric and bitwise operator
# Operator	Equivalent to	Use case
# +=	x = x + y	Add to running total
# -=	x = x - y	Deduct stock, decrement quantity
# *=	x = x * y	Apply a multiplier
# /=	x = x / y	Divide and rebind
# //=	x = x // y	Integer division
# %=	x = x % y	Modulo
# **=	x = x ** y	Power

cart3 = ["apple"]
items3 = cart3
cart3 += ["bread"]
print(cart3)
print(items3)

cart4 = ["apple"]
items4 = cart4
cart4 = cart4 + ["bread"]
print(cart4)
print(items4)

#Dynamic typing

order_id = 12345
print(type(order_id))

order_id = "ORD-12345"
print(type(order_id))

order_id = None
print(type(order_id))

import keyword
print(keyword.kwlist)

price1 = 19.99
print(price1)

#del price1
#print(price1) NameError: name 'price1' is not defined. Did you mean: 'price'?

cart5 = ["apple", "bannana"]
items5 = cart5

del cart5
print(items5)