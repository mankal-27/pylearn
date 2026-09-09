qunatity = 3
price = 19.99
total = qunatity * price
print(total)
print(type(total))

price1 = "19.99"
total1 = price1 * qunatity
print(total1)
print(type(total1))

price2 = "19.22"
total2 = float(price2) * qunatity
print(total2)
print(type(total2))

print(int(3.7))
print(int(-3.7))
print(int("42"))
print(int("  42  "))
print(int(True))
print(int(False))

print(int(3.9))
print(round(3.9))
print(int(-3.9))
print(round(-3.9))

print(int("42"))
#print(int("3.7")) int() won't parse a string that contains a decimal point.
print(int(float("3.7")))

#Parsing with a different base
print(int("12", 16))
print(int("ff", 16))
print(int("0xff", 16))
print(int("1010", 2))
print(int("777", 8))

print(float(42))
print(float("19.99"))
print(float("3"))
print(float("1e3"))
print(float(True))
print(float("  4.5  "))

print(float("inf"))
print(float("-inf"))
print(float("nan"))

#print(float("abc")) ValueError: could not convert string to float: 'abc'

form_input = "29.99"
price = float(form_input)
quantity = 3
total = price * quantity
print(f"Total: ${total:.2f}")

print(str(42))
print(str(19.99))
print(str(True))
print(str(None))
print(str([1, 2, 3]))
print(str({"name": "Alex"}))

quantity = 3
price = 19.99

message_old = "You bought " + str(quantity) + " items for $" + str(price)
message_new = f"You bought {quantity} items for ${price}"

print(message_old)
print(message_new)

print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(""))
print(bool(" "))
print(bool([]))
print(bool([0]))
print(bool(None))

cart = []

if cart:
    print(f"Cart has {len(cart)} items")
else:
    print("Cart is empty")

print(list("HELLO"))
print(tuple([1, 2, 3]))
print(set([1, 2, 2, 3, 3, 3]))

recently_viewed = [
    "Wireless Mouse",
    "USB Cable",
    "Wireless Mouse",
    "Webcam",
    "USB Cable",
    "Keyboard",
]

unique_unordered = set(recently_viewed)
print(unique_unordered)
unique_ordered = list(dict.fromkeys(recently_viewed))
print(unique_ordered)

prices_tuple = (29.99, 14.99, 9.99)
prices_list = list(prices_tuple)
prices_list.append(49.99)
print(prices_list)

product = dict(name="Wireless Mouse", price=19.99, stock=50)
print(product)

pairs = [
    ("name", "Wireless Mouse"),
    ("price", 19.99),
    ("stock", 50),
]
product = dict(pairs)
print(product)

product_names = ["Wireless Mouse", "USB Cable", "Webcam"]
prices = [19.99, 4.99, 39.99]

catalog = dict(zip(product_names, prices))
print(catalog)

default_settings = {"shipping": "standard", "currency": "USD"}
user_settings = dict(default_settings)
user_settings["shipping"] = "express"

print(default_settings)
print(user_settings)

form_input = "abc"

try:
    quantity = int(form_input)
    print(f"Quantity is {quantity}")
except ValueError:
    print(f"Could not parse '{form_input}' as a number")

print(3 + 4)
print(3 + 4.0)
print(3 * 2.5)
print(True + 1)
print(True + False)
#print("Price: $" + 19.99) TypeError: can only concatenate str (not "float") to str
print(f"Price: ${19.99}")

print(10 / 2)
print(10 // 2)
print(10 / 3)
print(10 // 3)