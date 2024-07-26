import sqlite3
con=sqlite3.connect("new.db")
try:
    con.execute("create table details(name text,place text,con_no int,address text)")
except:
    pass

# name=str(input("name:"))
# place=str(input("place:"))
# con_no=int(input("con_no:"))
# address=str(input("address:"))
# con.execute("insert into details(name,place,con_no,address)values(?,?,?,?)",(name,place,con_no,address))
# con.commit()

#innerjoin:

# a=con.execute("select student.name,student.age,student.mark,details.place,details.con_no,details.address from student inner join details on student.name==details.name")
# for i in a:
#     print(i)

#leftjoin:

# a=con.execute("select student.name,student.age,student.mark,details.place,details.con_no,details.address from student left join details on student.name==details.name")
# for i in a:
#     print(i)

#rightjoin:


# a=con.execute("select student.name,student.age,student.mark,details.place,details.con_no,details.address from details left join student on student.name==details.name")
# for i in a:
#     print(i)

#closed join:


a=con.execute("select student.name,student.age,student.mark,details.place,details.con_no,details.address from student cross join details")
for i in a:
    print(i)