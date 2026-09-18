mycourses = {}
i = 1
while True:

    print("1. Add Courses")
    print("2. Remove Courses")
    print("3. Replace")
    print("4. Print Courses")
    print ("5. Exit")
    choice = input("Enter your choice: ")
    course_name = input("Enter your course name: ")
    mycourses.update({"c_name1" + str(id): course_name})


    if choice == "1":
        mycourses.update({"c_name1":course_name})
        print(mycourses)
    elif choice == "2":
        del mycourses["c_name1"]
        print(mycourses)
    elif choice == "3":
        del mycourses
    elif choice == "4":
        print(mycourses)
        break

