#Compare Strings and Bytes

order_text = 'order_id=12345'

order_bytes = order_text.encode('utf-8')  # TODO: encode order_text using UTF-8
first_byte = order_bytes[0]  # TODO: read the integer byte at index 0
first_character = chr(first_byte)  # TODO: convert first_byte to a character

print(f'Text type: {type(order_text).__name__}')
print(f'Bytes value: {order_bytes}')
print(f'Bytes type: {type(order_bytes).__name__}')
print(f'Byte length: {len(order_bytes)}')
print(f'First byte: {first_byte}')
print(f'First character: {first_character}', end='')