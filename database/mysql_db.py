import pymysql
import re
from PySide6.QtCore import QUuid


# table
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
            # charset='utf8mb4'
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
        conn.commit()
        result = cursor.fetchone()
        cursor.close()
        # print(result)
        return result

    @staticmethod
    def creat_table(table_name):
        conn = SQL.connect_sql()
        print(conn)
        conn.select_db("user_information")
        cursor = conn.cursor()
        command = '''
    CREATE TABLE IF NOT EXISTS {} (
        id VARCHAR(255) PRIMARY KEY,
        username VARCHAR(128) NOT NULL UNIQUE ,
        password VARCHAR(255) NOT NULL 
    )
    '''.format(table_name)
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

    @staticmethod
    def search_values():
        conn = SQL.connect_sql()
        print(conn)
        conn.select_db("user_information")
        cursor = conn.cursor()
        sql = "SELECT * FROM user_info"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @staticmethod
    def get_currentItem_table(table_name=None):
        try:
            print(table_name)
            conn = SQL.connect_sql()
            conn.select_db("user_information")
            print(conn)
            cursor = conn.cursor()
            sql = "SELECT * FROM {};".format(table_name)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except pymysql.err.ProgrammingError:
            print('error')


# if __name__ == '__main__':
    # SQL().creat_table()
    # SQL().insert_values()
    # SQL.verify_login()
