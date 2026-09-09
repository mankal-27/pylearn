#Truncate Decimal Strings

decimal_texts = ["3.9", "-3.9", "2.5"]

for text in decimal_texts:
    # TODO: convert text to a float before calling int() and round().
    value = float(text)
    truncated = int(value)
    rounded = round(value)
    print(f"{text}: int={truncated}, round={rounded}")
