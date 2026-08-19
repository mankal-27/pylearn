'''
Write a program to find out whether a file is identical & matches the content of
another file.
'''

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    content1 = f1.read()
    content2 = f2.read()

    if content1 == content2:
        print("The files are identical.")
    else:
        print("The files are not identical.")   