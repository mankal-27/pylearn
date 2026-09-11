order_total = 186.75
item_count = 23
items_per_crate = 5
country = "CA"
membership = "gold"
contains_battery = False

allowed_countries = {"US", "CA", "MX"}
preferred_memberships = {"gold", "platinum"}

# TODO: use membership in preferred_memberships, order_total >= 100,
# country in allowed_countries, and not contains_battery
free_shipping = membership in preferred_memberships and order_total >= 100 and country in allowed_countries and not contains_battery

# TODO: use order_total >= 150 or contains_battery
requires_signature = order_total >= 150 or contains_battery

# TODO: use item_count // items_per_crate plus int(item_count % items_per_crate != 0)
crates_to_ship = item_count // items_per_crate + int(item_count % items_per_crate != 0)

# TODO: use item_count % items_per_crate
items_in_last_partial_crate = item_count % items_per_crate

# TODO: use not (1 <= item_count <= 50), country not in allowed_countries,
# and (contains_battery and order_total > 100)
audit_flag = not (1 <= item_count <= 50) or country not in allowed_countries or (contains_battery and order_total > 100)

# TODO: use free_shipping and requires_signature and not audit_flag
priority_handling = free_shipping and requires_signature and not audit_flag

print(f"Free shipping: {free_shipping}")
print(f"Requires signature: {requires_signature}")
print(f"Crates to ship: {crates_to_ship}")
print(f"Items in last partial crate: {items_in_last_partial_crate}")
print(f"Audit flag: {audit_flag}")
print(f"Priority handling: {priority_handling}")