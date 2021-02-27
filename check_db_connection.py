import pymysql.cursors


connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="admin", password="password")

try:
    cursor = connection.cursor()
    p = cursor.execute("SELECT * FROM group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()