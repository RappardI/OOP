from streamlit.web.skills import agent_harness_present

from ClassWork3 import name


class Person:
    def __init__(self):
        self.name = name(self)
        self.id = id(self)
        self.age = age(self)
        self.interests = interests(self)
    def display(self):
        print(self.name)
        print(self.id)
        print(self.age)
        print(self.interests)



class Student(Person):
    def __init__(self, a, b, c, d, x, y, z):
        Person.__init__(self.a,b,c,d)
        self.major = x
        self.gpa = y
        self.minor = z
    def display(self):
        Person.display()
        print(self.major)
        print(self.gpa)
        print(self.minor)


class Faculty(Person):
    def __init__(self, x, y, z):
        Person.__init__(self)
        self.department = x
        self.designation = y
        self.salary = z
    def display(self):
        Person.display(self)
        print(self.department)
        print(self.designation)
        print(self.salary)

s1 = Student("Isaac", "101", 19, "Music" "CS", 3.9, "AI")
f1 = Faculty("CS", "Prof", "150000")

