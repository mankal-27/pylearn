import os

directory = "./"

# for filename in os.listdir(directory):
#     if filename.endswith(".py"):
#         print(filename)

try:
    contents = os.listdir(directory)
    print(f"Contents of {directory}:")
    for filename in contents:
        if filename.endswith(".py"):
            print(filename)
except FileNotFoundError:
    print(f"Directory {directory} not found")
    exit(1)
except PermissionError:
    print(f"Permission denied for {directory}")
    exit(1)

exit(0)