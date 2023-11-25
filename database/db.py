from PySide6 import QtSql


db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName('./data.sqlite')
db.open()

if not db.open():
    print('Error')

query = QtSql.QSqlQuery()
# query.exec("create table userdata (id int primary key autoincrement not null ,username varchar(100) not null , password varchar(100) not null );")
#
# query.exec("insert into userdata (username, password) values ('123456', '5408')")
query.exec("select * from userdata where id=1")
query.first()
print(query.value('username'), query.value('password'))

