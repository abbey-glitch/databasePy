import mysql.connector
db_con = mysql.connector.connect(
    host = 'localhost',
    user = "root",
    password = '',
    database = 'management_db'
)

cursor = db_con.cursor()
if(cursor):
    id = 12
    age = 34
    fname = 'joh'
    Sname = "sam"
    mysql_insert_query=f"""
                   INSERT INTO `student` VALUES (%s, %s, %s, %s)
                   """
    record = (id, fname, age, Sname)
    cursor.execute(mysql_insert_query, record)
    db_con.commit()
    print("column field")
else:
    print("could not insert into table")