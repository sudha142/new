import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Sudha142@python",database="profesion")
cur=con.cursor()
cur.execute("create table person(pid int,pname varchar(100),location varchar(50))")
print("table is created")
for i in cur:
    print(i)
con.close()

