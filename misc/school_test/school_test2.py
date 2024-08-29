#create a new record in the table 

import sqlite3
MySchool=sqlite3.connect("schooltest.db")
curschool=MySchool.cursor()
# curschool.execute("""INSERT INTO students (StudentID, Name, House, Marks) 
# VALUES (5, 'Sherlock', 'Slytherin', 65);""")
# # MySchool.commit()

curschool.execute("""INSERT INTO students (StudentID, Name, House, Marks) 
VALUES (6, 'Harry', 'Gryfindor', 68);""")
MySchool.commit()
