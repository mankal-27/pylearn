#Combine Complex Signals
base_signal = 3 + 4j  # TODO: use 3 + 4j
adjustment = -1 + 2j  # TODO: use -1 + 2j

# TODO: add the two complex numbers
combined_signal = base_signal + adjustment

print(f"combined: {combined_signal}")
print(f"real part: {combined_signal.real}")
print(f"imaginary part: {combined_signal.imag}")
print(f"type: {type(combined_signal).__name__}")