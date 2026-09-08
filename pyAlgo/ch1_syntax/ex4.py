#Share One Grocery List
cart = ["apple", "bread", "milk"]
items = []

# TODO: bind items to the same list object as cart
# TODO: append "eggs" to the list through items
items = cart
items.append("eggs")

print(f"cart: {cart}")
print(f"items: {items}")
print(f"same object: {cart is items}")
