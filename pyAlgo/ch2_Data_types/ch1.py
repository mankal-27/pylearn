quantity = 5
price = 29.99
impedance = 3 + 4j

print(type(quantity))
print(type(price))
print(type(impedance))

print(True + True)
print(isinstance(True, int))

customer = "Srikar"
product = "Wireless Mouse"
greeting = "Welcome Srikar"

print(type(customer))
print(len(product))

order_data = b"order_id=12345"
print(type(order_data))
print(order_data[0])

cart = ["apple", "bananna", "bread"]
cart.append("egg")
print(cart)
print(type(cart))

order_position = (33.4444, -123.4445)
customer_info = "Srikar", "srikar@gmail.com", 36


print(type(customer_info))

customer = {
    "name": "Srikart",
    "email": "srikar@gmail.com",
    "orders": 5
}

print(customer["name"])
print(type(customer))

favorite_categories = {"electronics", "books", "kitchen"}
favorite_categories.add("electronics")
favorite_categories.add("toys")

print(favorite_categories)
print(type(favorite_categories))

fixed_categories = frozenset({"electronics", "books"})
print(type(fixed_categories))

shipping_address = None
print(type(shipping_address))
print(shipping_address is None)


def save_order():
    pass

result = save_order()
print(result)
print(result is None)

cart1 = ["apple"]
cart1.append("bread")
print(cart1)

product1 = "Mouse"
upgraded = product1.upper()
print(product1)
print(upgraded)

order = ("ORD-1", ["apple", "bread"])
order[1].append("milk")
print(order)

flag = True

print(type(flag) == int)
print(isinstance(flag, int))

def is_number(value):
    return isinstance(value, (int, float, complex))

print(is_number(5))
print(is_number("5"))
print(is_number(3.14))