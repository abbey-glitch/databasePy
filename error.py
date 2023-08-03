# import mysql.connector
# from mysql.connector import Error

# try:
#     db_con = mysql.connector.connect(
#        host = 'localhost',
#        user = 'root',
#        password = '',
#     )
#     cursor = db_con.cursor()
#     if db_con.is_connected():
#         cursor.execute("DROP DATABASE `admin_db`")
#         print("connected success")
# except Error as e:
#     print(e)
for i in range(2, 3):
    print(i)