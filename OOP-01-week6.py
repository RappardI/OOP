from hashlib import algorithms_guaranteed


class Student:
    def __init__(self):
        self.ID = ""
        self.name = ""
        self.age = ""

    def display_student(self):
        print(self.ID)
        print(self.name)
        print(self.age)


class Faculty:
    def __init__(self):
        self.ID = ""
        self.name = ""
        self.age = ""

    def display_faculty(self):
        print(self.ID)
        print(self.name)
        print(self.age)

class Courses:
    def __init__(self):
        self.coursename = ""
        self.grade = ""

    def display_course(self):
        print(self.coursename)
        print(self.grade)


while(True):

    print("1. Add Student")
    print("2. Add Faculty")
    print("3. Add Course")
    print("4. Exit")
    choice = int(input())

    if choice == 1:
        ID = input("Enter ID : ")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        print(Student)

    elif choice == 2:
        ID = input("Enter ID : ")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        print(Faculty)

    elif choice == 3:
        ID = input("Enter ID : ")
        name = input("Enter Name : ")
        print(Courses)



