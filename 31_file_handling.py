# Topic: Writing, reading, appending, and managing files

# Writing to a file
with open("students.txt", "w") as file:
    file.write("Name,Grade\n")
    file.write("Alice,A\n")
    file.write("Bob,B\n")

# Reading from a file
with open("students.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to a file
with open("students.txt", "a") as file:
    file.write("Charlie,A\n")

# Real-world example: Attendance system
from datetime import datetime

def record_attendance(student_name, present=True):
    status = "Present" if present else "Absent"
    with open("attendance.txt", "a") as file:
        file.write(f"{student_name},{status},{datetime.now().date()}\n")

def read_attendance():
    with open("attendance.txt", "r") as file:
        return [line.strip().split(",") for line in file.readlines()]

record_attendance("Alice")
record_attendance("Bob", False)
attendance_data = read_attendance()
for record in attendance_data:
    print(f"{record[0]}: {record[1]} on {record[2]}")
