import mysql.connector
from mysql.connector import cursor

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""

)
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE StudentDB")
print("Database created successfully")
mydb.close()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
StudentID INT PRIMARY KEY,
Name VARCHAR(50),
Department VARCHAR(50),
)
""")
print("Student Table created successfully")

def insert_student():
    sid=int(input("Enter Student ID: "))
    name=input("Enter Student Name: ")
    department=input("Enter Student Department: ")
    sql="INSERT INTO Student (StudentID, Name, Department) VALUES (%s, %s, %s)"
    val=(sid,name,department)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Record inserted successfully")

def display_students():
    cursor.execute("SELECT * FROM Student")
    for row in cursor.fetchall():
        print(row)

def update_student():
    sid=int(input("Enter Student ID: "))
    name=input("Enter Student Name: ")
    department=input("Enter Student Department: ")
    sql="""
    UPDATE Student
    SET Name = %s, Department = %s
    WHERE StudentID = %s
    """
    cursor.execute(sql,(name,department,sid))
    mydb.commit()
    print("Record Updated!" if cursor.rowcount else "Record Not Found")

def delete_student():
    sid=int(input("Enter Student ID: "))
    sql= "DELETE FROM Student WHERE StudentID = %s"
    cursor.execute(sql,(sid,))
    mydb.commit()
    print("Record Deleted!" if cursor.rowcount else "Record Not Found")

    