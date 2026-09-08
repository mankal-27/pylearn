#Mutate a List and Extend a Tuple
cart = ['apple', 'bread', 'milk']
location = ('Aisle 4', 'Shelf B')

# TODO: add 'eggs' to cart in place
cart.append("eggs")
updated_location = location  # TODO: create a new tuple with 'Bin 12' added
updated_location = location + ("Bin 12",)

print(f'Cart: {cart}')
print(f'Original location: {location}')
print(f'Updated location: {updated_location}')
print(f'Cart type: {type(cart).__name__}')
print(f'Location type: {type(location).__name__}', end='')