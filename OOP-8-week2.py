while("true"):
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    choice = input("Enter your choice: ")

    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))

    if choice == "1":
        c = a + b
        print(c)
    elif choice == "2":
        c = a - b
        print(c)
    elif choice == "3":
        print(c)
    elif choice == "4":
        c = a / b
        print(c)
    exit("true")