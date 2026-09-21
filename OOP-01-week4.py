while("true"):
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    choice = input("Enter your choice: ")

    def add():
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        c = a + b
        print(c)

    def sub():
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        c = a - b
        print(c)

    def mul():
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        c = a * b
        print(c)

    def div():
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        c = a / b
        print(c)

    if choice == "1":
        add()
    elif choice == "2":
        sub()
    elif choice == "3":
        mul()
    elif choice == "4":
        div()

    exit(True)

