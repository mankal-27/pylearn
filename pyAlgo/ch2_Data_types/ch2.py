huge = 10 ** 50
print(huge)
print(type(huge))

permissions = 0b1010
file_mode = 0o755
color = 0xff00ff

print(permissions)
print(file_mode)
print(color)

total_orders = 10_000_000
warehouse_stock = 1_250_000
zip_code = 94_103

print(total_orders)
print(warehouse_stock)
print(zip_code)

million = 1_000_000.50
binary = 0b_1010_1100

print(million)
print(binary)

price = 19.99
rating = 4.5
weight_kg = 0.35
tax_rate = 0.08

print(price, rating, weight_kg, tax_rate)

big_revenue = 1.5e6      # 1.5 x 10^6 = 1,500,000
small_fee = 2.5e-3       # 2.5 x 10^-3 = 0.0025
electron_mass = 9.11e-31

print(big_revenue)
print(small_fee)
print(electron_mass)

signal = 2 + 3j
pure_imaginary = 5j
just_real = complex(7, 0)

print(signal)
print(pure_imaginary)
print(just_real)
print(type(signal))

a = 2 + 3j
b = 1 - 1j

print(a + b)
print(a * b)

order_id = 10_245
quantity = 3
price = 19.99
discount = 0.10
signal = 2 + 3j

print(order_id, "is a", type(order_id).__name__)
print(quantity, "is a", type(quantity).__name__)
print(price, "is a", type(price).__name__)
print(discount, "is a", type(discount).__name__)
print(signal, "is a", type(signal).__name__)