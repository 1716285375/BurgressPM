import pandas as pd
import sqlalchemy as sql
from PySide6.QtCore import QUuid
import re


def connect_sql():
    return sql.create_engine('mysql://remote:12345678@120.26.55.56/user_information?charset=utf8')


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
    df_new.insert(0, 'usrid', usrid)

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


if __name__ == '__main__':
    dfs = read_data(filename='./usrinfo.xlsx')
    # print(dfs.head())
    insert_table(dfs)
    create_table(dfs, 'userlogin')
