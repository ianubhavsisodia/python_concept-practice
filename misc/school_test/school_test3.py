# to accept user input for the values to create new record
import sqlite3
MySchool=sqlite3.connect('schooltest.db')
curschool=MySchool.cursor()

# to accept user input, create varibale object to store each value
mysid= int(input("Enter Student ID: "))
myname= input("Enter name: ")
myhouse= input("Enter house: ")
mymarks= float(input("Enter marks: "))

#to insert data into database table using cursor method execute function
curschool.execute("""INSERT INTO students (StudentID, name, house, marks)
VALUES (?,?,?,?); """, (mysid, myname, myhouse, mymarks))

MySchool.commit()

#to retrieve next available data 
sql = "SELECT * from students;"
curschool=MySchool.cursor()
curschool.execute(sql)
while True:
    record= curschool.fetchone()
    if record==None:
        break
    print(record)

#to retrieve all records and print them one at a time

sql="SELECT * from students;"
            
curschool=MySchool.cursor()
curschool.execute(sql)
    
result=curschool.fetchall()
for record in result:
    print (record)


# to update a record

#take input of the name
nm = input("Enter name ")
#creating a string of select query to fetch the record
sql="SELECT * from students WHERE name='"+nm+"';"
#executing query
curschool=MySchool.cursor()
curschool.execute(sql)
record=curschool.fetchone()
print(record)

m= float(input("Enter new marks:"))
sql="UPDATE students SET marks='"+str(m)+"'WHERE name='"+nm+"';"
try:
    curschool.execute(sql)
    MySchool.commit()
    print("record updated successfully")
except:
    print ("Error updating record")
    MySchool.rollback()


## to delete a record 
#take input for student's name which needs deletion
nm=input("Enter name: ")
sql="SELECT * from students WHERE name='"+nm+"';"
#executing query
curschool=MySchool.cursor()
curschool.execute(sql)
record=curschool.fetchone()
print(record)

#ddeleting the retrieved record
res = input("Do you want to delete this record? (Y/N)")
sql = "DELETE from students WHERE name='"+nm+"';"
if res=='Y':
    try:
        curschool.execute(sql)
        MySchool.commit()
        print('Record deleted successfully')
    except:
        print ("error in deleting ")
        MySchool.rollback()
        