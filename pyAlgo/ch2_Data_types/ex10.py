#Mixed Numeric Inventory Audit
starting_stock = 1_250_000  # TODO: use 1_250_000
restock_batch = 0b_1111_0100  # TODO: use 0b_1111_0100
reserved_units = 0o1750  # TODO: use 0o1750
unit_price = 19.95  # TODO: use 19.95
base_signal = 2 + 3j  # TODO: use 2 + 3j
calibration = 1 - 1j  # TODO: use 1 - 1j

# TODO: compute the three derived values
available_stock = starting_stock + restock_batch - reserved_units
inventory_value = available_stock * unit_price
calibrated_signal = base_signal * calibration

print(f"available stock: {available_stock}")
print(f"stock type: {type(available_stock).__name__}")
print(f"inventory value: ${inventory_value:.2f}")
print(f"value type: {type(inventory_value).__name__}")
print(f"calibrated signal: {calibrated_signal}")
print(f"signal type: {type(calibrated_signal).__name__}")