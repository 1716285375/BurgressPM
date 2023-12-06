import sys
import time

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from end.database.mysqldata import *
from end.ui.main_demo_ui import *
from end.ui.loginWindow_ui import *
from end.ui.folder_list_content_edit_ui import *
from end.database.file_process import *

import pandas as pd
import random

QID = ''
USR = ''
stackWidget_page_obj2idx = {
    'btn_shome': 0,
    'btn_bhome': 0,
    'btn_blike': 1,
    'btn_slike': 1,
    'btn_strash': 2,
    'btn_btrash': 2,
    'btn_sfolder': 3,
    'btn_bfolder': 3,
    'btn_head_user': 4,
}

table_name_id2obj = {
    0: 'users_login_information',
    1: 'users_account_information',
    2: 'users_folder_information',
    3: 'users_folders',
    4: 'users_trash',
    5: 'users_like',
}

table_name = ['users_login_information',
              'users_folders_information',
              'users_folders']

msg_idx2obj = {
    0: '错误',
    1: '警告',
    2: '异常',
}
msg_idx2text = {
    '错误': '这是一个错误',
    '警告': '这是一个警告',
    '异常': '这是一个异常'
}
msg_idx2img = {
    0: u":/icons/feather/alert-octagon.svg",
    1: u":/icons/feather/info.svg",
    2: u":/icons/feather/alert-triangle.svg"
}
icon_idx2file = {
    0: u":/icons/feather/unlike.svg",
    1: u":/icons/feather/like.svg"
}
btn_str2obj = {
    'like': 'btn_folder_like',
    'edit': 'btn_folder_edit',

}


class Message(QObject):
    def __init__(self):
        super().__init__()
        self.message_sent = Signal(str)


