#Readable Integer Literals
permissions = 0b1010  # TODO: use binary literal 0b1010
file_mode = 0o755  # TODO: use octal literal 0o755
brand_color = 0xff00ff  # TODO: use hexadecimal literal 0xff00ff
yearly_orders = 10_000_000  # TODO: use decimal literal 10_000_000

print(f"permissions: {permissions} ({type(permissions).__name__})")
print(f"file mode: {file_mode} ({type(file_mode).__name__})")
print(f"brand color: {brand_color} ({type(brand_color).__name__})")
print(f"yearly orders: {yearly_orders} ({type(yearly_orders).__name__})")