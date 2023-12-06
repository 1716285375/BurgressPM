# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_demo.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLCDNumber, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)
import end.ui.image_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(998, 789)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/*============================================*/\n"
"/*btn*/\n"
"#centralwidget\n"
"{\n"
"	background-color: #9292AE;\n"
"	border: 1px solid rgb(255,255,255);\n"
"}\n"
"\n"
"\n"
"/*============================================*/\n"
"/*menu_bbtn*/\n"
"#frame_bmenu QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227,253,245, 0), stop:1 rgba(255,230,250, 140));\n"
"\n"
"	border: None;\n"
"	margin-bottom: 15px;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	\n"
"	\n"
"}\n"
"#frame_bmenu QPushButton:hover\n"
"{\n"
"		background-color: rgba(227,253,245, 255);\n"
"}\n"
"#frame_bmenu QPushButton:pressed\n"
"{\n"
"		padding-left: 10px;\n"
"		padding-top: 5px;\n"
"}\n"
"\n"
"/*============================================*/\n"
"/*menu_sbtn*/\n"
"#frame_smenu QPushButton\n"
"{\n"
"	text-align: left;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227,253,245, 50), stop:1 rgba"
                        "(255,230,250, 120));\n"
"	border: None;\n"
"	margin-bottom: 15px;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	\n"
"	\n"
"}\n"
"#frame_smenu QPushButton:hover\n"
"{\n"
"		background-color: rgba(227,253,245, 255);\n"
"}\n"
"#frame_smenu QPushButton:pressed\n"
"{\n"
"		padding-left: 10px;\n"
"		padding-top: 5px;\n"
"}\n"
"/*============================================*/\n"
"/*content_top_btn*/\n"
"#frame_body  #btn_menu \n"
"{\n"
"	background-color: rgba(215,255,254, 100);\n"
"	border: None;\n"
"	border-radius: 5px;\n"
"}\n"
"#frame_body  #btn_menu:hover\n"
"{\n"
"		background-color: rgba(215,255,254, 255);\n"
"}\n"
"\n"
"/*============================================*/\n"
"/*menu_slabel*/\n"
"#frame_smenu #label_simg,#label_stitle\n"
"{\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:rgba(215,255,254, 255);\n"
"	border-radius:2px;\n"
"}\n"
"\n"
"\n"
"/*============================================*/\n"
"/*menu_blabel*/\n"
"#frame_bmenu #label_bimg\n"
"{\n"
"	background-color: r"
                        "gba(0,0,0,0);\n"
