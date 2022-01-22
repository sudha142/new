import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Sudha142@python")
cur=con.cursor()
cur.execute("create database mydatabase")
cur.execute("show databases")
for i in cur:
    print(i)
print("database is created")
con.close()