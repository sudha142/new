import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Sudha142@python",database="profesion")
cur=con.cursor()
qury="insert into person(pid,pname,location)values(%s,%s,%s)"
val=[(102,"rani","mahb"),(103,"shanthi","varikuntla"),(104,"amrutha","vizag")]
cur.executemany(qury,val)
con.commit()
for i in cur:
    print(i)
print("data is inserted")
con.close()
