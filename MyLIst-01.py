mylist = [5,10,15,20,25]

mylist.append(66)
print(mylist)

mylist.remove(9)
print(mylist)

mylist.pop()
print(mylist)

mylist.sort()
print(mylist)

newlist = mylist.copy()
newlist.append (1001)

newvalue = int(input())
if newvalue in mylist:
    print("Element is in the list")
else:
    print("Element is not in the list")
