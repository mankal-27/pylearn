#Create a Product Record with Basic Types

product_name = 'Wireless Mouse'  # TODO: use the string 'Wireless Mouse'
quantity = 5  # TODO: use the int 5
price = 29.99  # TODO: use the float 29.99
in_stock = True  # TODO: use the bool True
discount_code = None  # TODO: use None

print(f'Product: {product_name} ({type(product_name).__name__})')
print(f'Quantity: {quantity} ({type(quantity).__name__})')
print(f'Price: {price} ({type(price).__name__})')
print(f'In stock: {in_stock} ({type(in_stock).__name__})')
print(f'Discount code: {discount_code} ({type(discount_code).__name__})', end='')
