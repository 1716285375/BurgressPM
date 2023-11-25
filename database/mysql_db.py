import pymysql
import re
from PySide6.QtCore import QUuid


class SQL:
    def __init__(self):
        count = None

    @staticmethod
    def connect_sql():
        conn = pymysql.connect(
            host='120.26.55.56',
            port=3306,
            user='remote',
            password='12345678',
            charset='utf8mb4'
        )
    # print(conn.get_server_info())
        return conn

    @staticmethod
    def verify_login(username, password):
        conn = SQL.connect_sql()
        print(conn)
        conn.select_db("user_information")
        cursor = conn.cursor()

# command = ("create table user_information(usrid varchar(255) primary key not null,"
#            "username varchar(128) not null, password varchar(255) not null )")
# cursor.execute(command)
#         query = 'username = {} and password = {}'.format(username, password)

        sql = "SELECT username, password FROM users_log WHERE username = %s and password = %s"
        data = (username, password)
        cursor.execute(sql, data)
        result = cursor.fetchone()
        # print(result)
        return result

    @staticmethod
    def creat_table():
        conn = SQL.connect_sql()
        print(conn)
        conn.select_db("user_information")
        cursor = conn.cursor()
        command = '''
    CREATE TABLE IF NOT EXISTS users_log (
        id VARCHAR(255) PRIMARY KEY,
        username VARCHAR(128) NOT NULL UNIQUE ,
        password VARCHAR(255) NOT NULL 
    )
    '''
        cursor.execute(command)
        conn.commit()
        cursor.close()

    @staticmethod
    def insert_values(ids, username, password):
        conn = SQL.connect_sql()
        print(conn)
        conn.select_db("user_information")
        cursor = conn.cursor()
        # pattern = r"[{}-]"
        # ids = re.sub(pattern, r"", QUuid.createUuid().toString())
        # print(ids)
        # username = '12345645'
        # password = '123'
        sql = "INSERT INTO users_log (id, username, password) VALUES (%s, %s, %s)"
        data = (ids, username, password)
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()


if __name__ == '__main__':
    # SQL().creat_table()
    # SQL().insert_values()
    SQL.verify_login()
