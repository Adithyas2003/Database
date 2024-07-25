import sqlite3
con=sqlite3.connect("employee.db")
try:
    con.execute("create table staff(id int,name text,position text,age int, salary real)")
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
         id=int(input("enter id:"))
         name=input("enter name:")
         position=input("enter position:")
         age=int(input("enter the age:"))
         salary=float(input("enter the salary:"))
         con.execute("insert into staff(id,name,position,age,salary)values(?,?,?,?,?)",(id,name,position,age,salary))
         con.commit()
         print("staff Added Successfully")
    elif ch=='2':
        update_name=str(input("enter the staff name to update"))
        con.execute("select * from staff")
        condition_age = 30
        update_salary = 70000.0
        con.execute("UPDATE staff SET  salary=? WHERE age=?", (update_name,update_salary))
        con.commit()
        print("staff updated successfully")



    





      