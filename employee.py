# import sqlite3
# con=sqlite3.connect("employee.db")
# try:
#     con.execute("create table staff(id int,name text,position text,age int, salary real)")
# except:
#        pass
# while True:
#     print("1.add")
#     print("2.update")
#     print("3.display")
#     print("4.search")
#     print("5.delete")
#     ch=input("enter your choice:")
#     if ch=='1':
#          id=int(input("enter id:"))
#          name=input("enter name:")
#          position=input("enter position:")
#          age=int(input("enter the age:"))
#          salary=float(input("enter the salary:"))
#          con.execute("insert into staff(id,name,position,age,salary)values(?,?,?,?,?)",(id,name,position,age,salary))
#          con.commit()
#          print("staff Added Successfully")
    

#     elif ch == '2':
#         name_to_update = input("Enter name of staff member to update: ")
#         new_salary = float(input("Enter new salary: "))

#         update_query = """
#             UPDATE staff 
#             SET salary = ?
#             WHERE name = ?
#         """
#         con.execute(update_query, (new_salary, name_to_update))
#         con.commit()
#         print("Staff updated successfully.")
#     elif ch == '3':
#        a=con.execute('SELECT * FROM staff')
#        staff = con.fetchall()
#        for staff in a:
#             print(f"ID: {staff[0]}, Name: {staff[1]}, Position: {staff[2]}, Salary: {staff[3]}")

#     elif ch == '4':
#         emp_id = int(input("Enter staff ID to delete: "))
#         con.execute('DELETE FROM staff WHERE id = ?', (emp_id,))
#         con.commit()
#         print("staff deleted successfully.")

#     elif ch == '5':
#         print("Exiting...")
#         break

#     else:
#         print("Invalid choice. Please try again.")

    
import sqlite3

con = sqlite3.connect("employee.db")
try:
    con.execute("CREATE TABLE IF NOT EXISTS staff (id INT, name TEXT, position TEXT, age INT, salary REAL)")
except Exception as e:
    print(e)

while True:
    print("\n1. Add")
    print("2. Update")
    print("3. Display")
    print("4. Search")
    print("5. Delete")
    print("6. Exit")
    ch = input("Enter your choice: ")

    if ch == '1':
        id = int(input("Enter id: "))
        name = input("Enter name: ")
        position = input("Enter position: ")
        age = int(input("Enter age: "))
        salary = float(input("Enter salary: "))
        
        con.execute("INSERT INTO staff (id, name, position, age, salary) VALUES (?, ?, ?, ?, ?)", (id, name, position, age, salary))
        con.commit()
        print("Staff added successfully.")

    elif ch == '2':
        name_to_update = input("Enter name of staff member to update: ")
        new_salary = float(input("Enter new salary: "))
        
        update_query = "UPDATE staff SET salary = ? WHERE name = ?"
        con.execute(update_query, (new_salary, name_to_update))
        con.commit()
        print("Staff updated successfully.")

    elif ch == '3':
        try:
            cursor = con.execute("SELECT * FROM staff")
            rows = cursor.fetchall()
            if len(rows) == 0:
                print("No staff records found.")
            else:
                for row in rows:
                    print(f"ID: {row[0]}, Name: {row[1]}, Position: {row[2]}, Age: {row[3]}, Salary: {row[4]}")
        except Exception as e:
            print(e)

    elif ch == '4':
        name_to_search = input("Enter name of staff member to search: ")
        search_query = "SELECT * FROM staff WHERE name = ?"
        cursor = con.execute(search_query, (name_to_search,))
        rows = cursor.fetchall()
        if len(rows) == 0:
            print("No staff records found.")
        else:
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Position: {row[2]}, Age: {row[3]}, Salary: {row[4]}")

    elif ch == '5':
        emp_id = int(input("Enter staff ID to delete: "))
        con.execute("DELETE FROM staff WHERE id = ?", (emp_id,))
        con.commit()
        print("Staff deleted successfully.")

    elif ch == '6':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")





      