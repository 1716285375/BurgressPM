import pymysql
import sqlalchemy as sql
import re
from PySide6.QtCore import QUuid
import pandas as pd
import random
from datetime import datetime, timedelta


def random_date():
    year = random.randint(2000, 2030)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime(year, month, day)


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
            charset='utf8mb4'
        )
    # print(conn.get_server_info())
        return conn

    # def update_login_info(self, Qid):
    #     try:
    #         conn = SQL.connect_sql()
    #         conn.select_db('users_login_information')
    #         cursor = conn.cursor()
    #         sql = "INSERT INTO users_log (qid, usr, pwd, name, address, sex) VALUES (%s, %s, %s, %s, %s, %s)"


class pdSqlalchemy:
    def __init__(self, table_name, file_name):
        self._engine = None
        self._table_name = table_name
        self._filename = file_name

    def pd_connect_sql(self):
        self._engine = sql.create_engine('mysql://remote:12345678@120.26.55.56/burgresspm_data?charset=utf8')
        print('connect')
        return self._engine

    def update_login_info(self):
        engine = self.pd_connect_sql()
        columns = ['qid', 'usr', 'pwd', 'name', 'address', 'sex']
        df = pd.read_excel(self._filename, sheet_name='Sheet1', header=0)
        df.columns = columns
        dtypes = {'qid': sql.String(255), 'usr': sql.String(45), 'pwd': sql.String(45),
                  'name': sql.String(128), 'address': sql.String(128),
                  'sex': sql.String(8)}
        df.to_sql(self._table_name, con=engine, if_exists='replace', index=False, dtype=dtypes)
        print('ok')

    def update_folder_info(self):
        engine = self.pd_connect_sql()
        df = pd.read_excel(self._filename, sheet_name='Sheet1', header=0)
        columns = ['usr', 'folder', 'url', 'username', 'password', 'note', 'createdate', 'like', 'trash']
        df.columns = columns
        random_dates = pd.Series([random_date() for _ in range(len(df))])
        df['createdate'] = random_dates
        dtypes = {'qid': sql.String(255),
                  'url': sql.String(255), 'folder': sql.String(128),
                  'username': sql.String(255), 'password': sql.String(255),
                  'note': sql.String(128), 'createdate': sql.DateTime, 'like': sql.Boolean
                  }
        df.to_sql(self._table_name, con=engine, if_exists='replace', index=False)
        print('ok')

    # def create_table_folder(self):
    #     engine = self.pd_connect_sql()


