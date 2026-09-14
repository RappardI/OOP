while("true"):
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    choice = input("Enter your choice: ")


    mylist = [5,10,15,20,25,30]
    print("current list is -",mylist)

    mylist.append(int(input("enter number to be added to list")))

    mylist.remove(int(input("enter number to be removed from list:")))
    new_remove = int(input())
    if new_remove in mylist:
    print("element is in the list")
    elif new_remove in mylist:

    mylist.remove(int(input("enter number to be replaced in list:")))
    mylist.append(int(input("enter the number you want it to replaced it with:")))

    mylist.sort()
    print(mylist)

    exit