class listWin(QDialog):
    def __init__(self, parent=None, usr=None, folder_name=None, url=None, username=None,
                 password=None, note=None, time=None, model=True):
        super().__init__(parent)
        # 定义变量
        self.flag = True
        self._usr = usr
        self._folder = folder_name
        self._url = url
        self._username = username
        self._password = password
        self._note = note
        self._time = time
        self._model = model
        # 初始化窗口
        self.ui = Ui_List_edit()
        self.ui.setupUi(self)
        self.init_window_setting()
        self.init_signal_slot()
        # 加载待编辑的数据
        self.show_edit_content()

    def init_window_setting(self):
        validator = QIntValidator(0, 32, self)
        self.ui.lineEdit_list_edit_len_num.setValidator(validator)
        pass

    def show_edit_content(self):
        if self._url or self._username or self._password or self._note or self._time:
            self.ui.lineEdit_list_edit_url.setText(self._url)
            self.ui.lineEdit_list_edit_usr.setText(self._username)
            self.ui.lineEdit_list_edit_pwd.setText(self._password)
            self.ui.lineEdit_list_edit_note.setText(self._note)
            self._model = False
        else:
            self._model = True

    def init_signal_slot(self):
        # 提交edit_information
        self.ui.btn_list_edit_confirm.clicked.connect(self.btn_affirm)
        # 取消，关闭窗口
        self.ui.btn_list_edit_cancel.clicked.connect(self.close)
        # 复制密码
        self.ui.btn_list_edit_copy.clicked.connect(self.copy_pwd)
        # 随机生成密码
        self.ui.btn_list_edit_produce.clicked.connect(self.passgen)
        # 填充生成的密码到edit_item
        self.ui.btn_list_edit_fill.clicked.connect(self.passfill)
        # 同步QSlider和QLineEdit的数值
        self.ui.horizontalSlider_list_edit_len.valueChanged.connect(self.update_value_slider2lineedit)
        self.ui.lineEdit_list_edit_len_num.textChanged.connect(self.update_value_lineedit2slider)

        # 清除密码生成器的所有设置
        self.ui.btn_list_edit_clear.clicked.connect(self.clear_setting)

    def update_value_slider2lineedit(self):
        value = self.ui.horizontalSlider_list_edit_len.value()
        if value:
            self.ui.lineEdit_list_edit_len_num.setText(str(value))
        else:
            self.ui.lineEdit_list_edit_len_num.setText('')

    def update_value_lineedit2slider(self):
        value = self.ui.lineEdit_list_edit_len_num.text().strip()
        if value:
            self.ui.horizontalSlider_list_edit_len.setValue(int(value))
        else:
            self.ui.horizontalSlider_list_edit_len.setValue(0)

    def btn_affirm(self):
        if not self._model:
            data_previous = [self._url, self._username, self._password, self._note, self._time]
            print(data_previous)
            self._url = self.ui.lineEdit_list_edit_url.text().strip()
            self._username = self.ui.lineEdit_list_edit_usr.text().strip()
            self._password = self.ui.lineEdit_list_edit_pwd.text().strip()
            self._note = self.ui.lineEdit_list_edit_note.text().strip()
            self._time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            flag = pyMysql(table_name=table_name[1], folder_name=self._folder, usr=self._usr,
                           url=self._url, username=self._username, password=self._password,
                           note=self._note, time=self._time,
                           url_p=data_previous[0], username_p=data_previous[1], password_p=data_previous[2],
                           note_p=data_previous[3], time_p=data_previous[4],
                           model=self._model).update_folders_list_item()
            if flag:
                QMessageBox.about(self, "编辑密码库列表项", "修改成功")
                pyMysql(table_name=table_name[2], folder_name=self._folder, usr=self._usr).update_folders_count()
            else:
                self.flag = False
                print("error:", flag)
                QMessageBox.about(self, "编辑密码库列表项", "修改失败")
            print(self._url, self._username, self._password, self._note, self._time)
        else:
            self._url = self.ui.lineEdit_list_edit_url.text().strip()
            self._username = self.ui.lineEdit_list_edit_usr.text().strip()
            self._password = self.ui.lineEdit_list_edit_pwd.text().strip()
            self._note = self.ui.lineEdit_list_edit_note.text().strip()
            self._time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            flag = pyMysql(table_name=table_name[1], folder_name=self._folder, usr=self._usr,
                           url=self._url, username=self._username, password=self._password,
                           note=self._note, time=self._time).update_folders_list_item()
            if flag:
                QMessageBox.about(self, "编辑密码库列表项", "添加成功")
                pyMysql(table_name=table_name[2], folder_name=self._folder, usr=self._usr).update_folders_count()
            else:
                self.flag = False
                print("error:", flag)
                QMessageBox.about(self, "编辑密码库列表项", "添加失败")
            print(self._url, self._username, self._password, self._note)

    def passgen(self):
        num = self.ui.checkBox_list_edit_number.text().strip()
        letter = self.ui.checkBox_list_edit_letter.text().strip()
        sign = self.ui.checkBox_list_edit_sign.text().strip()
        length = self.ui.lineEdit_list_edit_len_num.text().strip()
        print(num, letter, sign, length)
        pwd_gen = self.generate_random_string()
        self.ui.lineEdit_list_edit_to_pwd.setText(pwd_gen)

    def generate_random_string(self):
        num_flag = self.ui.checkBox_list_edit_number.isChecked()
        letter_flag = self.ui.checkBox_list_edit_letter.isChecked()
        sign_flag = self.ui.checkBox_list_edit_sign.isChecked()
        length = self.ui.lineEdit_list_edit_len_num.text().strip()
        if length and (num_flag or letter_flag or sign_flag):
            characters = ''
            if num_flag:
                characters += string.digits
            if letter_flag:
                characters += string.ascii_letters
            if sign_flag:
                characters += string.punctuation
            random_pwd = ''.join(random.choice(characters) for _ in range(int(length)))
            # self.ui.lineEdit_list_edit_to_pwd.setText(random_pwd)
        else:
            QMessageBox.about(self, "密码生成器", "请指定密码的长度")
            random_pwd = ''
        return random_pwd

    def passfill(self):
        pwd_fill = self.ui.lineEdit_list_edit_to_pwd.text().strip()
        if pwd_fill:
            self.ui.lineEdit_list_edit_pwd.setText(pwd_fill)
            print('ok')
            return 1
        else:
            QMessageBox.about(self, "填充生成的密码", "填充失败")
            return 0

    def copy_pwd(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.lineEdit_list_edit_to_pwd.text())
        pass

    def clear_setting(self):
        self.ui.lineEdit_list_edit_to_pwd.setText('')
        self.ui.lineEdit_list_edit_len_num.setText('')
        self.ui.checkBox_list_edit_number.setChecked(False)
        self.ui.checkBox_list_edit_letter.setChecked(False)
        self.ui.checkBox_list_edit_sign.setChecked(False)
        self.ui.horizontalSlider_list_edit_len.setValue(0)


