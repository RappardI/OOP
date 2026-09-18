from idlelib.undo import CommandSequence

students = {"s1":
                {"name":"isaac",
                 "major":"computer science",
                 "year":"freshman",
                 "gpa":"3.9"

                 },
            "s2":
                {"name":"john",
                 "major":"nursing",
                 "year":"freshman",
                 "gpa":"3.9"

            }
            }
i=1
while True:
    print("1. Add Course")
    print("2. Remove Course")
    print("3. Edit Course")
    print("4. Print Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name")
        major = input("Enter student major")
        year = input("Enter student year")
        gpa = input("Enter student GPA")

        students.update({"s"+str(i):
                             {
                                 "stu_name":name,
                                 "stu_major":major,
                                 "stu_year":year,
                                 "gpa":gpa
                             }
                        })
        i = i+1
    elif choice == "2":
        