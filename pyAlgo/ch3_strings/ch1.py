product_name = "Wireless Headphones"
customer_name = "Aarav Mehta"
order_status = "shipped"

print(product_name)
print(customer_name)
print(order_status)
print(type(product_name))

title_a = "Wireless Headphones"
title_b = 'Wireless Headphones'

print(title_a == title_b)
print(type(title_a))
print(type(title_b))

review = "It's the best laptop I've ever owned."
print(review)

product_blurb = 'Now featuring the new "Pro" mode for power users.'
print(product_blurb)

mixed = "He said \"It's on sale\" and walked off."
print(mixed)

email = "mkllk@gmail.com"
empty = ""

print(len(product_name))
print(len(email))
print(len(empty))

search_query = "wireless"

if len(search_query) < 3:
    print("Search must be at least 3 characters")
else:
    print("Searching for: " + search_query)

quantity = 3
price = 29.99
in_stock = True

quantity_text = str(quantity)
price_text = str(price)
in_stock_text = str(in_stock)

print(quantity_text)
print(price_text)
print(in_stock_text)
print(type(quantity_text))

product = "Wireless Headphones"
status = "shipped"

confirmation = "Your order for " + product + " has been " + status + "."
print(confirmation)

quantity = 3
#message = "You have " + quantity + " items in your cart." TypeError: can only concatenate str (not "int") to str
#print(message)

quantity = 3
message = "You have " + str(quantity) + " items in your cart."
print(message)

quantity = 3
print("You have", quantity, "items in your cart.")

nothing = "abc" * 0
also_nothing = "abc" * -5

print(repr(nothing))
print(repr(also_nothing))
print(len(nothing))
print(len(also_nothing))

title = "ORDER SUMMARY"
print("=" * 40)
print(" " * 13 + title)
print("=" * 40)

product_name = "Wireless Bluetooth Headphones"

print("Bluetooth" in product_name)
print("USB" in product_name)
print("phones" in product_name)
print("Wireless" not in product_name)

search_query = "Headphones"
product_titles = [
    "Wireless Bluetooth Headphones",
    "Mechanical Keyboard",
    "Noise Cancelling Headphones",
    "USB-C Charging Cable",
]

for title in product_titles:
    if search_query in title:
        print("Match:", title)

email = "aarav@example.com"

if "@" not in email:
    print("Invalid email address")
else:
    print("Looks like an email")

product = "laptop"

print(product[0])
print(product[1])
print(product[2])
print(product[5])

product = "laptop"

print(product[-1])
print(product[-2])
print(product[-6])

product = "laptop"

first = product[0]
print(first)
print(type(first))
print(len(first))

product = "laptop"
#print(product[10]) IndexError: string index out of range

product_code = "AB"

if len(product_code) >= 4:
    category_code = product_code[3]
    print("Category:", category_code)
else:
    print("Code too short")

product = "laptop"

for char in product:
    print(char)

email = "aarav@example.com"
at_count = 0

for c in email:
    if c == "@":
        at_count = at_count + 1

print("Number of @ signs:", at_count)

review = "Great laptop! Battery lasts forever."
exclamations = sum(c == "!" for c in review)
print("Exclamation marks:", exclamations)

product = "laptop"

for index, char in enumerate(product):
    print(index, char)

greeting = ""
print(repr(greeting))
print(len(greeting))
print(type(greeting))

print(bool(""))
print(bool("a"))
print(bool(" "))
print(bool("0"))
print(bool("False"))

customer_address = ""

if customer_address:
    print("Shipping to:", customer_address)
else:
    print("No address on file")

search_query = ""

if not search_query:
    print("Please enter a search term")

maybe_address = "   "

if maybe_address:
    print("Has an address (technically)")

print(len(maybe_address))

product = "laptop"
product = "L" + product[1:]
print(product)