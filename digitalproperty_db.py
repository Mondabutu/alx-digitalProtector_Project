import mysql.connector
dataBase=mysql.connector.connect(
    host = 'localhost',
    user ='root',
    passwd=''
)
cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE mydigitalproperty_db")
print("Database Created Successfully")