#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

"""
INSTRUCTIONS:

Your trio MISSION: Write a simple Python script to import CSV data into a relational database.

Read data from CSV files, and create a database whose table structure mimics that of the CSV files.
(In the care package you will find a CSV file of students and their IDs, and another linking said IDs to the students’ 
current grades in some courses. Desire more lulz? Add extra, more expansive CSVs.)
"""

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#Creates table and executes
db.execute("DROP TABLE if exists students")
db.execute("DROP TABLE if exists courses")
createCourses = "CREATE TABLE if not exists courses (code STRING, mark INTEGER, id INTEGER);"
c.execute(createCourses)
createStudents = "CREATE TABLE if not exists students (name STRING, age INTEGER, id INTEGER);"
c.execute(createStudents)

print("----COURSES TABLE----")

with open('courses.csv') as f:
    r = csv.DictReader(f) #Maps data to dictionary r
    for row in r:
        insertCourses = f"INSERT INTO courses VALUES('{row['code']}', {row['mark']}, {row['id']});"
        c.execute(insertCourses) #Inserts data into table for each row

with open('students.csv') as f:
    r = csv.DictReader(f) #Maps data to dictionary r
    for row in r: 
        insertStudents = f"INSERT INTO students VALUES('{row['name']}', {row['age']}, {row['id']});"
        c.execute(insertStudents) #Inserts data into table for each row

#Fetch all rows from ONE data table
c.execute('SELECT * from courses;') #query
for i in c.fetchall(): #
    print(i) #Prints out each data 
    
print("----STUDENTS TABLE----")

c.execute('SELECT * from students;') #query
for i in c.fetchall():
    print(i) #Prints out each data 

# for i in range(len(students)):
#     c.execute(f"INSERT INTO students VALUES (students['name'][{i}], students['age'][{i}], students['id'][{i}]);")

# for i in range(len(courses)):
#     c.execute(f"INSERT INTO students VALUES (courses['code'][{i}], courses['mark'][{i}], courses['id'][{i}]);")

#==========================================================

db.commit() #save changes
db.close()  #close database


