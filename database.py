import mysql.connector
db_name = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = ''
)

cursor = db_name.cursor()
if(cursor):
    cursor.execute("CREATE DATABASE `management_db`")
    print("connected")
else:
    print("database Error")
