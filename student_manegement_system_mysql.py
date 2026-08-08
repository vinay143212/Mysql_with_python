import mysql.connector

def connect_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vinay@2005",
        database="student_management"
    )
    return conn

conn = connect_database()
cursor = conn.cursor()
print("DATABASE CONNECTED SUCCESSFULLY")

class Student:
    def __init__(self,student_id,name,age,course,branch, marks,):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.course=course
        self.branch=branch
        self.marks=marks



print("===== STUDENT MANAGEMENT SYSTEM =====")

choice = ""
students=[]


while choice != "6":
    print("1.Add student")
    print("2.View students")
    print("3.Search student")
    print("4.Update student")
    print("5.Delete student")
    print("6.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id=int(input("enter the student id : "))
        name=input("enter the student name : ")
        age=int(input("enter the student age :"))
        course=input("enter the course: ")
        branch=input("enter the branch: ")
        marks=int(input("enter the student marks:"))
        student=Student(student_id,name,age,course,branch,marks)
        # Code to add student
        print("===STUDENT ADDED===")

        sql ="""INSERT INTO students (student_id, name, age, course, branch, marks)
        VALUES (%s, %s, %s, %s, %s, %s)"""
        values = (
            student.student_id,
            student.name,
            student.age,
            student.course,
            student.branch,
            student.marks
        )
        cursor.execute(sql, values)
        conn.commit()
        print("student added successfully to the database")
    elif choice == "2":
        print("==== STUDENT DETAILS===")

        sql = "SELECT * FROM students"
        cursor.execute(sql)
        records = cursor.fetchall()
        print("------------------------------")
        for student in records:
            print("student_id : ", student[0])               
            print("name : ", student[1])   
            print("age : ", student[2])
            print("course : ", student[3])
            print("branch: ", student[4])
            print("marks : ", student[5])
            print("------------------------------")

    elif choice == "3":
        # Code to search student
        print("search student selected")
        student_id = int(input("enter the student id to search:"))

        sql = "SELECT * FROM students WHERE student_id = %s"
        cursor.execute(sql,(student_id,))
        record = cursor.fetchone()

        if record:
            print("student found:")
            print("student_id : ", record[0])
            print("name : ", record[1])
            print("age : ", record[2])
            print("course : ", record[3])
            print("branch: ", record[4])
            print("marks : ", record[5])
        else:

            print("not found")
    elif choice == "4":
        print("=== UPDATE STUDENT ===")

        student_id = int(input("Enter the student ID to update: "))

        # Check whether student exists in database
        sql = "SELECT * FROM students WHERE student_id = %s"
        cursor.execute(sql, (student_id,))
        student_data = cursor.fetchone()

        if student_data is None:
            print("Student not found")
        else:
            print("Update student selected")
            print("1. Update name")
            print("2. Update age")
            print("3. Update course")
            print("4. Update branch")
            print("5. Update marks")

            update_choice = input("Enter your choice: ")

            if update_choice == "1":
                new_name = input("Enter the new name: ")

                sql = "UPDATE students SET name = %s WHERE student_id = %s"
                cursor.execute(sql, (new_name, student_id))
                conn.commit()

                print("Name updated successfully")

            elif update_choice == "2":
                new_age = int(input("Enter the new age: "))

                sql = "UPDATE students SET age = %s WHERE student_id = %s"
                cursor.execute(sql, (new_age, student_id))
                conn.commit()

                print("Age updated successfully")

            elif update_choice == "3":
                new_course = input("Enter the new course: ")

                sql = "UPDATE students SET course = %s WHERE student_id = %s"
                cursor.execute(sql, (new_course, student_id))
                conn.commit()

                print("Course updated successfully")

            elif update_choice == "4":
                new_branch = input("Enter the new branch: ")

                sql = "UPDATE students SET branch = %s WHERE student_id = %s"
                cursor.execute(sql, (new_branch, student_id))
                conn.commit()

                print("Branch updated successfully")

            elif update_choice == "5":
                new_marks = int(input("Enter the new marks: "))

                sql = "UPDATE students SET marks = %s WHERE student_id = %s"
                cursor.execute(sql, (new_marks, student_id))
                conn.commit()

                print("Marks updated successfully")

            else:
                print("Invalid choice")
           
    elif choice == "5":
        print("=== DELETE STUDENT ===")
        student_id = int(input("enter the student id to delete:"))
        sql = "DELETE FROM students WHERE student_id = %s"
        cursor.execute(sql, (student_id,))
        conn.commit()
        if cursor.rowcount > 0:
                    for student in students:
                         if student.student_id == student_id:

                            students.remove(student)
                            break

                            print("student deleted successfully")
                
                         else:
                            print("student not found")
        # Code to delete student
    elif choice == "6":
        cursor.close()
        conn.close()
        # Code to exit
        print("thankyou for using the student management system!")
    else:
        print("Invalid choice. Please try again.")