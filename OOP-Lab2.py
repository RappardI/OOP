myEmployees = {}

def add_employee():
    employee_name=input("enter employee name")
    basic_pay=int(input("enter basic pay"))
    allowance=int(input("enter allowance"))
    deductions=int(input("enter deductions"))
    taxes=int(input("enter taxes"))

    gross_pay = basic_pay + allowance
    net_pay = gross_pay - deductions - taxes

    myEmployees[employee_name] = {
            "e_name": employee_name,
            "basic_pay": basic_pay,
            "allowance": allowance,
            "deductions": deductions,
            "taxes": taxes,
            "gross_pay": gross_pay,
            "net_pay": net_pay
    }
    print("Employee has been added")



def delete_employee():
    employee_name = input("enter employee name")
    if employee_name in myEmployees:
       del myEmployees[employee_name]
       print("Employee deleted")
    else:
        print("Employee does not exist")


def modify_employee():
    employee_name = input("enter employee name")
    if employee_name in myEmployees:
        basic_pay=int(input("enter basic pay"))
        allowance =int(input("enter allowance"))
        deductions =int(input("enter deductions"))
        taxes =int(input("enter taxes"))

        gross_pay = basic_pay + allowance
        net_pay = gross_pay - deductions - taxes

        myEmployees[employee_name] = {
            "e_name": employee_name,
            "basic_pay": basic_pay,
            "allowance": allowance,
            "deductions": deductions,
            "taxes": taxes,
            "gross_pay": gross_pay,
            "net_pay": net_pay
        }
        print("Employee has been modified")
    else:
        print("Employee does not exist")

def display_employees():
    print(myEmployees)


while True:
    print ("1. Add an employee")
    print ("2. Delete an employee")
    print ("3. Modify an employee")
    print ("4. Display all employees")
    print ("5. Exit")

    choice = input("Enter your choice")

    if choice == "1":
        add_employee()
    elif choice == "2":
        delete_employee()
    elif choice == "3":
        modify_employee()
    elif choice == "4":
        display_employees()
    elif choice == "5":
        break
