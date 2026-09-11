a = 2
b = 3
c = 4

# TODO: use a + b * c ** 2
default_precedence = a + b * c ** 2

# TODO: use (a + b) * c ** 2
grouped_sum_first = (a + b) * c ** 2

# TODO: use ((a + b) * c) ** 2
grouped_before_power = ((a + b) * c) ** 2

# TODO: use 2 ** -3
negative_exponent = 2 ** -3

print(f"Default precedence: {default_precedence}")
print(f"Grouped sum first: {grouped_sum_first}")
print(f"Grouped before power: {grouped_before_power}")
print(f"Negative exponent: {negative_exponent}")