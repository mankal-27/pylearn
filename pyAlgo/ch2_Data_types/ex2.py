#Inspect Numeric and Boolean Types
numeric_values = [
    ('quantity', 5),
    ('price', 29.99),
    ('impedance', 4 + 3j),
    ('available', True),
    ('sold_out', False),
]


def type_name(value):
    # TODO: return the runtime type name for value
    return type(value).__name__


flag_total = True + True + False  # TODO: calculate True + True + False
true_is_int = isinstance(True, int)  # TODO: check isinstance(True, int)

for label, value in numeric_values:
    print(f'{label}: {type_name(value)}')

print(f'True + True + False = {flag_total}')
print(f'True is an int subclass: {true_is_int}', end='')