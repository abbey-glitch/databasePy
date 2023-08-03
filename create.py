import mysql.connector

db_conn = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = '',
    database = 'management_db'         
)

cursor = db_conn.cursor()
if(cursor):
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS `student`(
                   `id` INT PRIMARY KEY AUTO_INCREMENT,
                   `fname` VARCHAR(50),
                   `age` INT(20),
                   `surname` VARCHAR(50)
                   )
                   """)
else:
    print("could not create table")