import sqlite3
con=sqlite3.connect("employee1.db")
try:
    con.execute("create table staff(name text,position text,age int, salary real) ")
except:
       pass
while True:
    print("1.add")
    print("2.update")
    print("3.display")
    print("4.search")
    print("5.delete")
    ch=input("enter your choice")
    if ch=='1':
         name=input("enter name:")
         position=input("enter position:")
         age=int(input("enter the age:"))
         salary=float(input("enter the salary:"))
         con.execute("insert into staff(name,position,age,salary)values('kiran','HR',28,30000)")
         con.commit()
         print("Employee Added Successfully")
    elif ch=='2':
         name=input("enter the name:")


      