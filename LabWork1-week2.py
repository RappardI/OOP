import length

while ("true"):
    print("area of a rectangle")
    print("volume of a cube")
    print("area of a circle")
    print("circumference of a circle")
    choice = input("enter your choice")

    if choice == "5":
        exit()
    if choice == "1":
        length = int(input("enter your length"))
        width = int(input("enter your width"))
        area = length * width
        print("answer:", area)
    elif choice == "2":
        length = int(input("enter your length"))
        width = int(input("enter your width"))
        height = int(input("enter your height"))
        volume = length * width * height
        print("answer:", volume)
    elif choice == "3":
        radius = int(input("enter your radius"))
        areaofcircle = 3.14 * radius * radius
        print("answer:", areaofcircle)
    elif choice == "4":
        radius = int(input("enter your radius"))
        circumferenceofcircle = 2 * 3.14 * radius
        print("answer:", circumferenceofcircle)


