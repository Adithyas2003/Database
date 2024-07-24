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



# b=con.execute("select * from student")
# print("{:<10}{:<16}{:<10}".format('name','age','mark'))
# for i in b:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))


#user input:


# name=str(input("name"))
# d=con.execute("select * from student where name=?",(name,))
# print("{:<10}{:<16}{:<10}".format('name','age','mark'))
# for i in d:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))


#Direct:

# a=con.execute("select * from student where age=11")
# print("{:<10}{:<16}{:<10}".format('name','age','mark'))
# for i in a:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))

#user input of age:


# age=int(input("age"))
# d=con.execute("select * from student where age=?",(age,))
# print("{:<10}{:<16}{:<10}".format('name','age','mark'))
# for i in d:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))



# d=con.execute("select * from student where age>=12")
# print("{:<10}{:<16}{:<10}".format('name','age','mark'))
# for i in d:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))


# d=con.execute("select * from student where mark<=25")
# print("{:<10}{:<16}{:<10}".format('name','age','mark'))
# for i in d:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))


#update:


# d=con.execute("update student set name='anju'where name='anu'")
# con.commit()
# d=con.execute("select * from student")
# print("{:<10}{:<16}{:<10}".format('name','age','mark'))
# for i in d:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))


# update age:

# a=con.execute("update student set age=23 where age=22")
# con.commit()
# a=con.execute("select * from student")
# print("{:<10}{:<16}{:<10}".format('name','age','mark'))
# for i in a:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))


# a=con.execute("update student set age=23 where age=22")
# con.commit()
# a=con.execute("select * from student")
# print("{:<10}{:<16}".format('name:','age:',))
# for i in a:
#     print("{:<10}{:<16}".format(i[0],i[1]))


#delete:

# a=con.execute("delete from student where  name='anju'")
# con.commit()
# a=con.execute("select * from student")
# print("{:<10}{:<16}{:<10}".format('name','age','mark'))
# for i in a:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))

name=str(input("name"))
a=con.execute("delete from student where  name='appu'")
con.commit()
a=con.execute("select * from student where name=?",(name,))
print("{:<10}{:<16}{:<10}".format('name','age','mark'))
for i in a:
    print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))




