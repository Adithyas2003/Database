import mysql.connector

emp = mysql.connector.connect(
    host="localhost",
    user="Adithyas", 
    password="Adithya@123",  
    database="mydatabase"  
)

cursor = emp.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee (
        emp_id INT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        email VARCHAR(100),
        position VARCHAR(100)
    )
''')

while True:
    print('\n1.add\n2.update\n3.delete\n4.search\n5.view all')
    ch = int(input('enter your choice: '))
    if ch == 1:
        id = int(input('enter employee id: '))
        name = input('enter your name: ')
        age = int(input('enter your age: '))
        email = input('enter your email: ')
        pos = input('enter position: ')
        cursor.execute('INSERT INTO employee (emp_id, name, age, email, position) VALUES (%s, %s, %s, %s, %s)',
                       (id, name, age, email, pos))
        emp.commit()
    elif ch == 2:
        id = int(input('enter id of employee: '))
        name = input('enter your new name: ')
        age = int(input('enter your new age: '))
        email = input('enter your new email: ')
        pos = input('enter new position: ')
        cursor.execute('UPDATE employee SET name=%s, age=%s, email=%s, position=%s WHERE emp_id=%s',
                       (name, age, email, pos, id))
        emp.commit()
    elif ch == 3:
        id = int(input('enter id of employee to delete: '))
        cursor.execute('DELETE FROM employee WHERE emp_id=%s', (id,))
        emp.commit()
    elif ch == 4:
        id = int(input('enter id to search: '))
        cursor.execute('SELECT * FROM employee WHERE emp_id=%s', (id,))
        data = cursor.fetchall()
        print('{:<10}{:<10}{:<10}{:<20}{:<10}'.format('id', 'name', 'age', 'email', 'position'))
        print('-' * 60)
        if data:
            for i in data:
                print("{:<10}{:<10}{:<10}{:<20}{:<10}".format(i[0], i[1], i[2], i[3], i[4]))
        else:
            print('id not available')
    elif ch == 5:
        cursor.execute('SELECT * FROM employee')
        data = cursor.fetchall()
        print('{:<10}{:<10}{:<10}{:<20}{:<10}'.format('id', 'name', 'age', 'email', 'position'))
        print('-' * 60)
        for i in data:
            print("{:<10}{:<10}{:<10}{:<20}{:<10}".format(i[0], i[1], i[2], i[3], i[4]))
    else:
        print('invalid choice.....')