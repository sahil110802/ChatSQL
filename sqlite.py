import sqlite3


##connect to sqlite
connection=sqlite3.connect("student.db")

##create a cursor object to insert record, create table
cursor=connection.cursor()

##create the table
table_info="""
create table STUDENTS(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

##Insert some more records 
cursor.execute('''Insert Into STUDENTS values('Krish', 'Data Science', 'A', 90) ''')
cursor.execute('''Insert Into STUDENTS values('John', 'Data Science', 'B', 70) ''')
cursor.execute('''Insert Into STUDENTS values('Cena', 'DevOps', 'C', 50) ''')
cursor.execute('''Insert Into STUDENTS values('Ullu', 'DevOps', 'A', 90) ''')
cursor.execute('''Insert Into STUDENTS values('Paaji', 'Dev', 'B', 80) ''')



##Display all records
print("The inserted records are")
data=cursor.execute('''Select * from STUDENTS ''')
for row in data:
    print(row)

##Commit changes in DB
connection.commit()
connection.close()