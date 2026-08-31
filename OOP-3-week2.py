number1 = int(input("enter number1"))
number2 = int(input("enter number2"))

operator = input("enter operator")

if operator == "+":
    c = number1 + number2
elif operator == "-":
    c = number1 - number2
elif operator == "*":
    c = number1 * number2
elif operator == "/":
    c = number1 / number2
elif number1 / 0:
    print("The total equals" ,undefined)
elif number2 / 0:
    print("The total equals" ,undefined)

 print("The total of number1 and number2 is",c)