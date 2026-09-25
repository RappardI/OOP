myEmployees = {}
i=1

def add_employee():
    employee_name = input("enter employee name")


        basic_pay=int(input("enter basic pay"))
        allowance=int(input("enter allowance"))
        deductions=int(input("enter deductions"))
        taxes=int(input("enter taxes"))
        gross_pay=int(input("enter gross_pay"))
        net_pay=int(input("enter net_pay"))
        myEmployees.update({"E"+str(i):
            {   "e_name": employee_name,
                "basic_pay": basic_pay,
                "allowance": allowance,
                "deductions": deductions,
                "taxes": taxes,
                "gross_pay": gross_pay,
                "net_pay": net_pay
                }})



def delete_employee():
    employee_name = input("enter employee name")
    if employee_name in myEmployees:
        myEmployees.pop(employee_name)
    else:
        print("employee does not exist")

    def modify_employee():
        empid = input("enter employee id")

        updated_employee_name= input("enter employee name")
        myEmployees[empid]["e_name"] = updated_employee_name
        updated_employee_basic_pay= input("enter employee name")
        myEmployees[empid]["basic_pay"] = updated_employee_basic_pay
        updated_employee_allowance= input("enter employee name")
        myEmployees[empid]["allowance"] = updated_employee_allowance
        updated_employee_deductions= input("enter employee deductions")
        myEmployees[empid]["deductions"] = updated_employee_deductions
        updated_employee_taxes= input("enter employee taxes")
        myEmployees[empid]["taxes"] = updated_employee_taxes
        updated_employee_gross_pay= input("enter employee gross pay")
        myEmployees[empid]["gross_pay"] = updated_employee_gross_pay
        updated_employee_net_pay= input("enter employee net pay")
        myEmployees[empid]["net_pay"] = updated_employee_net_pay



def display_employees():
    print(myEmployees)



while True:
    print menu



    add_employee()
    i=i+1