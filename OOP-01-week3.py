from dataclasses import replace

myDictionary = {"name1": "Isaac", "name2": "Doe"}
print(list)
print(myDictionary)

myDictionary.update({"name3": "sam"})
print(myDictionary)
myDictionary.update({"name4": "william"})
print(myDictionary)
del myDictionary["name4"]
print(myDictionary)
myDictionary["name4"] = "william"
print(myDictionary)

fullname = input("Enter your full name")

myDictionary.update({"name5": fullname})
print(myDictionary)

mycourses = {"c_name1": "OOP"}
print("1. Add Courses")
print("2. Remove Courses")
print("3. Replace")
print("4. Print Courses")
print ("5. Exit")
choice = input("Enter your choice: ")
if choice == "1":
    mycourses.update({"c_name1":course_name})
    print(mycourses)
elif choice == "2":
    del mycourses["c_name1"]
    print(mycourses)
elif choice == "3":
    