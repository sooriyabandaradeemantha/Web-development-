import sqlite3

# Create/connect to database

conn = sqlite3.connect("database.sqlite")

cursor = conn.cursor()

# Create table

cursor.execute("""

CREATE TABLE IF NOT EXISTS students (

id INTEGER PRIMARY KEY,

name TEXT,

age INTEGER,

course TEXT

)

""")

# Insert sample data

cursor.executemany("""

INSERT INTO students (name, age, course)

VALUES (?, ?, ?)

""", [

("Gurpreet Singh", 22, "Computer Science"),

("Nisha Dhaliwal", 21, "Data Science"),

("Karan Singh", 23, "Artificial Intelligence")

])

# Save changes

conn.commit()

# Read data from table

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

# Display data

print("\nStudents Table:")

print("ID\tName\t\t\tAge\tCourse")

print("-" * 60)

for row in rows:

    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")

# Close connection

conn.close()

print("\ndatabase.sqlite created successfully!")