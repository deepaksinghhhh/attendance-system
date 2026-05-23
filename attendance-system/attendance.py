import mysql.connector
from datetime import date

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="attendance_db"
)
cursor = conn.cursor()

def add_student():
    name = input("Student ka naam: ")
    roll_no = input("Roll Number: ")
    cursor.execute("INSERT INTO students (name, roll_no) VALUES (%s, %s)", (name, roll_no))
    conn.commit()
    print("✅ Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("No students found!")
        return
    print("\n--- Students List ---")
    print(f"{'ID':<5} {'Name':<20} {'Roll No'}")
    print("-" * 35)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<20} {row[2]}")

def mark_attendance():
    view_students()
    student_id = int(input("\nStudent ID daalo: "))
    status = input("Status (Present/Absent): ")
    today = date.today()
    cursor.execute("INSERT INTO attendance (student_id, date, status) VALUES (%s, %s, %s)",
                   (student_id, today, status))
    conn.commit()
    print("✅ Attendance marked!")

def view_attendance():
    cursor.execute("""
        SELECT s.name, s.roll_no, a.date, a.status 
        FROM attendance a 
        JOIN students s ON a.student_id = s.id
        ORDER BY a.date DESC
    """)
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("No attendance records found!")
        return
    print("\n--- Attendance Records ---")
    print(f"{'Name':<20} {'Roll No':<12} {'Date':<15} {'Status'}")
    print("-" * 55)
    for row in rows:
        print(f"{row[0]:<20} {row[1]:<12} {str(row[2]):<15} {row[3]}")

def view_report():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("\n--- Attendance Report ---")
    print(f"{'Name':<20} {'Present':<10} {'Absent':<10} {'Total'}")
    print("-" * 50)
    for s in students:
        cursor.execute("SELECT COUNT(*) FROM attendance WHERE student_id=%s AND status='Present'", (s[0],))
        present = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM attendance WHERE student_id=%s AND status='Absent'", (s[0],))
        absent = cursor.fetchone()[0]
        print(f"{s[1]:<20} {present:<10} {absent:<10} {present+absent}")

while True:
    print("\n===== Attendance System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. View Attendance Records")
    print("5. View Report")
    print("6. Exit")

    choice = input("Choose (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        mark_attendance()
    elif choice == "4":
        view_attendance()
    elif choice == "5":
        view_report()
    elif choice == "6":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice!")