class logWin(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.qid = ''
        self.usr = ''
        self.pwd = ''
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initial_login_btn()

    def initial_login_btn(self):
        # self.ui.pushButton_login.clicked.connect(self.get_usr_info)
        self.ui.pushButton_login.clicked.connect(self.check_usr_info)
        self.ui.pushButton_register.clicked.connect(self.register_usr_info)

    def get_log_info(self):
        usr = self.ui.lineEdit_usr.text()
        pwd = self.ui.lineEdit_pwd.text()
        # print(usr, pwd)
        return usr, pwd

    # 登录验证
    def check_usr_info(self):
        usr, pwd = self.get_log_info()
        result = pyMysql(table_name_id2obj[0], '', 0, usr, pwd).search_usr_by_loginfo()
        # print(type(result))
        # print(result)
        if not result:
            print('error')
        else:
            if usr == result[1] and pwd == result[2]:
                print('ok')

                self.qid = pyMysql(table_name_id2obj[0], '', 0, usr, pwd).search_usr_by_loginfo()
                print(self.usr)
                burgresspm._qid = self.qid
                burgresspm._usr, burgresspm.usr = self.get_log_info()
                burgresspm.show()
                loginpm.close()
            else:
                print('error')

    # 注册账号
    def register_usr_info(self):
        usr, pwd = self.get_log_info()
        result = pyMysql(table_name_id2obj[0], 0, usr, pwd).search_usr_by_loginfo()
        if not result:
            self.qid = pyMysql(table_name_id2obj[0], 0, usr, pwd).update_usr_info()
            # QMessageBox('注册账号', '注册成功')
        else:
            print("注册失败！")


class mainApp(QMainWindow):
    def __init__(self, loginWin, parent=None):
        super().__init__(parent)
        self._usrinfo = loginWin
        self.listedit = None
        # user_information
        self._qid = self._usrinfo.qid
        self._usr = self._usrinfo.usr
        # main ui
        self.ui_mainWin = Ui_MainWindow()
        self.ui_mainWin.setupUi(self)
        self._main_qss = '../ui/main_window.qss'
        self._btn_qss = ''
        self._treewidget_qss = ''
        qss = self.load_stylesheet(self._main_qss)
        self.ui_mainWin.centralwidget.setStyleSheet(qss)
        self.initial_ui()

        self.init_signal_slot()

    # /*-------------------------@BEGIN: windows@--------------------------*/
    # 加载QSS
    def load_stylesheet(self, qss):
        style_file = QFile()
        style_file.setFileName(qss)
        if style_file.open(QFile.ReadOnly | QFile.Text):
            # 使用 QTextStream 读取文件内容
            stream = QTextStream(style_file)
            style_string = stream.readAll()
            style_file.close()
            print('ok')
            return style_string
        else:
            print(f"Failed to open style file: {self._qssfile}")
            print('error')
            return None

    # 初始化界面结构
    def initial_ui(self):
        self.ui_mainWin.frame_bmenu.hide()
        self.ui_mainWin.frame_folder_right.hide()

    # 切换菜单大小
    def init_signal_slot(self):
        # set_menu_btn_toggle
        self.ui_mainWin.btn_bhome.clicked.connect(self.set_page)
        self.ui_mainWin.btn_shome.clicked.connect(self.set_page)

        self.ui_mainWin.btn_blike.clicked.connect(self.set_page)
        self.ui_mainWin.btn_slike.clicked.connect(self.set_page)

        self.ui_mainWin.btn_btrash.clicked.connect(self.set_page)
        self.ui_mainWin.btn_strash.clicked.connect(self.set_page)

        self.ui_mainWin.btn_bfolder.clicked.connect(self.set_page)
        self.ui_mainWin.btn_bfolder.clicked.connect(self.load_folder_list)
        self.ui_mainWin.btn_bfolder.clicked.connect(self.load_folder_list_content)
        self.ui_mainWin.btn_sfolder.clicked.connect(self.set_page)
        self.ui_mainWin.btn_sfolder.clicked.connect(self.load_folder_list)
        self.ui_mainWin.btn_sfolder.clicked.connect(self.load_folder_list_content)

        self.ui_mainWin.btn_head_user.clicked.connect(self.set_page)

        # /*-----------------@BEGIN: folder@-------------------*/
        # initial current user's folder list
        self.ui_mainWin.btn_folder_all.clicked.connect(self.load_folder_list)
        # add folder_list
        self.ui_mainWin.btn_folder_list_add.clicked.connect(self.add_folder_list)
        # delete_folder_list
        self.ui_mainWin.btn_folder_list_delete.clicked.connect(self.delete_folder_list)
        # show folder_list_content
        self.ui_mainWin.listWidget_folder.itemClicked.connect(self.load_folder_list_content)
        # open add folder_list_content
        self.ui_mainWin.btn_folder_add.clicked.connect(self.open_add_folder_list_content)
        # delete_folder_list_content
        self.ui_mainWin.btn_folder_delete.clicked.connect(self.delete_folder_list_content)
        # like_folder_list_content
        self.ui_mainWin.btn_folder_like.clicked.connect(self.like_folder_list_content)
        # edit_folder_list_content
        self.ui_mainWin.btn_folder_edit.clicked.connect(self.open_add_folder_list_content)
        # refresh_folder_list_content
        self.ui_mainWin.btn_folder_refresh.clicked.connect(self.load_folder_list_content)
        # /*-----------------@END: folder@-------------------*/

        # /*-----------------@BEGIN: Like@-------------------*/
        self.ui_mainWin.btn_blike.clicked.connect(self.show_like_list_content)
        self.ui_mainWin.btn_slike.clicked.connect(self.show_like_list_content)
        # /*-----------------@END: Like@-------------------*/
        # /*-----------------@BEGIN: trash@-------------------*/
        self.ui_mainWin.btn_btrash.clicked.connect(self.load_trash_data)
        self.ui_mainWin.btn_strash.clicked.connect(self.load_trash_data)
        # /*-----------------@BEGIN: trash@-------------------*/

    # 显示当前菜单对应的页面
    def set_page(self):
        obj = self.sender().objectName()
        idx = stackWidget_page_obj2idx[obj]
        self.ui_mainWin.stackedWidget_content.setCurrentIndex(idx)
        print(self._usrinfo.qid)

    # /*-------------------------@END: windows@--------------------------*/

    # *********************************************************************
    # *********************************************************************
    # *********************************************************************

    # /*-------------------------@BEGIN: folder@-------------------------*/
    # 加载并显示用户的folder_list
    def load_folder_list(self):
        folder_list_data = pyMysql(table_name=table_name[2], usr=self._usr).search_folder_by_usr()
        # print(folder_list_data)
        # print(type(folder_list_data))
        icon = QIcon(u":/icons/feather/folder.svg")
        items = [re.sub(r"[(),']", r"", str(item)) for item in folder_list_data]
        # print(items)
        self.ui_mainWin.listWidget_folder.clear()
        for i in range(0, len(items)):
            item = QListWidgetItem(items[i])
            item.setIcon(icon)
            self.ui_mainWin.listWidget_folder.addItem(item)
        # self.load_folder_list_content()
        # print(items)
        # print(type(items))
        # self.ui_mainWin.listWidget_folder.addItems(itemsicon)
        # self.ui_mainWin.listWidget_folder.add

    def get_all_folder_name(self):
        folder_list = pyMysql(table_name=table_name[2], usr=self._usr).search_folder_by_usr()
        # print(folder_list)
        # print(type(folder_list))
        folder_list_re = [re.sub(r"[(),']", r"", str(item)) for item in folder_list]
        # print(folder_list_re)
        folder_list_text = [re.match(r"新建文件夹\d+", item) for item in folder_list_re]
        # print(folder_list_text)
        folder_list_item = [item for item in folder_list_text if item is not None]
        # print(folder_list_item)
        if folder_list_item:
            folder_list_row = [i.group(0) for i in folder_list_item]
            print(folder_list_row)
            row = [re.findall(r"\d+", i) for i in folder_list_row]
            row = [re.sub(r"[\[\]']", r"", str(item)) for item in row]
            # print(row)
            row = [int(item) for item in row]
            row.sort()
            if row:
                index = int(row[-1]) + 1
                # print(index)
            else:
                index = 1
        else:
            return 1
        return index

    # 创建新的folder
    def add_folder_list(self):
        row = self.ui_mainWin.listWidget_folder.currentRow()
        kids = self.ui_mainWin.listWidget_folder.count()
        index = self.get_all_folder_name()
        print(index)
        folder_item = '新建文件夹{}'.format(index)
        if row + 1:
            self.ui_mainWin.listWidget_folder.insertItem(row + 1, folder_item)
        else:
            self.ui_mainWin.listWidget_folder.insertItem(kids + 1, folder_item)
        # print(row)

        pyMysql(table_name=table_name[2], usr=self._usr, folder_name=folder_item).update_folders_list()
        pyMysql(table_name=table_name[0], usr=self._usr).update_log_folderscount()
        self.load_folder_list()

    # 删除指定的folder
    def delete_folder_list(self):
        # 当前folder_list的数量
        kids = self.ui_mainWin.listWidget_folder.count()
        if kids:
            # 当前点击的行， folder_item为待删除的list名字
            row = self.ui_mainWin.listWidget_folder.currentRow()
            print('row: ', row)
            flag = row + 1
            if flag:
                folder_item = self.ui_mainWin.listWidget_folder.item(row).text().strip()
                data = pyMysql(table_name=table_name[1], folder_name=folder_item, usr=self._usr).search_by_folder()
                if data:
                    result = QMessageBox.warning(self, "警告", "这将删除当前folder下的所有数据项?",
                                                  QMessageBox.Yes | QMessageBox.No)
                    if result == QMessageBox.Yes:
                        self.ui_mainWin.listWidget_folder.takeItem(row)
                        # 从users_folders中移除该项
                        pyMysql(table_name=table_name[2], usr=self._usr, folder_name=folder_item,
                                flag=False).update_folders_list()
                        # 从users_log_informations中移除该项, folderscount - 1
                        pyMysql(table_name=table_name[0], usr=self._usr, flag=False).update_log_folderscount()
                        # 从users_folders_informations中移除所有该项相关的账户
                        outcome = pyMysql(table_name=table_name[1],
                                          usr=self._usr,
                                          folder_name=folder_item).delete_folders_all_list()
                        print('outcome: ', outcome)
                    else:
                        print('result: ', result)
                else:
                    self.ui_mainWin.listWidget_folder.takeItem(row)
                    # 从users_folders中移除该项
                    pyMysql(table_name=table_name[2], usr=self._usr, folder_name=folder_item,
                            flag=False).update_folders_list()
                    # 从users_log_informations中移除该项, folderscount - 1
                    pyMysql(table_name=table_name[0], usr=self._usr, flag=False).update_log_folderscount()
            else:
                item = self.ui_mainWin.listWidget_folder.item(kids - 1)
                folder_item = item.text().strip()
                data = pyMysql(table_name=table_name[1], folder_name=folder_item, usr=self._usr).search_by_folder()
                if data:
                    result = QMessageBox.warning(self, "警告", "这将删除当前folder下的所有数据项?",
                                                  QMessageBox.Yes | QMessageBox.No)
                    if result == QMessageBox.Yes:
                        self.ui_mainWin.listWidget_folder.takeItem(kids - 1)
                        # 从users_folders中移除该项
                        pyMysql(table_name=table_name[2], usr=self._usr, folder_name=folder_item,
                                flag=False).update_folders_list()
                        # 从users_log_informations中移除该项, folderscount - 1
                        pyMysql(table_name=table_name[0], usr=self._usr, flag=False).update_log_folderscount()
                        # 从users_folders_informations中移除所有该项相关的账户
                        outcome = pyMysql(table_name=table_name[1],
                                          usr=self._usr,
                                          folder_name=folder_item).delete_folders_all_list()
                        print(outcome)
                    else:
                        print(result)
                else:
                    self.ui_mainWin.listWidget_folder.takeItem(kids - 1)
                    # 从users_folders中移除该项
                    pyMysql(table_name=table_name[2], usr=self._usr, folder_name=folder_item,
                            flag=False).update_folders_list()
                    # 从users_log_informations中移除该项, folderscount - 1
                    pyMysql(table_name=table_name[0], usr=self._usr, flag=False).update_log_folderscount()
        else:
            return 0
        print(folder_item)
        self.load_folder_list_content()

    # /*-----------------@folder_list_content@-------------------*/
    # 显示当前folder_list的数据
    def load_folder_list_content(self):
        # 将获取的list_item数据显示到table中
        icon = QIcon()
        index = self.ui_mainWin.listWidget_folder.currentRow()
        print(index)
        if index is None or index == -1:
            index = 0
            first_item = self.ui_mainWin.listWidget_folder.item(index)
            self.ui_mainWin.listWidget_folder.setCurrentItem(first_item)
        # widget.(btn)
        try:
            print('@', index)
            folder_list_name = self.ui_mainWin.listWidget_folder.item(index).text().strip()
            self.ui_mainWin.tableWidget_folder.clearContents()
            folder_list_data = pyMysql(table_name=table_name[1],
                                       folder_name=folder_list_name,
                                       usr=self._usr).search_by_folder()
            print(folder_list_data)
        except AttributeError as ae:
            folder_list_data = None
            print(f"Caught an AttributeError: {ae}")

        # print(folder_list_data)
        if folder_list_data is not None:
            head = ['URL', 'USERNAME', 'PASSWORD', 'NOTE', 'CREATE TIME', 'LIKE']
            self.ui_mainWin.tableWidget_folder.setHorizontalHeaderLabels(head)
            self.ui_mainWin.tableWidget_folder.verticalHeader().setHidden(True)
            self.ui_mainWin.tableWidget_folder.setRowCount(len(folder_list_data))

            # print(type(folder_list_data[0][7]))
            for i in range(0, len(folder_list_data)):
                for j in range(0, len(folder_list_data[0]) - 3):
                    cell = QTableWidgetItem()
                    cell.setFlags(cell.flags() ^ Qt.ItemIsEditable)
                    if j + 2 == 7:
                        if folder_list_data[i][j + 2]:
                            icon.addFile(icon_idx2file[1])
                        else:
                            icon.addFile(icon_idx2file[0])
                        btn = QPushButton()
                        btn.setIcon(icon)
                        btn.setIconSize(QSize(24, 24))
                        btn.setCursor(Qt.PointingHandCursor)

                        self._btn_qss = "../ui/btn_table_item.qss"
                        btn_qss = self.load_stylesheet(self._btn_qss)
                        btn.setStyleSheet(btn_qss)

                        btn.clicked.connect(self.like_folder_list_content)
                        # cell.setData(Qt.UserRole, btn)
                        self.ui_mainWin.tableWidget_folder.setCellWidget(i, j, btn)
                    else:
                        cell.setText(str(folder_list_data[i][j + 2]))
                        self.ui_mainWin.tableWidget_folder.setItem(i, j, cell)
                    # cell.setBackground(
                    #     QBrush(qRgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
                    # print(cell)
            self.ui_mainWin.tableWidget_folder.resizeColumnsToContents()

        else:
            print('None')
            self.ui_mainWin.tableWidget_folder.setRowCount(0)
            return 0

    # 获取表格当前行的各项数据
    def load_folder_list_currentrow(self):
        try:
            table_row = self.ui_mainWin.tableWidget_folder.currentRow()
            print(table_row)
            data = []
            for column in range(0, self.ui_mainWin.tableWidget_folder.columnCount()-1):
                item = self.ui_mainWin.tableWidget_folder.item(table_row, column).text().strip()
                print(item)
                data.append(item)
            print(data)
            return data, table_row
        except AttributeError as ae:
            print(f"Caught an AttributeError: {ae}")
            return 0

    # 为folder_list_content添加数据项
    def open_add_folder_list_content(self):
        try:
            index = self.ui_mainWin.listWidget_folder.currentRow()
            folder_name = self.ui_mainWin.listWidget_folder.item(index).text().strip()

            sender = self.sender()
            if sender.objectName() == btn_str2obj['edit']:
                try:
                    # table_row
                    row = self.ui_mainWin.tableWidget_folder.currentRow()
                    data = []
                    for column in range(0, self.ui_mainWin.tableWidget_folder.columnCount() - 1):
                        data.append(self.ui_mainWin.tableWidget_folder.item(row, column).text().strip())
                    print(data)
                    self.listedit = listWin(usr=self._usr, folder_name=folder_name, url=data[0],
                                            username=data[1], password=data[2], note=data[3],
                                            time=data[4])
                except AttributeError as ae:
                    print(f"Caught an AttributeError: {ae}")
                    QMessageBox.warning(self, "警告", "请选择待编辑的数据项", QMessageBox.Ok)
                    return 0
            else:
                self.listedit = listWin(usr=self._usr, folder_name=folder_name)
            qss = self.load_stylesheet("../ui/list_edit_content.qss")
            self.listedit.setStyleSheet(qss)
            self.listedit.show()
            print('ok')
        except AttributeError as ae:
            print(f"Caught an AttributeError: {ae}")
            QMessageBox.warning(self, "警告", "请选择一个密码库", QMessageBox.Ok)
            return 0

    # 删除folder_list_content的数据项
    def delete_folder_list_content(self):
        try:
            row = self.ui_mainWin.listWidget_folder.currentRow()
            print(row)
            folder_list_name = self.ui_mainWin.listWidget_folder.item(row).text().strip()
            try:
                data, _ = self.load_folder_list_currentrow()
                # like = pyMysql(table_name=table_name[1], folder_name=folder_list_name, usr=self._usr,
                #                  url=data[0], username=data[1], password=data[2], note=data[3],
                #                  time=data[4]).search_folder_like()
                result = pyMysql(table_name=table_name[1], folder_name=folder_list_name, usr=self._usr,
                                 url=data[0], username=data[1], password=data[2], note=data[3],
                                 time=data[4], flag=False).update_folders_list_item()
                pyMysql(table_name=table_name[2], folder_name=folder_list_name, usr=self._usr, flag=False).update_folders_count()
                print('result:', result)
                self.load_folder_list_content()
            except TypeError as te:
                print(f"Caught an TypeError: {te}")
                QMessageBox.warning(self, "警告", "请选择要删除的数据项", QMessageBox.Ok)
        except AttributeError as ae:
            print(f"Caught an AttributeError: {ae}")
            QMessageBox.warning(self, "警告", "请选择一个密码库", QMessageBox.Ok)

    # 收藏folder_list_content的数据项
    def show_like_list_content(self):
        icon = QIcon()
        icon.addFile(icon_idx2file[1])
        data_like = pyMysql(table_name=table_name[1], model=False).search_folder_like()
        print(data_like[0])
        self.ui_mainWin.treeWidget_like.clear()
        if data_like is not None:
            head = ['FOLDER', 'URL', 'USERNAME', 'PASSWORD', 'NOTE', 'CREATE TIME', 'LIKE']
            self.ui_mainWin.treeWidget_like.setHeaderLabels(head)
            header = self.ui_mainWin.treeWidget_like.header()
            self._treewidget_qss = "../ui/treeWidget_head.qss"
            qss = self.load_stylesheet(self._treewidget_qss)
            header.setStyleSheet(qss)
            # # print(header)
            # header.resizeSection(0, 160)
            # header.resizeSection(1, 200)
            # header.resizeSection(2, 200)
            # header.resizeSection(3, 200)
            # header.resizeSection(4, 200)
            # header.resizeSection(5, 160)
            # header.resizeSection(6, 32)
            # self.ui_mainWin.treeWidget_like.setHeaderHidden(True)
            self.ui_mainWin.treeWidget_like.setColumnCount(len(data_like[0]))
            # print(type(folder_list_data[0][7]))
            for i in range(0, len(data_like)):
                # print(data_like[i])
                data = list(data_like[i])
                print(data)
                data[5] = data[5].strftime("%Y-%m-%d %H:%M:%S")
                cell = QTreeWidgetItem(self.ui_mainWin.treeWidget_like, data)

                btn = QPushButton()
                btn.setMaximumSize(32, 32)
                btn.setIcon(icon)
                btn.setIconSize(QSize(26, 26))
                btn.setCursor(Qt.PointingHandCursor)
                self._btn_qss = "../ui/btn_table_item.qss"
                btn_qss = self.load_stylesheet(self._btn_qss)
                btn.setStyleSheet(btn_qss)
                btn.clicked.connect(self.update_like_page)

                self.ui_mainWin.treeWidget_like.setItemWidget(cell, 6, btn)
                cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)
            for i in range(0, self.ui_mainWin.treeWidget_like.columnCount()):
                self.ui_mainWin.treeWidget_like.resizeColumnToContents(i)
        else:
            print("none!")

    def update_like_page(self):
        sender_button = self.sender()
        row = self.ui_mainWin.treeWidget_like.indexAt(sender_button.pos()).row()
        # print(row)
        current_row_data = self.ui_mainWin.treeWidget_like.topLevelItem(row)
        # print(current_row_data)
        # print(current_row_data.text(0).strip())
        data = [current_row_data.text(i).strip() for i in range(0, self.ui_mainWin.treeWidget_like.columnCount())]
        # print(data)
        flag = False
        result = pyMysql(table_name=table_name[1], usr=self._usr, folder_name=data[0],
                         url=data[1], username=data[2], password=data[3], note=data[4],
                         time=data[5], like=0, flag=flag).update_folders_list_like()
        print(result)
        self.ui_mainWin.treeWidget_like.takeTopLevelItem(row)
        self.show_like_list_content()

    def like_folder_list_content(self):
        icon = QIcon()
        index = self.ui_mainWin.listWidget_folder.currentRow()
        folder_list_name = self.ui_mainWin.listWidget_folder.item(index).text().strip()
        # print(folder_list_name)
        sender_button = self.sender()
        # print(sender_button.objectName())
        try:
            if sender_button.objectName() == btn_str2obj['like']:
                row = self.ui_mainWin.tableWidget_folder.currentRow()
            else:
                row = self.ui_mainWin.tableWidget_folder.indexAt(sender_button.pos()).row()
            # print(row, '***')
            # print('row----: ', row)
            data = []
            for column in range(0,  self.ui_mainWin.tableWidget_folder.columnCount() - 1):
                data.append(self.ui_mainWin.tableWidget_folder.item(row, column).text())
            # print('data:', data)
            like = pyMysql(table_name=table_name[1], usr=self._usr, folder_name=folder_list_name,
                           url=data[0], username=data[1], password=data[2], note=data[3],
                           time=data[4]).search_folder_like()
            # print(like[0])
            if like[0]:
                icon.addFile(icon_idx2file[0])
                flag = False
                result = pyMysql(table_name=table_name[1], usr=self._usr, folder_name=folder_list_name,
                                 url=data[0], username=data[1], password=data[2], note=data[3],
                                 time=data[4], like=0, flag=flag).update_folders_list_like()
            else:
                icon.addFile(icon_idx2file[1])
                flag = True
                result = pyMysql(table_name=table_name[1], usr=self._usr, folder_name=folder_list_name,
                                 url=data[0], username=data[1], password=data[2], note=data[3],
                                 time=data[4], like=1, flag=flag).update_folders_list_like()
            if sender_button.objectName() == btn_str2obj['like']:
                self.ui_mainWin.tableWidget_folder.cellWidget(row, self.ui_mainWin.tableWidget_folder.columnCount()-1).setIcon(icon)
            else:
                sender_button.setIcon(icon)
            print('done:result', result)
        except AttributeError as ae:
            print(f"Caught an AttributeError: {ae}")
            QMessageBox.warning(self, "警告", "请选择待收藏的数据项！", QMessageBox.Ok)

    # /*-------------------------@END: folder@-------------------------*/

    # /*-------------------------@BEGIN: trash@-------------------------*/
    def load_trash_data(self):
        data_trash = pyMysql(table_name=table_name[1], usr=self._usr).search_by_trash()
        print(data_trash)
        self.ui_mainWin.treeWidget_trash.clear()
        if data_trash is not None:
            head = ['FOLDER', 'URL', 'USERNAME', 'PASSWORD', 'NOTE', 'DELETE TIME']
            self.ui_mainWin.treeWidget_trash.setHeaderLabels(head)
            header = self.ui_mainWin.treeWidget_trash.header()
            self._treewidget_qss = "../ui/treeWidget_head.qss"
            qss = self.load_stylesheet(self._treewidget_qss)
            header.setStyleSheet(qss)
            try:
                self.ui_mainWin.treeWidget_trash.setColumnCount(len(data_trash[0]))
                for i in range(0, len(data_trash)):
                    # print(data_like[i])
                    data = list(data_trash[i])
                    print(data)
                    data[5] = data[5].strftime("%Y-%m-%d %H:%M:%S")
                    cell = QTreeWidgetItem(self.ui_mainWin.treeWidget_trash, data)
                    self.ui_mainWin.treeWidget_trash.addTopLevelItem(cell)
                    cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)
                for i in range(0, self.ui_mainWin.treeWidget_trash.columnCount()):
                    self.ui_mainWin.treeWidget_trash.resizeColumnToContents(i)
            except ImportError as ie:
                print(f"Caught an AttributeError: {ie}")
        else:
            print("none!")
    # /*-------------------------@END: trash@-------------------------*/


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginpm = logWin()
    loginpm.show()
    burgresspm = mainApp(loginpm)
    # burgresspm.show()
    sys.exit(app.exec())
