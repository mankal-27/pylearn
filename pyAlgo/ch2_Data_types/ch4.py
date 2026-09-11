price = 19.99
quantity = 3
shipping = 4.99

subtotal = price * quantity
total = subtotal + shipping

print("Subtotal: ", subtotal)
print("Total: ", total)

print(10 / 3)
print(10 // 3)
print(-10 // 3)

order_count = 17
items_per_box = 5

full_boxes = order_count // items_per_box
leftover = order_count % items_per_box

print("Full boxes:", full_boxes)
print("Items left over: ", leftover)

cart_total = 75.50
free_shipping_threshold = 50

qualifies_for_free_shipping = cart_total >= free_shipping_threshold
print("Free shipping?", qualifies_for_free_shipping)

print("apple" < "banana")
#print(5 < "5")

price = 35

is_mid_range = 20 < price < 100
print(is_mid_range)

rating = 4.5
print(0 <= rating <= 5)
print(1 < rating < 5 != 0)

price = 35
is_mid_range = price > 20 and price < 100


cart_total = 75
items_in_cart = 4

ready_to_checkout = cart_total > 0 and items_in_cart > 0
print("Ready to checkout?", ready_to_checkout)

discount_code = ""

is_valid = discount_code != "" and discount_code.startswith("SAVE")
print(is_valid)

print(0 or 19.99)
print("" or "Guest")
print("Alex" and "alex@example.com")
print(None and "anything")

print(not True)
print(not "")
print(not 19.99)

cart_a = ["Wireless Mouse", "USB Cable"]
cart_b = ["Wireless Mouse", "USB Cable"]
cart_c = cart_a

print(cart_a == cart_b)
print(cart_a is cart_b)
print(cart_a is cart_c)

selected_coupon = None

if selected_coupon is None:
    print("No coupon applied")

a = 256
b = 256
print(a is b)

a = 1000
b = 1000
print(a is b)

cart = ["Wireless Mouse", "USB Cable", "HDMI Cable"]

print("USB Cable" in cart)
print("Webcam" in cart)
print("Webcam" not in cart)

email = "alex@example.com"
print("@" in email)
print(".com" in email)
print("alex" in email)

stock = {"Wireless Mouse": 12, "USB Cable": 30, "HDMI Cable": 0}

print("Wireless Mouse" in stock)
print(12 in stock)
print(12 in stock.values())

EMAIL = 0b001    # 1
SMS = 0b010      # 2
PUSH = 0b100     # 4

# Customer opts in to email and push, not SMS.
preferences = EMAIL | PUSH

print("Wants email?", bool(preferences & EMAIL))
print("Wants SMS?", bool(preferences & SMS))
print("Wants push?", bool(preferences & PUSH))

print(1 << 4)
print(16 >> 2)
print(7 >> 1)

cart_total = 0

cart_total += 19.99
cart_total += 4.99
cart_total += 14.99

print("Cart total:", cart_total)

cart_a = ["Wireless Mouse"]
cart_b = cart_a

cart_a += ["USB Cable"]
print("cart_a:", cart_a)
print("cart_b:", cart_b)

cart_a = ["Wireless Mouse"]
cart_b = cart_a

cart_a = cart_a + ["USB Cable"]
print("cart_a:", cart_a)
print("cart_b:", cart_b)

print(2 ** 3 ** 2)
print((2 ** 3) ** 2)
print(2 ** (3 ** 2))