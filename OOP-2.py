
number1 = int(input("enter number1"))
number2 = int(input("enter number2"))
number3 = int(input("enter number3"))

if number1 > number2:
    print("number1 is is the biggest")

elif number2 > number1 and number2 > number3:
        print("number2 is biggest")

elif number1 > number3 and number1 > number2:
        print("number1 is biggest")

elif number3 > number1 and number3 > number2:
    print("number3 is biggest")

elif number1 == number3 and number2 == number3:
    print("They are all equal")

elif number1 == number2:
    print("number1 and number2 are equal")

elif number1 == number3:
    print("number1 and number3 are equal")

elif number2 == number3:
    print("number2 and number3 are equal")


else:
    print("Invalid number")

