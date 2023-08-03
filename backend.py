import mysql.connector

db_con = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password = ''
)

cursor = db_con.cursor()
if(cursor):
    cursor.execute("SHOW DATABASES")
    for db in cursor:
        print(db)