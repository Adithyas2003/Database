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
    

    elif ch == '2':
        name_to_update = input("Enter name of staff member to update: ")
        new_salary = float(input("Enter new salary: "))

        update_query = """
            UPDATE staff 
            SET salary = ?
            WHERE name = ?
        """
        con.execute(update_query, (new_salary, name_to_update))
        con.commit()
        print("Staff updated successfully.")
    elif ch == '3':
        con.execute('SELECT * FROM employees')
        employees = con.fetchall()
        for employee in employees:
            print(f"ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}, Salary: {employee[3]}")

    elif ch == '4':
        emp_id = int(input("Enter employee ID to delete: "))
        con.execute('DELETE FROM employees WHERE id = ?', (emp_id,))
        con.commit()
        print("Employee deleted successfully.")

    elif ch == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")

    





      