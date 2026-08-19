# List Methods

friends = ["apple", "bannana", "cherry", 7, False, None]

print(friends)
# All List Methods like sort reverse

mylist = [34,545,233,567,9022,1,2,3,4,5,6,7,8,9,10]
#sorting the list
mylist.sort()
print(mylist)
#reversing the list
mylist.reverse()
print(mylist)
#length of the list
print(len(mylist))
#max of the list
print(max(mylist))
#min of the list
print(min(mylist))

#sum of the list
print(sum(mylist))

#count of the list
print(mylist.count(34))

#append of the list
mylist.append(34)
print(mylist)

#insert of the list
mylist.insert(1,34)
print(mylist)

#remove of the list
mylist.remove(34)
print(mylist)

#pop of the list
mylist.pop()
print(mylist)

#clear of the list
mylist.clear()
print(mylist)

#copy of the list
mylist2 = mylist.copy()
print(mylist2)

#extend of the list
mylist.extend(mylist2)
print(mylist)


