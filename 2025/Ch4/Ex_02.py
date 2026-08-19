#Write a program to accept marks of 6 students and display them in a sorted
# manner.

marks = []
for i in range(6):
    mark = int(input("Enter a mark: "))
    marks.append(mark)
marks.sort()
print(marks)