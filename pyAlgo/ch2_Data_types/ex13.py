#Parse Numbers from Different Bases

red_hex = "ff"
green_hex = "7f"
blue_hex = "00"
binary_text = "101101"
octal_text = "777"

# TODO: parse each hexadecimal color channel using base 16.
red = (red_hex, 16)
green = (green_hex, 16)
blue = (blue_hex, 16)

# TODO: parse binary_text using base 2.
binary_value = (binary_text, 2)

# TODO: parse octal_text using base 8.
octal_value = (octal_text, 8)

print(f"RGB decimal: {red}, {green}, {blue}")
print(f"Binary {binary_text} = {binary_value}")
print(f"Octal {octal_text} = {octal_value}")
