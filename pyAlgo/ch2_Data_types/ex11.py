#Convert Form Values for a Total

price_text = "19.99"
quantity_text = "3"

# TODO: convert price_text to a float.
price = float(price_text)

# TODO: convert quantity_text to an int.
quantity = int(quantity_text)

total = price * quantity

print(f"Total: ${total:.2f}")
print(f"price type: {type(price).__name__}")
print(f"quantity type: {type(quantity).__name__}")
print(f"total type: {type(total).__name__}")