import sys
from end.ui.loginWindow_ui import Ui_Form
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from end.database.mysql_db import *
from end.ui.main_demo_ui import *
from end.database.file_process import *
import pandas as pd


# 全局变量
index_dict = {
    'btn_shome': 0,
    'btn_slike': 1,
    'btn_strash': 2,
    'btn_sfolder': 3,
    'btn_bhome': 0,
    'btn_blike': 1,
    'btn_btrash': 2,
    'btn_bfolder': 3,
    'btn_head_user': 4,
}


class myWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.frame_smenu.hide()
        self.ui.frame_folder_right.hide()
        # self.ui.listWidget.hide()

        # 选择对应的Qstackwidgets的页面, 高亮当前按钮
        # Big btn
        self.ui.btn_bhome.clicked.connect(self.change_window)
        self.ui.btn_bhome.clicked.connect(self.show_current_btn)

        self.ui.btn_blike.clicked.connect(self.change_window)
        self.ui.btn_blike.clicked.connect(self.show_current_btn)

        self.ui.btn_btrash.clicked.connect(self.change_window)
        self.ui.btn_btrash.clicked.connect(self.show_current_btn)

        self.ui.btn_bfolder.clicked.connect(self.change_window)
        self.ui.btn_bfolder.clicked.connect(self.show_current_btn)
        # Small btn
        self.ui.btn_shome.clicked.connect(self.change_window)
        self.ui.btn_shome.clicked.connect(self.show_current_btn)

        self.ui.btn_slike.clicked.connect(self.change_window)
        self.ui.btn_slike.clicked.connect(self.show_current_btn)

        self.ui.btn_strash.clicked.connect(self.change_window)
        self.ui.btn_strash.clicked.connect(self.show_current_btn)

        self.ui.btn_sfolder.clicked.connect(self.change_window)
        self.ui.btn_sfolder.clicked.connect(self.show_current_btn)

        self.ui.btn_head_user.clicked.connect(self.change_window)

        # listWidget signal and slot
        # 加载当前item的数据
        self.ui.listWidget_folder.itemClicked.connect(self.load_data)
        # 保存当前item的名字
        # self.ui.listWidget.doubleClicked.connect
        # self.ui.treeWidget_folder.itemClicked.connect(self.initial_table)

        # self.ui.tableWidget_folder.hide()

        # self.get_all_folders()

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
            self.ui.btn_blike.setStyleSheet(style_sheet)
            self.ui.btn_btrash.setStyleSheet(style_sheet)
            self.ui.btn_bfolder.setStyleSheet(style_sheet)
            # small
            self.ui.btn_slike.setStyleSheet(style_sheet)
            self.ui.btn_strash.setStyleSheet(style_sheet)
            self.ui.btn_sfolder.setStyleSheet(style_sheet)
        if index_dict[text] == 1:
            self.ui.btn_bhome.setStyleSheet(style_sheet)
            self.ui.btn_btrash.setStyleSheet(style_sheet)
            self.ui.btn_bfolder.setStyleSheet(style_sheet)
            # small
            self.ui.btn_shome.setStyleSheet(style_sheet)
            self.ui.btn_strash.setStyleSheet(style_sheet)
            self.ui.btn_sfolder.setStyleSheet(style_sheet)
        if index_dict[text] == 2:
            self.ui.btn_bhome.setStyleSheet(style_sheet)
            self.ui.btn_blike.setStyleSheet(style_sheet)
            self.ui.btn_bfolder.setStyleSheet(style_sheet)
            # small
            self.ui.btn_shome.setStyleSheet(style_sheet)
            self.ui.btn_slike.setStyleSheet(style_sheet)
            self.ui.btn_sfolder.setStyleSheet(style_sheet)

        if index_dict[text] == 3:
            self.ui.btn_bhome.setStyleSheet(style_sheet)
            self.ui.btn_blike.setStyleSheet(style_sheet)
            self.ui.btn_btrash.setStyleSheet(style_sheet)
            # small
            self.ui.btn_shome.setStyleSheet(style_sheet)
            self.ui.btn_slike.setStyleSheet(style_sheet)
            self.ui.btn_strash.setStyleSheet(style_sheet)

        self.sender().setStyleSheet(u"background-color: rgb(66,185,131)")

    def get_index(self, item):
        print(self.ui.listWidget_folder.currentIndex())
        print(self.sender().objectName())
        print(item.text(0))
        print(item.childCount())

    def load_data(self):
        list_itms_dic = {}
        kids = self.ui.listWidget_folder.count()

        for i in range(0, kids):
            item_text = self.ui.listWidget_folder.item(i).text()
            list_itms_dic[item_text] = i
        print(list_itms_dic)

        item = self.ui.listWidget_folder.currentRow()
        list_text = self.ui.listWidget_folder.item(item).text()
        print(list_text)

        # data = SQL.get_currentItem_table(list_text)
        # try:
        #     print(len(data))
        #     print(len(data[0]))
        #     raws = len(data)
        #     self.ui.tableWidget_folder.setRowCount(raws)
        #     for i in range(0, raws):
        #         for j in range(0, len(data[0])):
        #             cell = QTableWidgetItem()
        #             cell.setText(data[i][j])
        #             self.ui.tableWidget_folder.setItem(i, j, cell)
        #
        # except NoneType:
        #     print('error')

        # header = ['url', 'name', 'sex', 'number', 'major', 'phone']
        # self.ui.tableWidget_folder.setHorizontalHeaderLabels(header)
        # self.ui.tableWidget.verticalHeader().setVisible(False)
        # self.ui.tableWidget_folder.show()
        # data = SQL.search_values()

        # else:
        #     self.ui.tableWidget_folder.clearContents()
        #     self.ui.tableWidget_folder.hide()

    def get_all_folders(self):
        kids = self.ui.listWidget_folder.currentIndex().row()
        data = self.ui.listWidget_folder.item(kids)
        print(data.text())
        # lenth = len(kids)
        # print(lenth)
        print(kids)
        # label = kids.text()
        # print(label)
        # data_dict = {}

    # btn_like
    # def on_btn_like_cli
    @Slot()
    def on_btn_folder_list_add_clicked(self):
        print('++++')
        item = QListWidgetItem()
        item.setIcon(QIcon(":/icons/feather/folder.svg"))
        item.setText('新建密码库')
        item.setFlags(Qt.ItemIsEnabled|Qt.ItemIsEditable)
        self.ui.listWidget_folder.addItem(item)

    @Slot()
    def on_btn_folder_list_delete_clicked(self):
        print('----')
        current_item = self.ui.listWidget_folder.count() - 1
        print(current_item)
        item = self.ui.listWidget_folder.takeItem(current_item)
        del item


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainwin = myWindow()
#     mainwin.show()
#     sys.exit(app.exec())
