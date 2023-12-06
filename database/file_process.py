import numpy as np
import pandas as pd
import sqlalchemy as sql
from PySide6.QtCore import QUuid
import re
import string
import random

from datetime import datetime, timedelta


def random_date():
    year = random.randint(2000, 2030)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime(year, month, day)

# random_dates = [random_date() for _ in range(100)]

def connect_sql():
    return sql.create_engine('mysql://remote:12345678@120.26.55.56/burgresspm_data?charset=utf8')


def read_data(filename):
    df = pd.read_excel(filename, sheet_name='Sheet1', header=0, skiprows=1)
    print(df.columns)
    print(df.head())
    colums_to_delete = [df.columns[0], df.columns[6], df.columns[7], df.columns[8]]
    # df_new = df.drop(columns=colums_to_delete, axis=1, inplace=False)[[df.columns[3], df.columns[5]]]
    df_new = df.drop(columns=colums_to_delete, axis=1, inplace=False)
    # print(len(df_new))
    # print(df_new)
    colunms_table = ['name', 'sex', 'number', 'major', 'phone']
    df_new.columns = colunms_table
    print(df_new.columns)
    print(df_new.head())
    patten = r"[{}-]"
    ids = [re.sub(patten, r"", QUuid.createUuid().toString()) for i in range(0, len(df_new))]
    # print(ids[0:12])
    usrid = pd.Series(ids)
    random_dates = [random_date() for _ in range(len(df_new))]
    df_new.insert(0, 'usrid', usrid)
    df_new.insert(4, 'time', pd.Series(random_dates))

    print(df_new.head())
    return df_new

def create_table(df, table_name=None):
    engine = connect_sql()
    if table_name:
        dtype = {'usrid': sql.String(256), 'number': sql.String(128), 'phone': sql.String(128)}
        df_new = df[[df.columns[0], df.columns[3], df.columns[5]]]
        df_new.to_sql(table_name, con=engine, if_exists='replace', index=False, dtype=dtype)
        print('create successfully')
    else:
        print('create failure!')
        return 0

def insert_table(df):
    engine = connect_sql()
    dtype = {'usrid': sql.String(255), 'name': sql.String(255), 'sex': sql.String(16),
             'number': sql.String(128), 'major': sql.String(255), 'phone': sql.String(128)}
    df.to_sql('user_info', con=engine, if_exists='replace',
              index=False, dtype=dtype)
    print('ok')


def insert_value(df, table):
    engine = connect_sql()
    df.to_sql(table, con=engine, if_exists='append',
              index=False)


def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def get_data(filename):
    df = pd.read_csv(filename)
    # print(df.head())
    colums_to_delete = [df.columns[0], df.columns[4]]
    # df_new = df.drop(columns=colums_to_delete, axis=1, inplace=False).apply(lambda x: x.fillna(''), axis=0)
    df_new = df.drop(columns=colums_to_delete, axis=1, inplace=False).dropna()
    data = np.zeros(len(df_new), dtype=np.str_).tolist()
    for i in range(0, len(df_new)):
        data[i] = generate_random_string(10)
        # print(data[i])
    # print(data)
    # print(df_new)
    df_new.insert(loc=df_new.columns.get_loc('password') + 1, column='note', value=data)
    print(df_new.head())
    return df_new


def get_table(df, table_name=None):
    engine = connect_sql()
    if table_name:
        dtype = {'url': sql.String(256), 'username': sql.String(128),
                 'password': sql.String(128), 'note': sql.String(256)}
        df.to_sql(table_name, con=engine, if_exists='replace', index=False, dtype=dtype)
        print('create successfully')
    else:
        print('create failure!')
        return 0


if __name__ == '__main__':
    # dfs = read_data(filename='./usrinfo.xlsx')
    # print(dfs.head())
    # insert_table(dfs)
    # create_table(dfs, 'userlogin')

    # file = './Edge_pwd.csv'
    # df = get_data(file)
    # qid = read_data('./usrinfo.xlsx')
    # qid.to_excel('./user.xlsx')

    # df.to_csv('./loginfo.csv')
    # get_table(df, 'usrinfo_folder_6')
    table_name = 'users_folders'
    engine = connect_sql()
    df = pd.read_excel('./users_folders.xlsx', sheet_name='Sheet1', header=0)
    print(df.head())
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print('2322')
