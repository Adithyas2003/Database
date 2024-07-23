import sqlite3
con=sqlite3.connect("new.db")
try:
    con.execute("create table student(age int, name text, mark real)")
except:
    pass
# con.execute("insert into student(age,name,mark)values(21,'abc',65)")
# con.commit()

# age=int(input("age"))
# name=str(input("name"))
# mark=float(input("mark"))
# con.execute("insert into student(age,name,mark)values(?,?,?)",(age,name,mark))
# con.commit()

#multiple vales:

# a=int(input("limit"))
# for i in range(a):
#     age=int(input("age"))
#     name=str(input("name"))
#     mark=float(input("mark"))
#     con.execute("insert into student(age,name,mark)values(?,?,?)",(age,name,mark))
#     con.commit()


# b=con.execute("select * from student")
# print(b)
# for i in b:
#     print(i)



b=con.execute("select * from student")
print("{:<10}{:<16}{:<10}".format('name','age','mark'))
for i in b:
    print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))