class pyMysql:
    def __init__(self, table_name=None, folder_name=None, qid=None, usr=None, pwd=None,
                 url=None, username=None, password=None, note=None, time=None, like=0, trash=0,
                 url_p=None, username_p=None, password_p=None, note_p=None, time_p=None, like_p=0, trash_p=0,
                 flag=True, model=True, foldercount=0):
        # 数据库信息
        self._table_name = table_name
        self._folder = folder_name
        # 用户信息
        self._qid = qid
        self._usr_name = usr
        self._usr_pwd = pwd
        # 账户信息
        self._url = url
        self._username = username
        self._password = password
        self._note = note
        self._time = time
        self._like = like
        self._trash = trash
        # previous
        self._url_p = url_p
        self._username_p = username_p
        self._password_p = password_p
        self._note_p = note_p
        self._time_p = time_p
        self._like_p = like_p
        self._trash_p = trash_p
        # 标志位
        self._flag = flag
        self._model = model
        self._foldercount = foldercount
        # 连接数据库
        self._conn = pymysql.connect(
            host='120.26.55.56',
            port=3306,
            user='remote',
            password='12345678',
            charset='utf8mb4'
        )
        self._database = "burgresspm_data"
        self._cursor = None

    # 创建数据库连接
    def create_connect(self):
        try:
            self._conn.select_db(self._database)
            self._cursor = self._conn.cursor()
            return 1
        except pymysql.Error as e:
            print(f"Error:{e.args[0]},{e.args[1]}")
            return 0

    # /*-----------------@BEGIN: folders@-------------------*/
    # 检索用户当前点击的folder对应的数据
    def search_by_folder(self):
        self.create_connect()
        try:
            sql_command = f"SELECT * FROM {self._table_name} WHERE usr = %s and folder = %s and trash=0"
            data = (self._usr_name, self._folder)
            self._cursor.execute(sql_command, data)
            self._conn.commit()
            result = self._cursor.fetchall()
            return result
        except pymysql.Error as e:
            print(f" search_by_folder Error:{e.args[0]},{e.args[1]}")
            return 0
        finally:
            self._cursor.close()

    # 给当前用户的folders_list添加folder
    def update_folders_list(self):
        self.create_connect()
        try:
            if self._flag:
                sql_command = f"INSERT INTO {self._table_name} (usr, folder) VALUES (%s, %s)"
            else:
                sql_command = f"DELETE FROM {self._table_name} WHERE usr = %s and folder = %s"
            data = (self._usr_name, self._folder)
            self._cursor.execute(sql_command, data)
            self._conn.commit()
        except pymysql.Error as e:
            self._conn.rollback()
            print(f"update_folders_list Error:{e.args[0]},{e.args[1]}")
            return 0
        finally:
            self._cursor.close()

    # 删除当前folder_list下的所有数据项
    def delete_folders_all_list(self):
        self.create_connect()
        try:
            sql_command = f"UPDATE {self._table_name} SET trash=1, `like`=0 WHERE usr = %s and folder = %s"
            data = (self._usr_name, self._folder)
            self._cursor.execute(sql_command, data)
            self._conn.commit()
            return 1
        except pymysql.Error as e:
            self._conn.rollback()
            print(f"update_folders_list_content Error:{e.args[0]},{e.args[1]}")
            return 0
        finally:
            self._cursor.close()

    # 编辑folder_list里面的数据项
    def update_folders_list_item(self):
        self.create_connect()
        try:
            if self._model:
                if self._flag:
                    sql_command = f'''INSERT INTO {self._table_name} (usr, folder, url, username, password, note, createdate) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s)'''
                    data = (self._usr_name, self._folder, self._url, self._username, self._password, self._note, self._time)
                    self._cursor.execute(sql_command, data)
                    self._conn.commit()
                else:
                    sql_command = f'''UPDATE {self._table_name} SET trash=1, `like`=0 WHERE usr=%s and folder=%s and url=%s
                                                                and username=%s and password=%s and note=%s 
                                                                and createdate=%s'''
                    data = (self._usr_name, self._folder,
                            self._url, self._username, self._password, self._note,
                            self._time)
                    self._cursor.execute(sql_command, data)
                    self._conn.commit()
            else:
                sql_command = f'''UPDATE {self._table_name} SET url=%s, username=%s, password=%s, note=%s, createdate=%s
                                    WHERE usr=%s and folder=%s and url=%s
                                                and username=%s and password=%s
                                                and note=%s and createdate=%s'''
                data = (self._url, self._username, self._password, self._note, self._time,
                        self._usr_name, self._folder, self._url_p, self._username_p, self._password_p,
                        self._note_p, self._time_p)
                self._cursor.execute(sql_command, data)
                self._conn.commit()
            return 1
        except pymysql.Error as e:
            self._conn.rollback()
            print(f"update_folders_list Error:{e.args[0]},{e.args[1]}")
            # print(type(self._trash), type(self._like))
            return 0
        finally:
            self._cursor.close()

    # 更新users_folders中的foldercount的数量
    def update_folders_count(self):
        self.create_connect()
        try:
            if self._flag:
                sql_command = f"UPDATE {self._table_name} SET foldercount = foldercount+1 WHERE usr = %s AND folder = %s"
            else:
                sql_command = f"UPDATE {self._table_name} SET foldercount = foldercount-1 WHERE usr = %s AND folder = %s"
            data = (self._usr_name, self._folder)
            self._cursor.execute(sql_command, data)
            self._conn.commit()
            return 1
        except pymysql.Error as e:
            self._conn.rollback()
            print(f"update_folders_list Error:{e.args[0]},{e.args[1]}")
            return 0

    # 收藏选中的folder_list
    def update_folders_list_like(self):
        self.create_connect()
        try:
            if self._flag:
                sql_command = f'''UPDATE {self._table_name} SET `like`=%s WHERE usr=%s and folder=%s and url=%s and username=%s and `password`=%s and note=%s and createdate=%s'''
            else:
                sql_command = f'''UPDATE {self._table_name} SET `like`=%s WHERE usr=%s and folder=%s and url=%s and username=%s and password=%s and note=%s and createdate=%s'''
            data = (self._like, self._usr_name, self._folder, self._url, self._username, self._password,
                    self._note, self._time)
            self._cursor.execute(sql_command, data)
            self._conn.commit()
            return 1
        except pymysql.Error as e:
            self._conn.rollback()
            print(f"update_folders_list_like: {e.args[0]},{e.args[1]}")
            return 0
        finally:
            self._cursor.close()

    # 更新当前用户的log_folderscount值
    def update_log_folderscount(self):
        self.create_connect()
        try:
            if self._flag:
                sql_command = f"UPDATE {self._table_name} SET folderscount = folderscount+1 WHERE usr = {self._usr_name}"
            else:
                sql_command = f"UPDATE {self._table_name} SET folderscount = folderscount-1 WHERE usr = {self._usr_name}"
            self._cursor.execute(sql_command)
            self._conn.commit()
        except pymysql.Error as e:
            self._conn.rollback()
            print(f"update_log_folderscount Error:{e.args[0]},{e.args[1]}")
            return 0
        finally:
            self._cursor.close()

    # /*-----------------@END: windows@-------------------*/

    def search_folder_like(self):
        self.create_connect()
        if self._model:
            try:
                sql_command = f'''SELECT `like` FROM {self._table_name} WHERE usr=%s AND folder=%s AND
                                    url=%s AND username=%s AND password=%s AND note=%s AND createdate=%s AND trash=0'''
                data = (self._usr_name, self._folder, self._url, self._username, self._password, self._note, self._time)
                self._cursor.execute(sql_command, data)
                self._conn.commit()
                result = self._cursor.fetchone()
                return result
            except pymysql.Error as e:
                print(f" search_folder_like Error:{e.args[0]},{e.args[1]}")
                return 0
            finally:
                self._cursor.close()
        else:
            try:
                sql_command = f"SELECT folder, url, username, password, note, createdate, `like`  FROM {self._table_name} WHERE `like` = 1"
                self._cursor.execute(sql_command)
                self._conn.commit()
                result = self._cursor.fetchall()
                return result
            except pymysql.Error as e:
                print(f" search_folder_like Error:{e.args[0]},{e.args[1]}")
                return 0
            finally:
                self._cursor.close()

    def search_by_trash(self):
        self.create_connect()
        try:
            sql_command = f'''SELECT folder, url, username, password, note, createdate
                                FROM {self._table_name} WHERE usr={self._usr_name} AND trash=1'''
            self._cursor.execute(sql_command)
            self._conn.commit()
            result = self._cursor.fetchall()
            # print(len(result))
            return result
        except pymysql.Error as e:
            print(f"search_folder_by_usr Error:{e.args[0]},{e.args[1]}")
            return 0
        finally:
            self._cursor.close()

    # 查找当前用户的拥有的folder
    def search_folder_by_usr(self):
        self.create_connect()
        try:
            sql_command = f'''SELECT folder FROM {self._table_name} WHERE usr = {self._usr_name} '''
            self._cursor.execute(sql_command)
            self._conn.commit()
            result = self._cursor.fetchall()
            # print(len(result))
            return result
        except pymysql.Error as e:
            print(f"search_folder_by_usr Error:{e.args[0]},{e.args[1]}")
            return 0
        finally:
            self._cursor.close()

    def search_usr_by_loginfo(self):
        self.create_connect()
        try:
            sql_command = f'''SELECT qid, usr, pwd FROM {self._table_name}
                            WHERE usr = {self._usr_name} and pwd = {self._usr_pwd}'''
            self._cursor.execute(sql_command)
            self._conn.commit()
            result = self._cursor.fetchone()
            return result
        except pymysql.Error as e:
            print(f"search_by_loginfoError:{e.args[0]},{e.args[1]}")
            return 0
        finally:
            self._cursor.close()

    # 更新表users_log_information
    def update_usr_info(self):
        self.create_connect()
        try:
            self._qid = re.sub('[{}-]', r"", QUuid.createUuid().toString())
            print(self._qid)
            sql_command = f"INSERT INTO {self._table_name} (qid, usr, pwd) VALUES (%s, %s, %s)"
            data = (self._qid, self._usr_name, self._usr_pwd)
            self._cursor.execute(sql_command, data)
            self._conn.commit()
            return self._qid
        except pymysql.Error as e:
            self._conn.rollback()
            print(f"search_by_update_usr_info Error:{e.args[0]},{e.args[1]}")
            return 0
        finally:
            self._cursor.close()

    # /*-----------------@windows@-------------------*/

