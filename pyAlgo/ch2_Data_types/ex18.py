price = 42
inventory = 8
rating = 4.7
coupon_code = "SAVE10"
discontinued = False

# TODO: use the chained comparison 20 < price < 50
price_in_range = 20 < price < 50

# TODO: use inventory >= 5
inventory_ok = inventory >= 5

# TODO: use the chained comparison 0 <= rating <= 5
rating_ok = 0 <= rating <= 5

# TODO: use coupon_code == "SAVE10"
coupon_ok = coupon_code == "SAVE10"

# TODO: combine all checks with and, including not discontinued
can_apply_coupon = price_in_range and inventory_ok and rating_ok and coupon_ok and not discontinued

print(f"Price in range: {price_in_range}")
print(f"Inventory ok: {inventory_ok}")
print(f"Rating ok: {rating_ok}")
print(f"Coupon accepted: {coupon_ok}")
print(f"Apply coupon: {can_apply_coupon}")