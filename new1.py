import mysql.connector

em = mysql.connector.connect(
    host="localhost",
    user="Adithyas", 
    password="Adithya@123",  
    database="mydatabase"  
)

cursor = em.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS details(
        emp_id INT PRIMARY KEY,
        position VARCHAR(100),
        address VARCHAR(100)
    )
''')




while True:
    print('\n1.add\n2.view all\n3.left join\n4.right join\n5.cross join')
    ch = int(input('enter your choice: '))
    if ch == 1:
        l= int (input("Enter limit : "))
        for i in range(l):
            id = int(input('enter employee id: '))
            pos = input('enter position: ')
            add=input('enter the address:')
            cursor.execute('INSERT INTO details (emp_id, position,address) VALUES (%s, %s, %s)',
                        (id,pos,add))
            em.commit()
    elif ch==2:
         cursor.execute('''
            SELECT employe.emp_id, employe.name, employe.age, employe.email, employe.position, employe.salary,
                   details.emp_id, details.position, details.address
            FROM employe
            INNER JOIN details ON employe.emp_id = details.emp_id
        ''')
         data=cursor.fetchall()
         for i in data:
             print(i)
    elif ch==3:
        cursor.execute('''
            SELECT employe.emp_id, employe.name, employe.age, employe.email, employe.position, employe.salary,
                   details.emp_id, details.position, details.address
            FROM employe
            Left JOIN details ON employe.emp_id = details.emp_id
        ''')
        data=cursor.fetchall()
        for i in data:
             print(i)
    elif ch==4:
         cursor.execute('''
            SELECT employe.emp_id, employe.name, employe.age, employe.email, employe.position, employe.salary,
                   details.emp_id, details.position, details.address
            FROM details left join employe ON employe.emp_id = details.emp_id
        ''')
         data=cursor.fetchall()
         for i in data:
             print(i)
    elif ch==5:
        cursor.execute('''
            SELECT employe.emp_id, employe.name, employe.age, employe.email, employe.position, employe.salary,
                   details.emp_id, details.position, details.address
            FROM employe cross join details 
        ''')
        data=cursor.fetchall()
        for i in data:
             print(i)


    else:
        print("invalid choice")

    # cursor.close()