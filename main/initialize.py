import sys
from end.ui.loginWindow_ui import Ui_Form
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from end.database.mysql_db import *
from end.main.mainWin import *

from end.database.file_process import *




# 登录窗口
class logWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # self.openDB()

        # self.ui.pushButton_login.clicked.connect(self.check)



    @Slot()
    def on_pushButton_login_clicked(self):
        usrtext = self.ui.lineEdit_usr
        pwdtext = self.ui.lineEdit_pwd
        current_usr = usrtext.text()
        current_pwd = pwdtext.text()
        # print(current_usr)
        # print(current_pwd)

        result = SQL.verify_login(current_usr, current_pwd)
        # print(tuple(result))
        # print(type(result))
        # print(result[0])
        # print(type(result[0]))
        if result:
            usr = result[0]
            pwd = result[1]
        else:
            usr = None
            pwd = None

        if current_usr == u'' or current_pwd == u'':
            if current_usr == u'':
                print('input usr')
            else:
                print('input pwd')
        elif current_usr == usr and current_pwd == pwd:
            # self.sql.cursor.close()
            print('ok')
            new_window.show()
            self.close()

        else:
            print('usr or pwd error')
            usrtext.setText(u'')
            pwdtext.setText(u'')

    @Slot()
    def on_pushButton_register_clicked(self):
        usrtext = self.ui.lineEdit_usr
        pwdtext = self.ui.lineEdit_pwd
        current_usr = usrtext.text()
        current_pwd = pwdtext.text()

        if current_usr == u'' or current_pwd == u'':
            print('input usr or pwd')
        elif SQL.verify_login(current_usr, current_pwd):
            print('user has already existed!')
            usrtext.setText(u'')
            pwdtext.setText(u'')
        else:
            pattern = r"[{}-]"
            # userid =
            # df = pd.DataFrame()
            try:
                SQL.insert_values(re.sub(pattern, r"", QUuid.createUuid().toString()),
                                  current_usr,
                                  current_pwd)
                print('register ok!')
            except pymysql.err.IntegrityError:
                print('username has already existed!')

    @Slot()
    def on_label_findAccount_clicked(self):
        self.ui.label_findAccount.setOpenExternalLinks(True)

    @Slot()
    def on_pushButton_github_clicked(self):
        QDesktopServices.openUrl(QUrl('https://github.com/1716285375'))

    @Slot()
    def on_pushButton_youtube_clicked(self):
        QDesktopServices.openUrl(QUrl('https://www.youtube.com/channel/UCU9p68IGgJnTKUxGS7_MWHA'))

    @Slot()
    def on_pushButton_twitter_clicked(self):
        QDesktopServices.openUrl(QUrl('https://twitter.com/jie07965079'))

    @Slot()
    def on_pushButton_telegram_clicked(self):
        QDesktopServices.openUrl(QUrl('https://www.ahnu.edu.cn/'))

    # def move_window(self):


# 主窗口
class mainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedSize(600, 600)
        self.setWindowIcon(QIcon(':/icons/feather/command.svg'))
        self.setWindowTitle('Burgress PM')

        win = QWidget()
        self.label = QLabel(win)
        self.label.setText('Welcome')
        self.label.setGeometry(200, 200, 100, 30)

        self.button = QPushButton(win)
        self.button.setIcon(QIcon(':/icons/feather/check.svg'))
        self.button.clicked.connect(self.on_button_clicked)

        self.setCentralWidget(win)

    def on_button_clicked(self):
        msg = QMessageBox.information(self, "heelo", "goodasdasf",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        print(msg)
        print(msg == QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = logWindow()
    login.show()
    new_window = myWindow()
    sys.exit(app.exec())


