#Calculate a Float Cart Total
unit_price = 19.99
quantity = 3
tax_rate = 0.0825
shipping = 4.99

# TODO: compute subtotal, tax, and total from the values above
subtotal = unit_price * quantity
tax = subtotal * tax_rate
total = subtotal + tax + shipping

print(f"subtotal: ${subtotal:.2f}")
print(f"tax: ${tax:.2f}")
print(f"shipping: ${shipping:.2f}")
print(f"total: ${total:.2f}")
print(f"total type: {type(total).__name__}")