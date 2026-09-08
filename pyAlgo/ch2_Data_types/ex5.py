#Classify Built-in Data Types

samples = [
    ('count', 42),
    ('price', 3.14),
    ('impedance', 2 + 3j),
    ('paid', False),
    ('customer', 'Aisha'),
    ('payload', b'order'),
    ('cart', [1, 2, 3]),
    ('location', (1, 2, 3)),
    ('profile', {'name': 'Aisha'}),
    ('tag_ids', {1, 2, 3}),
    ('locked_ids', frozenset({1, 2, 3})),
    ('missing', None),
]

type_info = {
    # TODO: add entries like int: ('Numeric', 'No')
    int: ('Numeric', 'No'),
    float: ('Numeric', 'No'),
    complex: ('Numeric', 'No'),
    bool: ('Numeric (bool)', 'No'),
    str: ('Sequence (text)', 'No'),
    bytes: ('Sequence (binary)', 'No'),
    list: ('Sequence (general)', 'Yes'),
    tuple: ('Sequence (general)', 'No'),
    dict: ('Mapping', 'Yes'),
    set: ('Set', 'Yes'),
    frozenset: ('Set', 'No'),
    type(None): ('Singleton', 'No'),
}

lines = []
for label, value in samples:
    value_type = type(value)
    category, mutable = type_info.get(value_type, ('unknown', 'unknown'))
    lines.append(f'{label}: {value_type.__name__} | {category} | mutable={mutable}')

print('\n'.join(lines), end='')
