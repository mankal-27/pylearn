notebook_price = 2.50
notebook_count = 3
pen_price = 1.25
shipping = 4.00
bundle_discount = 1.50

# TODO: use notebook_price * notebook_count + pen_price
subtotal = notebook_price * notebook_count + pen_price

# TODO: use subtotal + shipping
total = subtotal + shipping

# TODO: use (notebook_price * notebook_count - bundle_discount) / notebook_count
discounted_notebook_average =  (notebook_price * notebook_count - bundle_discount) / notebook_count

print(f"Subtotal: ${subtotal:.2f}")
print(f"Total: ${total:.2f}")
print(f"Discounted notebook average: ${discounted_notebook_average:.2f}")