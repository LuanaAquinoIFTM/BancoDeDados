import mysql.connector

mydb = mysql.connector.connect(
    host="relational.fit.cvut.cz",
    user="guest",
    password="relational",
    database="northwind"
)

cont = 1
mycursor = mydb.cursor()

mycursor.execute(f'SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = "BASE TABLE" AND TABLE_SCHEMA="northwind"')
myresult = []
myresult = mycursor.fetchall()

print("-------------------------TABELAS--------------------------")
for registro in myresult:
    
    print("|", cont, "- " f'{registro[0]} ')
    
    cont = cont + 1
print("----------------------------------------------------------")