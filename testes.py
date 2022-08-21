import mysql.connector

mydb = mysql.connector.connect(
    host="relational.fit.cvut.cz",
    user="guest",
    password="relational",
    database="northwind"
)

i = 1
mycursor = mydb.cursor()

mycursor.execute(f'SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "Customers" and table_schema = "northwind"')
myresult = [i]
myresult = mycursor.fetchall()

for registro in myresult:
    print(i, "- " f'{registro[0]}')
    
    i = i + 1
   