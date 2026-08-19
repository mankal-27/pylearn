'''
Write a program to find out the line number where python is present from ques 6.
'''

with open("log.txt", "r") as f:
    content = f.readlines()
    for i in range(len(content)):
        if "python" in content[i]:
            print(f"Line number where python is present is {i + 1}")
            break
    else:
        print("Python is not present in the file")


