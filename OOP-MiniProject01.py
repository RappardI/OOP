import mysql.connector
from mysql.connector import cursor

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="StudentMasterDB"
)
mycursor = mydb.cursor()

mycursor.execute("""
            CREATE TABLE IF NOT EXISTS Student (
            StudentID INT PRIMARY KEY,
            Name VARCHAR(50),
            Department VARCHAR(50)
        )
""")
print("Student Table created successfully")


def insert_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    department = input("Enter Student Department: ")
    sql = "INSERT INTO Student (StudentID, Name, Department) VALUES (%s, %s, %s)"
    val = (sid, name, department)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Record inserted successfully")


def display_students():
    cursor.execute("SELECT * FROM Student")
    for row in cursor.fetchall():
        print(row)


def update_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    department = input("Enter Student Department: ")
    sql = """
    UPDATE Student
    SET Name = %s, Department = %s
    WHERE StudentID = %s
    """
    cursor.execute(sql, (name, department, sid))
    mydb.commit()
    print("Record Updated!" if cursor.rowcount else "Record Not Found")


def delete_student():
    sid = int(input("Enter Student ID: "))
    sql = "DELETE FROM Student WHERE StudentID = %s"
    cursor.execute(sql, (sid,))
    mydb.commit()
    print("Record Deleted!" if cursor.rowcount else "Record Not Found")


def insert_faculty():
    sid = int(input("Enter Faculty ID: "))
    name = input("Enter Faculty Name: ")
    department = input("Enter Faculty Department: ")
    sql = "INSERT INTO Faculty (FacultyID, Name, Department) VALUES (%s, %s, %s)"
    val = (sid, name, department)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Record inserted successfully")


def display_facultys():
    cursor.execute("SELECT * FROM Faculty")
    for row in cursor.fetchall():
        print(row)


def update_faculty():
    sid = int(input("Enter Faculty ID: "))
    name = input("Enter Faculty Name: ")
    department = input("Enter Faculty Department: ")
    sql = """
    UPDATE Faculty
    SET Name = %s, Department = %s
    WHERE FacultyID = %s
    """
    cursor.execute(sql, (name, department, sid))
    mydb.commit()
    print("Record Updated!" if cursor.rowcount else "Record Not Found")


def delete_faculty():
    sid = int(input("Enter Faculty ID: "))
    sql = "DELETE FROM Faculty WHERE FacultyID = %s"
    cursor.execute(sql, (sid,))
    mydb.commit()
    print("Record Deleted!" if cursor.rowcount else "Record Not Found")


while True:
    print("\n1.Insert Student")
    print("2.Insert Faculty")
    print("3.Display Students")
    print("4 Display Facultys")
    print("5.Update Student")
    print("6.Update Faculty")
    print("7.Delete Student")
    print("8.Delete Faculty")
    print("9.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        insert_student()
    elif choice == 2:
        insert_faculty()
    elif choice == 3:
        display_students()
    elif choice == 4:
        display_facultys()
    elif choice == 5:
        update_student()
    elif choice == 6:
        update_faculty()
    elif choice == 7:
        delete_student()
    elif choice == 8:
        delete_faculty()
    elif choice == 9:
        break
    else:
        print("Invalid Choice")
    cursor.close()
    mydb.close()
    print("Database connection closed")



