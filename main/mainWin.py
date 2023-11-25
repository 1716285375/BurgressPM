import sys
from end.ui.loginWindow_ui import Ui_Form
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from end.database.mysql_db import *
from end.ui.mainWindow_ui import *
from end.database.file_process import *


# 全局变量
index_dict = {
    'btn_home': 0,
    'btn_like': 1,
    'btn_trash': 2,
    'treeWidget_pwd': 3
}


class myWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 选择对应的Qstackwidgets的页面, 高亮当前按钮
        self.ui.btn_home.clicked.connect(self.change_window)
        self.ui.btn_home.clicked.connect(self.show_current_btn)

        self.ui.btn_like.clicked.connect(self.change_window)
        self.ui.btn_like.clicked.connect(self.show_current_btn)

        self.ui.btn_trash.clicked.connect(self.change_window)
        self.ui.btn_trash.clicked.connect(self.show_current_btn)

        self.ui.treeWidget_pwd.itemClicked.connect(self.change_window)


    def get_index(self, item):
        print(self.ui.treeWidget_pwd.currentIndex())
        print(self.sender().objectName())
        # print(item.text(0))
        # print(item.childCount())

    def change_window(self):
        text = self.sender().objectName()
        # print(type(text))
        # print(text)
        idx = index_dict[text]
        # print(idx)
        # print(type(idx))
        self.ui.stackedWidget_content.setCurrentIndex(idx)

    def show_current_btn(self):
        text = self.sender().objectName()
        print(text)
        with open("../ui/option_button.qss", "r") as f:
            style_sheet = f.read()
        if index_dict[text] == 0:
            self.ui.btn_like.setStyleSheet(style_sheet)
            self.ui.btn_trash.setStyleSheet(style_sheet)
        if index_dict[text] == 1:
            self.ui.btn_home.setStyleSheet(style_sheet)
            self.ui.btn_trash.setStyleSheet(style_sheet)
        if index_dict[text] == 2:
            self.ui.btn_home.setStyleSheet(style_sheet)
            self.ui.btn_like.setStyleSheet(style_sheet)
        self.sender().setStyleSheet(u"background-color: rgb(66,185,131)")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = myWindow()
    mainwin.show()
    sys.exit(app.exec())
