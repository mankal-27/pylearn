# Rebind One Name, Mutate Another
primary = ["red", "green"]
alias = primary

# TODO: rebind primary to a new list made with primary + ["blue"]
# TODO: mutate alias by assigning "yellow" to index 0

primary += ["blue"]
alias[0] = "yellow"

print(f"primary: {primary}")
print(f"alias: {alias}")
print(f"same object: {primary is alias}")