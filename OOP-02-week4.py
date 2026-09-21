myQueue = []

def enqueue():
    myQueue.append(1)
    print(myQueue)
def dequeue():
    myQueue.pop(0)
    print(myQueue)
def display_queue():
    print(myQueue)

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

    while True:
        if choice == "1":
            enqueue()
        elif choice == "2":
            dequeue()
        elif choice == "3":
            display_queue()
        exit(True)



