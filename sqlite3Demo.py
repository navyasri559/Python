import sqlite3
con=sqlite3.connect("mydatabase.db")
cur=con.cursor()
cur.execute("create table if not exists students(name varchar(50),email varchar(50),password varchar(50))")
'''x=cur.execute("show tables")
cur.execute('insert into students values("joe","sd@12","1234")')
cur.execute('insert into students values("jack","sd@21","2345")')
cur.execute('insert into students values("lisa","sd@13","3456")')
cur.execute('delete from students where name="lisa"')'''
cur.execute('update students set name="mona" where password=" 2345"')
x=cur.execute('select *from students')
print(x.fetchall())
con.commit()
print(x)