#Write a program to detect double space in a string.

a = input("Enter a string: ")
if "  " in a:
    print("Double space found at index:", a.find("  "))
else:
    print("No double space found.")

# Replace double spaces with a single space
modified_string = a.replace("  ", " ")

print("Modified string:", modified_string)