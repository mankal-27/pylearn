#Unpack Contact Details and Swap Counts

recipient = ""
city = ""
package_count = 0

# TODO: bind recipient, city, and package_count with one tuple-unpacking assignment

recipient, city, package_count = "Mina Patel", "Denver", 3

morning_count = 7
evening_count = 11

print(f"Contact: {recipient} in {city}")
print(f"Packages: {package_count}")
print(f"Before swap: morning={morning_count}, evening={evening_count}")

# TODO: swap morning_count and evening_count with one multiple-assignment statement

morning_count, evening_count = evening_count, morning_count

print(f"After swap: morning={morning_count}, evening={evening_count}")