"	color: rgba(215,255,254, 255);\n"
"	border-radius:2px;\n"
"}\n"
"")
        self.gridLayout_10 = QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_smenu = QFrame(self.centralwidget)
        self.frame_smenu.setObjectName(u"frame_smenu")
        self.frame_smenu.setFrameShape(QFrame.StyledPanel)
        self.frame_smenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_smenu)
        self.verticalLayout_3.setSpacing(60)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_menu_shead = QHBoxLayout()
        self.horizontalLayout_menu_shead.setObjectName(u"horizontalLayout_menu_shead")
        self.horizontalLayout_menu_shead.setContentsMargins(-1, 0, -1, -1)
        self.label_menu_simg = QLabel(self.frame_smenu)
        self.label_menu_simg.setObjectName(u"label_menu_simg")
        font = QFont()
        font.setFamilies([u"Social Media Circled"])
        font.setPointSize(30)
        self.label_menu_simg.setFont(font)
        self.label_menu_simg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_menu_shead.addWidget(self.label_menu_simg, 0, Qt.AlignLeft)

        self.label_menu_stitle = QLabel(self.frame_smenu)
        self.label_menu_stitle.setObjectName(u"label_menu_stitle")
        font1 = QFont()
        font1.setFamilies([u"Great Vibes"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_menu_stitle.setFont(font1)
        self.label_menu_stitle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_menu_shead.addWidget(self.label_menu_stitle, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_menu_shead)

        self.verticalLayout_menu_sbtn = QVBoxLayout()
        self.verticalLayout_menu_sbtn.setSpacing(10)
        self.verticalLayout_menu_sbtn.setObjectName(u"verticalLayout_menu_sbtn")
        self.btn_shome = QPushButton(self.frame_smenu)
        self.btn_shome.setObjectName(u"btn_shome")
        font2 = QFont()
        font2.setFamilies([u"Spirax"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.btn_shome.setFont(font2)
        self.btn_shome.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_shome.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/feather/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_shome.setIcon(icon)
        self.btn_shome.setIconSize(QSize(32, 32))

        self.verticalLayout_menu_sbtn.addWidget(self.btn_shome)

        self.btn_slike = QPushButton(self.frame_smenu)
        self.btn_slike.setObjectName(u"btn_slike")
        self.btn_slike.setFont(font2)
        self.btn_slike.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/feather/star.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_slike.setIcon(icon1)
        self.btn_slike.setIconSize(QSize(32, 32))

        self.verticalLayout_menu_sbtn.addWidget(self.btn_slike)

        self.btn_strash = QPushButton(self.frame_smenu)
        self.btn_strash.setObjectName(u"btn_strash")
        font3 = QFont()
        font3.setFamilies([u"Spirax"])
        font3.setPointSize(10)
        self.btn_strash.setFont(font3)
        self.btn_strash.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/feather/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_strash.setIcon(icon2)
        self.btn_strash.setIconSize(QSize(32, 32))

        self.verticalLayout_menu_sbtn.addWidget(self.btn_strash)

        self.btn_sfolder = QPushButton(self.frame_smenu)
        self.btn_sfolder.setObjectName(u"btn_sfolder")
        self.btn_sfolder.setFont(font3)
        self.btn_sfolder.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/feather/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sfolder.setIcon(icon3)
        self.btn_sfolder.setIconSize(QSize(32, 32))

        self.verticalLayout_menu_sbtn.addWidget(self.btn_sfolder)


        self.verticalLayout_3.addLayout(self.verticalLayout_menu_sbtn)

        self.verticalSpacer_smenu_bottom = QSpacerItem(20, 249, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_smenu_bottom)

        self.btn_slogout = QPushButton(self.frame_smenu)
        self.btn_slogout.setObjectName(u"btn_slogout")
        font4 = QFont()
        font4.setFamilies([u"Spirax"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.btn_slogout.setFont(font4)
        self.btn_slogout.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/feather/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_slogout.setIcon(icon4)
        self.btn_slogout.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.btn_slogout)


        self.gridLayout_10.addWidget(self.frame_smenu, 0, 1, 1, 1)

        self.frame_body = QFrame(self.centralwidget)
        self.frame_body.setObjectName(u"frame_body")
        self.frame_body.setFrameShape(QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_body)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_head = QFrame(self.frame_body)
        self.frame_head.setObjectName(u"frame_head")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_head.sizePolicy().hasHeightForWidth())
        self.frame_head.setSizePolicy(sizePolicy)
        self.frame_head.setMaximumSize(QSize(16777215, 60))
        self.frame_head.setFrameShape(QFrame.StyledPanel)
        self.frame_head.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_head)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_head_menu = QPushButton(self.frame_head)
        self.btn_head_menu.setObjectName(u"btn_head_menu")
        self.btn_head_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_head_menu.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/feather/toggle-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icons/feather/toggle-right.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_head_menu.setIcon(icon5)
        self.btn_head_menu.setIconSize(QSize(40, 40))
        self.btn_head_menu.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_head_menu)

        self.horizontalSpacer_head_left = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_head_left)

        self.gridLayout_head_search = QGridLayout()
        self.gridLayout_head_search.setObjectName(u"gridLayout_head_search")
        self.gridLayout_head_search.setHorizontalSpacing(10)
        self.gridLayout_head_search.setVerticalSpacing(0)
        self.lineEdit_head_search = QLineEdit(self.frame_head)
        self.lineEdit_head_search.setObjectName(u"lineEdit_head_search")
        self.lineEdit_head_search.setMinimumSize(QSize(0, 35))
        font5 = QFont()
        font5.setFamilies([u"Spirax"])
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setItalic(True)
        self.lineEdit_head_search.setFont(font5)
        self.lineEdit_head_search.setMaxLength(18)

        self.gridLayout_head_search.addWidget(self.lineEdit_head_search, 0, 0, 1, 1)

        self.btn_head_search = QPushButton(self.frame_head)
        self.btn_head_search.setObjectName(u"btn_head_search")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_head_search.sizePolicy().hasHeightForWidth())
        self.btn_head_search.setSizePolicy(sizePolicy1)
        self.btn_head_search.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/feather/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_head_search.setIcon(icon6)
        self.btn_head_search.setIconSize(QSize(32, 32))

        self.gridLayout_head_search.addWidget(self.btn_head_search, 0, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_head_search)

        self.horizontalSpacer_head_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_head_right)

        self.btn_head_user = QPushButton(self.frame_head)
        self.btn_head_user.setObjectName(u"btn_head_user")
        self.btn_head_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_head_user.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/feather/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_head_user.setIcon(icon7)
        self.btn_head_user.setIconSize(QSize(60, 60))

        self.horizontalLayout.addWidget(self.btn_head_user)


        self.verticalLayout_5.addWidget(self.frame_head)

        self.frame_content = QFrame(self.frame_body)
        self.frame_content.setObjectName(u"frame_content")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(8)
        sizePolicy2.setHeightForWidth(self.frame_content.sizePolicy().hasHeightForWidth())
        self.frame_content.setSizePolicy(sizePolicy2)
        self.frame_content.setStyleSheet(u"")
        self.frame_content.setFrameShape(QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_content)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.stackedWidget_content = QStackedWidget(self.frame_content)
        self.stackedWidget_content.setObjectName(u"stackedWidget_content")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.gridLayout_2 = QGridLayout(self.page_home)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_home_main = QVBoxLayout()
        self.verticalLayout_home_main.setObjectName(u"verticalLayout_home_main")
        self.frame_home_main = QFrame(self.page_home)
        self.frame_home_main.setObjectName(u"frame_home_main")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(9)
        sizePolicy3.setHeightForWidth(self.frame_home_main.sizePolicy().hasHeightForWidth())
        self.frame_home_main.setSizePolicy(sizePolicy3)
        font6 = QFont()
        font6.setFamilies([u"\u5e7c\u5706"])
        self.frame_home_main.setFont(font6)
        self.frame_home_main.setFrameShape(QFrame.StyledPanel)
        self.frame_home_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_home_main)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_home_content_top = QHBoxLayout()
        self.horizontalLayout_home_content_top.setObjectName(u"horizontalLayout_home_content_top")
        self.label_home_title = QLabel(self.frame_home_main)
        self.label_home_title.setObjectName(u"label_home_title")
        self.label_home_title.setMinimumSize(QSize(0, 60))
        font7 = QFont()
        font7.setFamilies([u"\u9e3f\u96f7\u62d9\u4e66\u7b80\u4f53"])
        font7.setPointSize(30)
        font7.setBold(True)
        font7.setItalic(False)
        self.label_home_title.setFont(font7)

        self.horizontalLayout_home_content_top.addWidget(self.label_home_title)

        self.horizontalSpacer_3 = QSpacerItem(208, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_home_content_top.addItem(self.horizontalSpacer_3)

        self.gridLayout_home_content_right = QGridLayout()
        self.gridLayout_home_content_right.setObjectName(u"gridLayout_home_content_right")
        self.lcdNumber_2 = QLCDNumber(self.frame_home_main)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setDigitCount(1)
        self.lcdNumber_2.setProperty("value", 2.000000000000000)

        self.gridLayout_home_content_right.addWidget(self.lcdNumber_2, 0, 1, 1, 1)

        self.lcdNumber_3 = QLCDNumber(self.frame_home_main)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        self.lcdNumber_3.setDigitCount(1)
        self.lcdNumber_3.setProperty("value", 2.000000000000000)

        self.gridLayout_home_content_right.addWidget(self.lcdNumber_3, 0, 3, 1, 1)

        self.label_home_colon = QLabel(self.frame_home_main)
        self.label_home_colon.setObjectName(u"label_home_colon")
        font8 = QFont()
        font8.setFamilies([u"Algerian"])
        font8.setPointSize(10)
        font8.setBold(True)
        self.label_home_colon.setFont(font8)
        self.label_home_colon.setAlignment(Qt.AlignCenter)

        self.gridLayout_home_content_right.addWidget(self.label_home_colon, 0, 2, 1, 1)

        self.lcdNumber_4 = QLCDNumber(self.frame_home_main)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")
        self.lcdNumber_4.setDigitCount(1)
        self.lcdNumber_4.setProperty("value", 2.000000000000000)

        self.gridLayout_home_content_right.addWidget(self.lcdNumber_4, 0, 4, 1, 1)

        self.lcdNumber_1 = QLCDNumber(self.frame_home_main)
        self.lcdNumber_1.setObjectName(u"lcdNumber_1")
        self.lcdNumber_1.setFont(font3)
        self.lcdNumber_1.setDigitCount(1)
        self.lcdNumber_1.setProperty("value", 1.000000000000000)

        self.gridLayout_home_content_right.addWidget(self.lcdNumber_1, 0, 0, 1, 1)


        self.horizontalLayout_home_content_top.addLayout(self.gridLayout_home_content_right)


        self.verticalLayout_9.addLayout(self.horizontalLayout_home_content_top)

        self.frame_home_content = QFrame(self.frame_home_main)
        self.frame_home_content.setObjectName(u"frame_home_content")
        self.frame_home_content.setFrameShape(QFrame.StyledPanel)
        self.frame_home_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_home_content)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.frame_home_search = QFrame(self.frame_home_content)
        self.frame_home_search.setObjectName(u"frame_home_search")
        self.frame_home_search.setFrameShape(QFrame.StyledPanel)
        self.frame_home_search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_home_search)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_home_search = QHBoxLayout()
        self.horizontalLayout_home_search.setObjectName(u"horizontalLayout_home_search")
        self.gridLayout_home_search_left = QGridLayout()
        self.gridLayout_home_search_left.setObjectName(u"gridLayout_home_search_left")
        self.label_home_url = QLabel(self.frame_home_search)
        self.label_home_url.setObjectName(u"label_home_url")
        self.label_home_url.setAlignment(Qt.AlignCenter)

        self.gridLayout_home_search_left.addWidget(self.label_home_url, 0, 0, 1, 1)

        self.lineEdit_home_url = QLineEdit(self.frame_home_search)
        self.lineEdit_home_url.setObjectName(u"lineEdit_home_url")
        self.lineEdit_home_url.setMinimumSize(QSize(0, 30))

        self.gridLayout_home_search_left.addWidget(self.lineEdit_home_url, 0, 1, 1, 1)

        self.label_home_usr = QLabel(self.frame_home_search)
        self.label_home_usr.setObjectName(u"label_home_usr")
        self.label_home_usr.setAlignment(Qt.AlignCenter)

        self.gridLayout_home_search_left.addWidget(self.label_home_usr, 1, 0, 1, 1)

        self.lineEdit_home_usr = QLineEdit(self.frame_home_search)
        self.lineEdit_home_usr.setObjectName(u"lineEdit_home_usr")
        self.lineEdit_home_usr.setMinimumSize(QSize(0, 30))

        self.gridLayout_home_search_left.addWidget(self.lineEdit_home_usr, 1, 1, 1, 1)

        self.label_home_pwd = QLabel(self.frame_home_search)
        self.label_home_pwd.setObjectName(u"label_home_pwd")
        self.label_home_pwd.setAlignment(Qt.AlignCenter)

        self.gridLayout_home_search_left.addWidget(self.label_home_pwd, 2, 0, 1, 1)

        self.lineEdit_home_pwd = QLineEdit(self.frame_home_search)
        self.lineEdit_home_pwd.setObjectName(u"lineEdit_home_pwd")
        self.lineEdit_home_pwd.setMinimumSize(QSize(0, 30))

        self.gridLayout_home_search_left.addWidget(self.lineEdit_home_pwd, 2, 1, 1, 1)


        self.horizontalLayout_home_search.addLayout(self.gridLayout_home_search_left)

        self.gridLayout_home_search_right = QGridLayout()
        self.gridLayout_home_search_right.setObjectName(u"gridLayout_home_search_right")
        self.label_home_note = QLabel(self.frame_home_search)
        self.label_home_note.setObjectName(u"label_home_note")
        self.label_home_note.setAlignment(Qt.AlignCenter)

        self.gridLayout_home_search_right.addWidget(self.label_home_note, 0, 0, 1, 1)

        self.lineEdit_home_note = QLineEdit(self.frame_home_search)
        self.lineEdit_home_note.setObjectName(u"lineEdit_home_note")
        self.lineEdit_home_note.setMinimumSize(QSize(0, 30))

        self.gridLayout_home_search_right.addWidget(self.lineEdit_home_note, 0, 1, 1, 1)

        self.label_home_time = QLabel(self.frame_home_search)
        self.label_home_time.setObjectName(u"label_home_time")
        self.label_home_time.setAlignment(Qt.AlignCenter)

        self.gridLayout_home_search_right.addWidget(self.label_home_time, 1, 0, 1, 1)

        self.lineEdit_home_time = QLineEdit(self.frame_home_search)
        self.lineEdit_home_time.setObjectName(u"lineEdit_home_time")
        self.lineEdit_home_time.setMinimumSize(QSize(0, 30))

        self.gridLayout_home_search_right.addWidget(self.lineEdit_home_time, 1, 1, 1, 1)

        self.label_home_folder = QLabel(self.frame_home_search)
        self.label_home_folder.setObjectName(u"label_home_folder")
        self.label_home_folder.setAlignment(Qt.AlignCenter)

        self.gridLayout_home_search_right.addWidget(self.label_home_folder, 2, 0, 1, 1)

        self.lineEdit_home_folder = QLineEdit(self.frame_home_search)
        self.lineEdit_home_folder.setObjectName(u"lineEdit_home_folder")
        self.lineEdit_home_folder.setMinimumSize(QSize(0, 30))

        self.gridLayout_home_search_right.addWidget(self.lineEdit_home_folder, 2, 1, 1, 1)


        self.horizontalLayout_home_search.addLayout(self.gridLayout_home_search_right)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_home_search)


        self.verticalLayout_4.addWidget(self.frame_home_search)

        self.frame_home_select = QFrame(self.frame_home_content)
        self.frame_home_select.setObjectName(u"frame_home_select")
        self.frame_home_select.setFrameShape(QFrame.StyledPanel)
        self.frame_home_select.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_home_select)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_home_select = QHBoxLayout()
        self.horizontalLayout_home_select.setObjectName(u"horizontalLayout_home_select")
        self.horizontalSpacer_home_select = QSpacerItem(178, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_home_select.addItem(self.horizontalSpacer_home_select)

        self.btn_home_select = QPushButton(self.frame_home_select)
        self.btn_home_select.setObjectName(u"btn_home_select")

        self.horizontalLayout_home_select.addWidget(self.btn_home_select)

        self.btn_home_clear = QPushButton(self.frame_home_select)
        self.btn_home_clear.setObjectName(u"btn_home_clear")

        self.horizontalLayout_home_select.addWidget(self.btn_home_clear)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_home_select)


        self.verticalLayout_4.addWidget(self.frame_home_select)

        self.tableWidget_home = QTableWidget(self.frame_home_content)
        if (self.tableWidget_home.columnCount() < 7):
            self.tableWidget_home.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_home.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_home.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_home.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_home.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_home.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_home.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_home.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget_home.setObjectName(u"tableWidget_home")

        self.verticalLayout_4.addWidget(self.tableWidget_home)


        self.verticalLayout_9.addWidget(self.frame_home_content)

        self.label_home_say = QLabel(self.frame_home_main)
        self.label_home_say.setObjectName(u"label_home_say")
        font9 = QFont()
        font9.setFamilies([u"\u534e\u6587\u5f69\u4e91"])
        font9.setPointSize(12)
        self.label_home_say.setFont(font9)
        self.label_home_say.setLayoutDirection(Qt.RightToLeft)
        self.label_home_say.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.label_home_say)


        self.verticalLayout_home_main.addWidget(self.frame_home_main)

        self.frame_home_bottom = QFrame(self.page_home)
        self.frame_home_bottom.setObjectName(u"frame_home_bottom")
        sizePolicy.setHeightForWidth(self.frame_home_bottom.sizePolicy().hasHeightForWidth())
        self.frame_home_bottom.setSizePolicy(sizePolicy)
        self.frame_home_bottom.setMaximumSize(QSize(16777215, 30))
        self.frame_home_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_home_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_home_bottom)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_home_left = QLabel(self.frame_home_bottom)
        self.label_home_left.setObjectName(u"label_home_left")
        font10 = QFont()
        font10.setFamilies([u"\u6977\u4f53"])
        font10.setPointSize(7)
        self.label_home_left.setFont(font10)

        self.horizontalLayout_6.addWidget(self.label_home_left)

        self.horizontalSpacer_home_bottom_right = QSpacerItem(469, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_home_bottom_right)

        self.horizontalLayout_home_bottom_label = QHBoxLayout()
        self.horizontalLayout_home_bottom_label.setSpacing(10)
        self.horizontalLayout_home_bottom_label.setObjectName(u"horizontalLayout_home_bottom_label")
        self.label = QLabel(self.frame_home_bottom)
        self.label.setObjectName(u"label")
        font11 = QFont()
        font11.setFamilies([u"Social Media Circled"])
        font11.setPointSize(14)
        self.label.setFont(font11)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_home_bottom_label.addWidget(self.label)

        self.label_2 = QLabel(self.frame_home_bottom)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font11)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_home_bottom_label.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_home_bottom)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font11)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_home_bottom_label.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_home_bottom)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font11)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_home_bottom_label.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_home_bottom_label)


        self.verticalLayout_home_main.addWidget(self.frame_home_bottom)


        self.gridLayout_2.addLayout(self.verticalLayout_home_main, 0, 0, 1, 1)

        self.stackedWidget_content.addWidget(self.page_home)
        self.page_like = QWidget()
        self.page_like.setObjectName(u"page_like")
        self.gridLayout_6 = QGridLayout(self.page_like)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_like = QFrame(self.page_like)
        self.frame_like.setObjectName(u"frame_like")
        self.frame_like.setFrameShape(QFrame.StyledPanel)
        self.frame_like.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_like)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.treeWidget_like = QTreeWidget(self.frame_like)
        self.treeWidget_like.setObjectName(u"treeWidget_like")
        self.treeWidget_like.setAlternatingRowColors(True)
        self.treeWidget_like.setAnimated(False)
        self.treeWidget_like.header().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.treeWidget_like, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_like, 0, 0, 1, 1)

        self.stackedWidget_content.addWidget(self.page_like)
        self.page_trash = QWidget()
        self.page_trash.setObjectName(u"page_trash")
        self.gridLayout_8 = QGridLayout(self.page_trash)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_trash_head = QFrame(self.page_trash)
        self.frame_trash_head.setObjectName(u"frame_trash_head")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.frame_trash_head.sizePolicy().hasHeightForWidth())
        self.frame_trash_head.setSizePolicy(sizePolicy4)
        self.frame_trash_head.setFrameShape(QFrame.StyledPanel)
        self.frame_trash_head.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_trash_head)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_head_top = QLabel(self.frame_trash_head)
        self.label_head_top.setObjectName(u"label_head_top")
        font12 = QFont()
        font12.setFamilies([u"\u9e3f\u96f7\u62d9\u4e66\u7b80\u4f53"])
        self.label_head_top.setFont(font12)

        self.verticalLayout_8.addWidget(self.label_head_top)

        self.verticalSpacer_head_center = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_head_center)

        self.frame_trash_head_main = QFrame(self.frame_trash_head)
        self.frame_trash_head_main.setObjectName(u"frame_trash_head_main")
        self.frame_trash_head_main.setFrameShape(QFrame.StyledPanel)
        self.frame_trash_head_main.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_trash_head_main)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_head_content = QHBoxLayout()
        self.horizontalLayout_head_content.setObjectName(u"horizontalLayout_head_content")
        self.btn_head_edit = QPushButton(self.frame_trash_head_main)
        self.btn_head_edit.setObjectName(u"btn_head_edit")
        font13 = QFont()
        font13.setFamilies([u"YuFanXinYu"])
        font13.setPointSize(14)
        font13.setBold(True)
        self.btn_head_edit.setFont(font13)
        self.btn_head_edit.setCheckable(True)

        self.horizontalLayout_head_content.addWidget(self.btn_head_edit)

        self.horizontalSpacer_head_content_center = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_head_content.addItem(self.horizontalSpacer_head_content_center)

        self.frame_head_left = QFrame(self.frame_trash_head_main)
        self.frame_head_left.setObjectName(u"frame_head_left")
        self.frame_head_left.setFrameShape(QFrame.StyledPanel)
        self.frame_head_left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_head_left)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_head_left = QHBoxLayout()
        self.horizontalLayout_head_left.setObjectName(u"horizontalLayout_head_left")
        self.btn_head_recover = QPushButton(self.frame_head_left)
        self.btn_head_recover.setObjectName(u"btn_head_recover")
        self.btn_head_recover.setFont(font13)

        self.horizontalLayout_head_left.addWidget(self.btn_head_recover)

        self.btn_head_recoverall = QPushButton(self.frame_head_left)
        self.btn_head_recoverall.setObjectName(u"btn_head_recoverall")
        self.btn_head_recoverall.setFont(font13)

        self.horizontalLayout_head_left.addWidget(self.btn_head_recoverall)

        self.btn_head_delete = QPushButton(self.frame_head_left)
        self.btn_head_delete.setObjectName(u"btn_head_delete")
        self.btn_head_delete.setFont(font13)

        self.horizontalLayout_head_left.addWidget(self.btn_head_delete)

        self.btn_head_deleteall = QPushButton(self.frame_head_left)
        self.btn_head_deleteall.setObjectName(u"btn_head_deleteall")
        self.btn_head_deleteall.setFont(font13)

        self.horizontalLayout_head_left.addWidget(self.btn_head_deleteall)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_head_left)


        self.horizontalLayout_head_content.addWidget(self.frame_head_left)


        self.gridLayout_7.addLayout(self.horizontalLayout_head_content, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_trash_head_main)


        self.gridLayout_8.addWidget(self.frame_trash_head, 0, 0, 1, 1)

        self.frame_trash_body = QFrame(self.page_trash)
        self.frame_trash_body.setObjectName(u"frame_trash_body")
        sizePolicy2.setHeightForWidth(self.frame_trash_body.sizePolicy().hasHeightForWidth())
        self.frame_trash_body.setSizePolicy(sizePolicy2)
        self.frame_trash_body.setFrameShape(QFrame.StyledPanel)
        self.frame_trash_body.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_trash_body)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.treeWidget_trash = QTreeWidget(self.frame_trash_body)
        self.treeWidget_trash.setObjectName(u"treeWidget_trash")
        self.treeWidget_trash.setAllColumnsShowFocus(False)
        self.treeWidget_trash.header().setVisible(True)
        self.treeWidget_trash.header().setStretchLastSection(False)

        self.gridLayout_9.addWidget(self.treeWidget_trash, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_trash_body, 1, 0, 1, 1)

        self.stackedWidget_content.addWidget(self.page_trash)
        self.page_folder = QWidget()
        self.page_folder.setObjectName(u"page_folder")
        self.gridLayout = QGridLayout(self.page_folder)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_folder_main = QVBoxLayout()
        self.verticalLayout_folder_main.setObjectName(u"verticalLayout_folder_main")
        self.frame_folder_head = QFrame(self.page_folder)
        self.frame_folder_head.setObjectName(u"frame_folder_head")
        self.frame_folder_head.setFrameShape(QFrame.StyledPanel)
        self.frame_folder_head.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_folder_head)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_folder_edit = QPushButton(self.frame_folder_head)
        self.btn_folder_edit.setObjectName(u"btn_folder_edit")
        self.btn_folder_edit.setFont(font13)
        self.btn_folder_edit.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/feather/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_folder_edit.setIcon(icon8)
        self.btn_folder_edit.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_folder_edit)

        self.btn_folder_refresh = QPushButton(self.frame_folder_head)
        self.btn_folder_refresh.setObjectName(u"btn_folder_refresh")
        self.btn_folder_refresh.setFont(font13)
        self.btn_folder_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/feather/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_folder_refresh.setIcon(icon9)
        self.btn_folder_refresh.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_folder_refresh)

        self.btn_folder_copy = QPushButton(self.frame_folder_head)
        self.btn_folder_copy.setObjectName(u"btn_folder_copy")
        self.btn_folder_copy.setFont(font13)
        self.btn_folder_copy.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/feather/copy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_folder_copy.setIcon(icon10)
        self.btn_folder_copy.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_folder_copy)

        self.horizontalSpacer_folder_head = QSpacerItem(405, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_folder_head)

        self.btn_folder_tool = QPushButton(self.frame_folder_head)
        self.btn_folder_tool.setObjectName(u"btn_folder_tool")
        self.btn_folder_tool.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/feather/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u":/icons/feather/arrow-down-circle.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_folder_tool.setIcon(icon11)
        self.btn_folder_tool.setIconSize(QSize(32, 32))
        self.btn_folder_tool.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btn_folder_tool)


        self.verticalLayout_folder_main.addWidget(self.frame_folder_head)

        self.gridLayout_folder_content = QGridLayout()
        self.gridLayout_folder_content.setObjectName(u"gridLayout_folder_content")
        self.frame_folder_table = QFrame(self.page_folder)
        self.frame_folder_table.setObjectName(u"frame_folder_table")
        font14 = QFont()
        font14.setPointSize(10)
        self.frame_folder_table.setFont(font14)
        self.frame_folder_table.setStyleSheet(u"")
        self.frame_folder_table.setFrameShape(QFrame.StyledPanel)
        self.frame_folder_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_folder_table)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 48, 0, 0)
        self.tableWidget_folder = QTableWidget(self.frame_folder_table)
        if (self.tableWidget_folder.columnCount() < 6):
            self.tableWidget_folder.setColumnCount(6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_folder.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_folder.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_folder.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_folder.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_folder.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_folder.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        self.tableWidget_folder.setObjectName(u"tableWidget_folder")
        self.tableWidget_folder.setAlternatingRowColors(True)
        self.tableWidget_folder.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_folder.setSortingEnabled(False)
        self.tableWidget_folder.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_folder.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_folder.verticalHeader().setVisible(False)
        self.tableWidget_folder.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_7.addWidget(self.tableWidget_folder)


        self.gridLayout_folder_content.addWidget(self.frame_folder_table, 0, 1, 1, 1)

        self.frame_folder_right = QFrame(self.page_folder)
        self.frame_folder_right.setObjectName(u"frame_folder_right")
        self.frame_folder_right.setFrameShape(QFrame.StyledPanel)
        self.frame_folder_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_folder_right)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_folder_right_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_folder_right_top)

        self.verticalLayout_right_tool = QVBoxLayout()
        self.verticalLayout_right_tool.setSpacing(4)
        self.verticalLayout_right_tool.setObjectName(u"verticalLayout_right_tool")
        self.btn_folder_add = QPushButton(self.frame_folder_right)
        self.btn_folder_add.setObjectName(u"btn_folder_add")
        font15 = QFont()
        font15.setFamilies([u"YuFanXinYu"])
        font15.setPointSize(14)
        font15.setBold(True)
        font15.setItalic(False)
        self.btn_folder_add.setFont(font15)
        self.btn_folder_add.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/feather/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_folder_add.setIcon(icon12)
        self.btn_folder_add.setIconSize(QSize(32, 32))

        self.verticalLayout_right_tool.addWidget(self.btn_folder_add)

        self.btn_folder_delete = QPushButton(self.frame_folder_right)
        self.btn_folder_delete.setObjectName(u"btn_folder_delete")
        self.btn_folder_delete.setFont(font13)
        self.btn_folder_delete.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/feather/divide-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_folder_delete.setIcon(icon13)
        self.btn_folder_delete.setIconSize(QSize(32, 32))

        self.verticalLayout_right_tool.addWidget(self.btn_folder_delete)

        self.btn_folder_like = QPushButton(self.frame_folder_right)
        self.btn_folder_like.setObjectName(u"btn_folder_like")
        self.btn_folder_like.setFont(font13)
        self.btn_folder_like.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/feather/heart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_folder_like.setIcon(icon14)
        self.btn_folder_like.setIconSize(QSize(32, 32))

        self.verticalLayout_right_tool.addWidget(self.btn_folder_like)


        self.verticalLayout_6.addLayout(self.verticalLayout_right_tool)

        self.verticalSpacer_folder_right_center = QSpacerItem(20, 167, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_folder_right_center)

        self.horizontalLayout_folder_img = QHBoxLayout()
        self.horizontalLayout_folder_img.setSpacing(0)
        self.horizontalLayout_folder_img.setObjectName(u"horizontalLayout_folder_img")
        self.label_folder_img = QLabel(self.frame_folder_right)
        self.label_folder_img.setObjectName(u"label_folder_img")
        font16 = QFont()
        font16.setFamilies([u"Social Media Circled"])
        font16.setPointSize(25)
        self.label_folder_img.setFont(font16)
        self.label_folder_img.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_folder_img.addWidget(self.label_folder_img)


        self.verticalLayout_6.addLayout(self.horizontalLayout_folder_img)

        self.verticalLayout_6.setStretch(0, 2)
        self.verticalLayout_6.setStretch(2, 4)

        self.gridLayout_folder_content.addWidget(self.frame_folder_right, 0, 2, 1, 1, Qt.AlignTop)

        self.frame_folder_left = QFrame(self.page_folder)
        self.frame_folder_left.setObjectName(u"frame_folder_left")
        self.frame_folder_left.setFrameShape(QFrame.StyledPanel)
        self.frame_folder_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_folder_left)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_folder_list_top = QHBoxLayout()
        self.horizontalLayout_folder_list_top.setSpacing(6)
        self.horizontalLayout_folder_list_top.setObjectName(u"horizontalLayout_folder_list_top")
        self.btn_folder_all = QPushButton(self.frame_folder_left)
        self.btn_folder_all.setObjectName(u"btn_folder_all")
        font17 = QFont()
        font17.setFamilies([u"YuFanXinYu"])
        font17.setPointSize(16)
        font17.setBold(True)
        self.btn_folder_all.setFont(font17)
        icon15 = QIcon()
        icon15.addFile(u":/icons/feather/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_folder_all.setIcon(icon15)
        self.btn_folder_all.setIconSize(QSize(32, 32))

        self.horizontalLayout_folder_list_top.addWidget(self.btn_folder_all)

        self.horizontalSpacer_folder_btn_top = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_folder_list_top.addItem(self.horizontalSpacer_folder_btn_top)

        self.btn_folder_showall = QPushButton(self.frame_folder_left)
        self.btn_folder_showall.setObjectName(u"btn_folder_showall")
        self.btn_folder_showall.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/icons/feather/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon16.addFile(u":/icons/feather/chevron-left.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_folder_showall.setIcon(icon16)
        self.btn_folder_showall.setIconSize(QSize(20, 20))
        self.btn_folder_showall.setCheckable(True)

        self.horizontalLayout_folder_list_top.addWidget(self.btn_folder_showall)


        self.verticalLayout.addLayout(self.horizontalLayout_folder_list_top)

        self.listWidget_folder = QListWidget(self.frame_folder_left)
        self.listWidget_folder.setObjectName(u"listWidget_folder")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(4)
        sizePolicy5.setHeightForWidth(self.listWidget_folder.sizePolicy().hasHeightForWidth())
        self.listWidget_folder.setSizePolicy(sizePolicy5)
        self.listWidget_folder.setMinimumSize(QSize(0, 0))
        font18 = QFont()
        font18.setFamilies([u"\u9e3f\u96f7\u62d9\u4e66\u7b80\u4f53"])
        font18.setPointSize(12)
        font18.setBold(False)
        self.listWidget_folder.setFont(font18)
        self.listWidget_folder.setStyleSheet(u"QListWidget {\n"
"    background-color: #f7f7f7; /* \u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: #ffffff; /* \u767d\u8272\u5217\u8868\u9879\u80cc\u666f */\n"
"    border: 1px solid #d1d1d1; /* \u5217\u8868\u9879\u8fb9\u6846 */\n"
"    padding: 10px; /* \u5217\u8868\u9879\u5185\u8fb9\u8ddd */\n"
"    color: #333333; /* \u5217\u8868\u9879\u6587\u5b57\u989c\u8272 */\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #a0c4ff; /* \u9009\u4e2d\u5217\u8868\u9879\u7684\u6de1\u84dd\u8272\u80cc\u666f */\n"
"    color: #ffffff; /* \u9009\u4e2d\u5217\u8868\u9879\u7684\u767d\u8272\u6587\u5b57 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.listWidget_folder)

        self.verticalSpacer_folder_left_center = QSpacerItem(20, 66, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_folder_left_center)

        self.horizontalLayout_folder_btn_bottom = QHBoxLayout()
        self.horizontalLayout_folder_btn_bottom.setSpacing(0)
        self.horizontalLayout_folder_btn_bottom.setObjectName(u"horizontalLayout_folder_btn_bottom")
        self.btn_folder_list_add = QPushButton(self.frame_folder_left)
        self.btn_folder_list_add.setObjectName(u"btn_folder_list_add")
        self.btn_folder_list_add.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/icons/feather/folder-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_folder_list_add.setIcon(icon17)
        self.btn_folder_list_add.setIconSize(QSize(32, 32))

        self.horizontalLayout_folder_btn_bottom.addWidget(self.btn_folder_list_add)

        self.horizontalSpacer_folder_list_center = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_folder_btn_bottom.addItem(self.horizontalSpacer_folder_list_center)

        self.btn_folder_list_delete = QPushButton(self.frame_folder_left)
        self.btn_folder_list_delete.setObjectName(u"btn_folder_list_delete")
        self.btn_folder_list_delete.setCursor(QCursor(Qt.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u":/icons/feather/folder-minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_folder_list_delete.setIcon(icon18)
        self.btn_folder_list_delete.setIconSize(QSize(32, 32))

        self.horizontalLayout_folder_btn_bottom.addWidget(self.btn_folder_list_delete)


        self.verticalLayout.addLayout(self.horizontalLayout_folder_btn_bottom)


        self.gridLayout_folder_content.addWidget(self.frame_folder_left, 0, 0, 1, 1)

        self.gridLayout_folder_content.setColumnStretch(0, 1)
        self.gridLayout_folder_content.setColumnStretch(1, 7)

        self.verticalLayout_folder_main.addLayout(self.gridLayout_folder_content)


        self.gridLayout.addLayout(self.verticalLayout_folder_main, 0, 0, 1, 1)

        self.stackedWidget_content.addWidget(self.page_folder)
        self.page_user = QWidget()
        self.page_user.setObjectName(u"page_user")
        self.gridLayout_4 = QGridLayout(self.page_user)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_user_main = QVBoxLayout()
        self.verticalLayout_user_main.setObjectName(u"verticalLayout_user_main")
        self.verticalSpacer_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_user_main.addItem(self.verticalSpacer_top)

        self.horizontalLayout_user_content = QHBoxLayout()
        self.horizontalLayout_user_content.setSpacing(0)
        self.horizontalLayout_user_content.setObjectName(u"horizontalLayout_user_content")
        self.horizontalSpacer_user_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_user_content.addItem(self.horizontalSpacer_user_left)

        self.frame_user_content = QFrame(self.page_user)
        self.frame_user_content.setObjectName(u"frame_user_content")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_user_content.sizePolicy().hasHeightForWidth())
        self.frame_user_content.setSizePolicy(sizePolicy6)
        self.frame_user_content.setMinimumSize(QSize(400, 500))
        self.frame_user_content.setStyleSheet(u"")
        self.frame_user_content.setFrameShape(QFrame.StyledPanel)
        self.frame_user_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_user_content)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_user_content = QVBoxLayout()
        self.verticalLayout_user_content.setObjectName(u"verticalLayout_user_content")
        self.groupBox_user_content = QGroupBox(self.frame_user_content)
        self.groupBox_user_content.setObjectName(u"groupBox_user_content")
        font19 = QFont()
        font19.setFamilies([u"Great Vibes"])
        font19.setPointSize(33)
        font19.setBold(True)
        font19.setItalic(True)
        self.groupBox_user_content.setFont(font19)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_user_content)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, -1, 20, 0)
        self.verticalSpacer_user_content_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_user_content_top)

        self.gridLayout_user_information = QGridLayout()
        self.gridLayout_user_information.setObjectName(u"gridLayout_user_information")
        self.gridLayout_user_information.setVerticalSpacing(20)
        self.gridLayout_user_information.setContentsMargins(20, 6, -1, 6)
        self.label_user_username = QLabel(self.groupBox_user_content)
        self.label_user_username.setObjectName(u"label_user_username")
        self.label_user_username.setFont(font17)
        self.label_user_username.setLayoutDirection(Qt.LeftToRight)
        self.label_user_username.setAlignment(Qt.AlignCenter)

        self.gridLayout_user_information.addWidget(self.label_user_username, 0, 0, 1, 1)

        self.lineEdit_user_username = QLineEdit(self.groupBox_user_content)
        self.lineEdit_user_username.setObjectName(u"lineEdit_user_username")
        self.lineEdit_user_username.setMinimumSize(QSize(0, 30))

        self.gridLayout_user_information.addWidget(self.lineEdit_user_username, 0, 1, 1, 2)

        self.label_user_password = QLabel(self.groupBox_user_content)
        self.label_user_password.setObjectName(u"label_user_password")
        self.label_user_password.setFont(font17)
        self.label_user_password.setAlignment(Qt.AlignCenter)

        self.gridLayout_user_information.addWidget(self.label_user_password, 1, 0, 1, 1)

        self.lineEdit_user_password = QLineEdit(self.groupBox_user_content)
        self.lineEdit_user_password.setObjectName(u"lineEdit_user_password")
        self.lineEdit_user_password.setMinimumSize(QSize(0, 30))

        self.gridLayout_user_information.addWidget(self.lineEdit_user_password, 1, 1, 1, 2)

        self.label_user_address = QLabel(self.groupBox_user_content)
        self.label_user_address.setObjectName(u"label_user_address")
        self.label_user_address.setFont(font17)
        self.label_user_address.setLayoutDirection(Qt.LeftToRight)
        self.label_user_address.setAlignment(Qt.AlignCenter)

        self.gridLayout_user_information.addWidget(self.label_user_address, 2, 0, 1, 1)

        self.lineEdit_user_address = QLineEdit(self.groupBox_user_content)
        self.lineEdit_user_address.setObjectName(u"lineEdit_user_address")
        self.lineEdit_user_address.setMinimumSize(QSize(0, 30))

        self.gridLayout_user_information.addWidget(self.lineEdit_user_address, 2, 1, 1, 2)

        self.label_user_sex = QLabel(self.groupBox_user_content)
        self.label_user_sex.setObjectName(u"label_user_sex")
        self.label_user_sex.setFont(font17)
        self.label_user_sex.setAlignment(Qt.AlignCenter)

        self.gridLayout_user_information.addWidget(self.label_user_sex, 3, 0, 1, 1)

        self.radioButton_user_man = QRadioButton(self.groupBox_user_content)
        self.radioButton_user_man.setObjectName(u"radioButton_user_man")
        self.radioButton_user_man.setMinimumSize(QSize(0, 30))
        font20 = QFont()
        font20.setFamilies([u"YuFanXinYu"])
        font20.setPointSize(12)
        font20.setBold(True)
        self.radioButton_user_man.setFont(font20)
        self.radioButton_user_man.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_user_information.addWidget(self.radioButton_user_man, 3, 1, 1, 1)

        self.radioButton_user_woman = QRadioButton(self.groupBox_user_content)
        self.radioButton_user_woman.setObjectName(u"radioButton_user_woman")
        self.radioButton_user_woman.setMinimumSize(QSize(0, 30))
        self.radioButton_user_woman.setFont(font20)

        self.gridLayout_user_information.addWidget(self.radioButton_user_woman, 3, 2, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_user_information)

        self.horizontalSpacer_user_content_bottom = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_10.addItem(self.horizontalSpacer_user_content_bottom)


        self.verticalLayout_user_content.addWidget(self.groupBox_user_content)

        self.verticalSpacer_user_content_center = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_user_content.addItem(self.verticalSpacer_user_content_center)

        self.horizontalLayout_user_btn_edit = QHBoxLayout()
        self.horizontalLayout_user_btn_edit.setObjectName(u"horizontalLayout_user_btn_edit")
        self.horizontalSpacer_user_btn_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_user_btn_edit.addItem(self.horizontalSpacer_user_btn_left)

        self.btn_user_modify = QPushButton(self.frame_user_content)
        self.btn_user_modify.setObjectName(u"btn_user_modify")
        self.btn_user_modify.setMinimumSize(QSize(60, 30))
        font21 = QFont()
        font21.setFamilies([u"\u9e3f\u96f7\u62d9\u4e66\u7b80\u4f53"])
        font21.setPointSize(16)
        font21.setBold(True)
        font21.setItalic(False)
        self.btn_user_modify.setFont(font21)
        self.btn_user_modify.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_user_btn_edit.addWidget(self.btn_user_modify)

        self.horizontalSpacer_user_btn_center = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_user_btn_edit.addItem(self.horizontalSpacer_user_btn_center)

        self.btn_user_save = QPushButton(self.frame_user_content)
        self.btn_user_save.setObjectName(u"btn_user_save")
        self.btn_user_save.setMinimumSize(QSize(60, 30))
        font22 = QFont()
        font22.setFamilies([u"\u9e3f\u96f7\u62d9\u4e66\u7b80\u4f53"])
        font22.setPointSize(16)
        font22.setBold(True)
        self.btn_user_save.setFont(font22)
        self.btn_user_save.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_user_btn_edit.addWidget(self.btn_user_save)

        self.horizontalSpacer_user_btn_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_user_btn_edit.addItem(self.horizontalSpacer_user_btn_right)


        self.verticalLayout_user_content.addLayout(self.horizontalLayout_user_btn_edit)

        self.verticalSpacer_user_content_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_user_content.addItem(self.verticalSpacer_user_content_bottom)


        self.horizontalLayout_11.addLayout(self.verticalLayout_user_content)


        self.horizontalLayout_user_content.addWidget(self.frame_user_content)

        self.horizontalSpacer_user_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_user_content.addItem(self.horizontalSpacer_user_right)


        self.verticalLayout_user_main.addLayout(self.horizontalLayout_user_content)

        self.verticalSpacer_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_user_main.addItem(self.verticalSpacer_bottom)


        self.gridLayout_4.addLayout(self.verticalLayout_user_main, 0, 0, 1, 1)

        self.stackedWidget_content.addWidget(self.page_user)

        self.gridLayout_5.addWidget(self.stackedWidget_content, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_content)


        self.gridLayout_10.addWidget(self.frame_body, 0, 2, 1, 1)

        self.frame_bmenu = QFrame(self.centralwidget)
        self.frame_bmenu.setObjectName(u"frame_bmenu")
        self.frame_bmenu.setFrameShape(QFrame.StyledPanel)
        self.frame_bmenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_bmenu)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_menu_bhead = QHBoxLayout()
        self.horizontalLayout_menu_bhead.setObjectName(u"horizontalLayout_menu_bhead")
        self.label_menu_bimg = QLabel(self.frame_bmenu)
        self.label_menu_bimg.setObjectName(u"label_menu_bimg")
        font23 = QFont()
        font23.setFamilies([u"Social Media Circled"])
        font23.setPointSize(40)
        self.label_menu_bimg.setFont(font23)
        self.label_menu_bimg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_menu_bhead.addWidget(self.label_menu_bimg)


        self.verticalLayout_2.addLayout(self.horizontalLayout_menu_bhead)

        self.verticalLayout_bbtn = QVBoxLayout()
        self.verticalLayout_bbtn.setObjectName(u"verticalLayout_bbtn")
        self.verticalLayout_bbtn.setContentsMargins(-1, 0, -1, -1)
        self.btn_bhome = QPushButton(self.frame_bmenu)
        self.btn_bhome.setObjectName(u"btn_bhome")
        self.btn_bhome.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_bhome.setStyleSheet(u"")
        self.btn_bhome.setIcon(icon)
        self.btn_bhome.setIconSize(QSize(50, 50))

        self.verticalLayout_bbtn.addWidget(self.btn_bhome)

        self.btn_blike = QPushButton(self.frame_bmenu)
        self.btn_blike.setObjectName(u"btn_blike")
        self.btn_blike.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_blike.setIcon(icon1)
        self.btn_blike.setIconSize(QSize(50, 50))

        self.verticalLayout_bbtn.addWidget(self.btn_blike)

        self.btn_btrash = QPushButton(self.frame_bmenu)
        self.btn_btrash.setObjectName(u"btn_btrash")
        self.btn_btrash.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_btrash.setIcon(icon2)
        self.btn_btrash.setIconSize(QSize(50, 50))

        self.verticalLayout_bbtn.addWidget(self.btn_btrash)

        self.btn_bfolder = QPushButton(self.frame_bmenu)
        self.btn_bfolder.setObjectName(u"btn_bfolder")
        self.btn_bfolder.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_bfolder.setIcon(icon3)
        self.btn_bfolder.setIconSize(QSize(50, 50))

        self.verticalLayout_bbtn.addWidget(self.btn_bfolder)


        self.verticalLayout_2.addLayout(self.verticalLayout_bbtn)

        self.verticalSpacer_bmenu_center = QSpacerItem(20, 258, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_bmenu_center)

        self.btn_blogout = QPushButton(self.frame_bmenu)
        self.btn_blogout.setObjectName(u"btn_blogout")
        self.btn_blogout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_blogout.setIcon(icon4)
        self.btn_blogout.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.btn_blogout)


        self.gridLayout_10.addWidget(self.frame_bmenu, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 998, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_blogout.clicked.connect(MainWindow.close)
        self.btn_slogout.clicked.connect(MainWindow.close)
        self.btn_head_edit.toggled.connect(self.frame_head_left.setHidden)
        self.btn_head_menu.toggled.connect(self.frame_bmenu.setVisible)
        self.btn_folder_showall.toggled.connect(self.listWidget_folder.setHidden)
        self.btn_folder_tool.toggled.connect(self.frame_folder_right.setVisible)
        self.btn_head_edit.toggled.connect(self.frame_head_left.setVisible)
        self.btn_head_menu.toggled.connect(self.frame_smenu.setHidden)

        self.stackedWidget_content.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_menu_simg.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.label_menu_stitle.setText(QCoreApplication.translate("MainWindow", u"BurgressPM", None))
        self.btn_shome.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_slike.setText(QCoreApplication.translate("MainWindow", u"LIKE", None))
        self.btn_strash.setText(QCoreApplication.translate("MainWindow", u"TRASH", None))
        self.btn_sfolder.setText(QCoreApplication.translate("MainWindow", u"FOLDER", None))
        self.btn_slogout.setText(QCoreApplication.translate("MainWindow", u"LOGOUT", None))
        self.btn_head_menu.setText("")
        self.lineEdit_head_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Searching...", None))
        self.btn_head_search.setText("")
        self.btn_head_user.setText("")
        self.label_home_title.setText(QCoreApplication.translate("MainWindow", u"\u60a8\u597d\uff01\u6b22\u8fce\u4f7f\u7528BurgressPM\u5bc6\u7801\u7ba1\u7406\u5668\uff01", None))
        self.label_home_colon.setText(QCoreApplication.translate("MainWindow", u"\uff1a", None))
        self.label_home_url.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.label_home_usr.setText(QCoreApplication.translate("MainWindow", u"USERNAME", None))
        self.label_home_pwd.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None))
        self.label_home_note.setText(QCoreApplication.translate("MainWindow", u"NOTE", None))
        self.label_home_time.setText(QCoreApplication.translate("MainWindow", u"CREATE_TIME", None))
        self.label_home_folder.setText(QCoreApplication.translate("MainWindow", u"FOLDER", None))
        self.btn_home_select.setText(QCoreApplication.translate("MainWindow", u"\u7b5b\u9009", None))
        self.btn_home_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        ___qtablewidgetitem = self.tableWidget_home.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"FOLDER", None));
        ___qtablewidgetitem1 = self.tableWidget_home.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"URL", None));
        ___qtablewidgetitem2 = self.tableWidget_home.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"USERNAME", None));
        ___qtablewidgetitem3 = self.tableWidget_home.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None));
        ___qtablewidgetitem4 = self.tableWidget_home.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"NOTE", None));
        ___qtablewidgetitem5 = self.tableWidget_home.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"CREATE_TIME", None));
        ___qtablewidgetitem6 = self.tableWidget_home.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"LIKE", None));
        self.label_home_say.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u5f85\u751f\u547d\uff0c\u4f60\u4e0d\u59a8\u5927\u80c6\u4e00\u70b9\uff0c\u56e0\u4e3a\u6211\u4eec\u59cb\u7ec8\u8981\u5931\u53bb\u5b83\u3002", None))
        self.label_home_left.setText(QCoreApplication.translate("MainWindow", u"\u7248\u6743\u6240\u6709 \u5907\u6848\u53f7\uff1a\u7696ICP\u590720231231\u53f7-217", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u")", None))
        ___qtreewidgetitem = self.treeWidget_like.headerItem()
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"LIKE", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"CREATE TIME", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"NOTE", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"PASSWORD", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"USERNAME", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"URL", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"FOLDER", None));
        self.label_head_top.setText(QCoreApplication.translate("MainWindow", u"THIS IS A TRASH\uff01", None))
        self.btn_head_edit.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.btn_head_recover.setText(QCoreApplication.translate("MainWindow", u"\u6062\u590d", None))
        self.btn_head_recoverall.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u6062\u590d", None))
        self.btn_head_delete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.btn_head_deleteall.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u5220\u9664", None))
        ___qtreewidgetitem1 = self.treeWidget_trash.headerItem()
        ___qtreewidgetitem1.setText(5, QCoreApplication.translate("MainWindow", u"FOLDER", None));
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"DELETE TIME", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"NOTE", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"PASSWORD", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"USERNAME", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"URL", None));
        self.btn_folder_edit.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.btn_folder_refresh.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.btn_folder_copy.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
        self.btn_folder_tool.setText("")
        ___qtablewidgetitem7 = self.tableWidget_folder.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"URL", None));
        ___qtablewidgetitem8 = self.tableWidget_folder.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"USERNAME", None));
        ___qtablewidgetitem9 = self.tableWidget_folder.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None));
        ___qtablewidgetitem10 = self.tableWidget_folder.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"NOTE", None));
        ___qtablewidgetitem11 = self.tableWidget_folder.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"CREATE TIME", None));
        ___qtablewidgetitem12 = self.tableWidget_folder.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"LIKE", None));
        self.btn_folder_add.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.btn_folder_delete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.btn_folder_like.setText(QCoreApplication.translate("MainWindow", u"\u6536\u85cf", None))
        self.label_folder_img.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_folder_all.setText(QCoreApplication.translate("MainWindow", u"\u6211\u7684\u5bc6\u7801\u5e93", None))
        self.btn_folder_showall.setText("")
        self.btn_folder_list_add.setText("")
        self.btn_folder_list_delete.setText("")
        self.groupBox_user_content.setTitle(QCoreApplication.translate("MainWindow", u"Account Information", None))
        self.label_user_username.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.label_user_password.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.label_user_address.setText(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb\u65b9\u5f0f", None))
        self.label_user_sex.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b", None))
        self.radioButton_user_man.setText(QCoreApplication.translate("MainWindow", u"\u7537", None))
        self.radioButton_user_woman.setText(QCoreApplication.translate("MainWindow", u"\u5973", None))
        self.btn_user_modify.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.btn_user_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.label_menu_bimg.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn_bhome.setText("")
        self.btn_blike.setText("")
        self.btn_btrash.setText("")
        self.btn_bfolder.setText("")
        self.btn_blogout.setText("")
    # retranslateUi

