#Inspect Boolean Conversion
values = [
    ('empty string', ''),
    ('string "False"', 'False'),
    ('string "0"', '0'),
    ('integer 0', 0),
    ('empty list', []),
    ('list with zero', [0]),
]


def as_bool(value):
    # TODO: explicitly convert value to bool.

    return bool(value)


for label, value in values:
    print(f"{label}: {as_bool(value)}")
