course1 = int(input("Enter grade points for course 1"))
course2 = int(input("Enter grade points for course 2"))
course3 = int(input("Enter grade points for course 3"))


if precentile < 100 and precentile >=90:
    print("Grade A")
elif precentile <90 and precentile >=80:
    print("Grade B")
elif precentile <80 and precentile >=70:
    print("Grade C")
elif precentile <70 and precentile >=60:
    print("Grade D")
elif precentile <60 and precentile >50:
    print("Course Failed")