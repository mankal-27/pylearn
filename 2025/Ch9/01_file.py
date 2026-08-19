f = open("file.txt")
print(f.read())
f.close()

w = open("file1.txt", "w")
w.write("Hello World")
w.close()

a = open("file1.txt")
print(a.read())
a.close()