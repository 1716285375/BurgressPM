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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLCDNumber, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)
import end.ui.image_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(985, 790)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(49, 45, 42);\n"
"border: 1px solid rgb(255,255,255);")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
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
        self.label_bimg = QLabel(self.frame_bmenu)
        self.label_bimg.setObjectName(u"label_bimg")
        font = QFont()
        font.setFamilies([u"Social Media Circled"])
        font.setPointSize(40)
        self.label_bimg.setFont(font)
        self.label_bimg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_menu_bhead.addWidget(self.label_bimg)


        self.verticalLayout_2.addLayout(self.horizontalLayout_menu_bhead)

        self.verticalLayout_bbtn = QVBoxLayout()
        self.verticalLayout_bbtn.setObjectName(u"verticalLayout_bbtn")
        self.verticalLayout_bbtn.setContentsMargins(-1, 0, -1, -1)
        self.btn_bhome = QPushButton(self.frame_bmenu)
        self.btn_bhome.setObjectName(u"btn_bhome")
        icon = QIcon()
        icon.addFile(u":/icons/feather/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_bhome.setIcon(icon)
        self.btn_bhome.setIconSize(QSize(50, 50))

        self.verticalLayout_bbtn.addWidget(self.btn_bhome)

        self.btn_blike = QPushButton(self.frame_bmenu)
        self.btn_blike.setObjectName(u"btn_blike")
        icon1 = QIcon()
        icon1.addFile(u":/icons/feather/star.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_blike.setIcon(icon1)
        self.btn_blike.setIconSize(QSize(50, 50))

        self.verticalLayout_bbtn.addWidget(self.btn_blike)

        self.btn_btrash = QPushButton(self.frame_bmenu)
        self.btn_btrash.setObjectName(u"btn_btrash")
        icon2 = QIcon()
        icon2.addFile(u":/icons/feather/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_btrash.setIcon(icon2)
        self.btn_btrash.setIconSize(QSize(50, 50))

        self.verticalLayout_bbtn.addWidget(self.btn_btrash)

        self.btn_bfolder = QPushButton(self.frame_bmenu)
        self.btn_bfolder.setObjectName(u"btn_bfolder")
        icon3 = QIcon()
        icon3.addFile(u":/icons/feather/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_bfolder.setIcon(icon3)
        self.btn_bfolder.setIconSize(QSize(50, 50))

        self.verticalLayout_bbtn.addWidget(self.btn_bfolder)


        self.verticalLayout_2.addLayout(self.verticalLayout_bbtn)

        self.verticalSpacer = QSpacerItem(20, 321, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_blogout = QPushButton(self.frame_bmenu)
        self.btn_blogout.setObjectName(u"btn_blogout")
        icon4 = QIcon()
        icon4.addFile(u":/icons/feather/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_blogout.setIcon(icon4)
        self.btn_blogout.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.btn_blogout)


        self.horizontalLayout_3.addWidget(self.frame_bmenu)

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
        self.label_simg = QLabel(self.frame_smenu)
        self.label_simg.setObjectName(u"label_simg")
        self.label_simg.setMinimumSize(QSize(40, 40))
        self.label_simg.setMaximumSize(QSize(40, 40))
        font1 = QFont()
        font1.setFamilies([u"Social Media Circled"])
        font1.setPointSize(30)
        self.label_simg.setFont(font1)
        self.label_simg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_menu_shead.addWidget(self.label_simg)

        self.label_stitle = QLabel(self.frame_smenu)
        self.label_stitle.setObjectName(u"label_stitle")
        font2 = QFont()
        font2.setFamilies([u"Algerian"])
        font2.setPointSize(8)
        self.label_stitle.setFont(font2)
        self.label_stitle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_menu_shead.addWidget(self.label_stitle)


        self.verticalLayout_3.addLayout(self.horizontalLayout_menu_shead)

        self.verticalLayout_menu_sbtn = QVBoxLayout()
        self.verticalLayout_menu_sbtn.setSpacing(25)
        self.verticalLayout_menu_sbtn.setObjectName(u"verticalLayout_menu_sbtn")
        self.btn_shome = QPushButton(self.frame_smenu)
        self.btn_shome.setObjectName(u"btn_shome")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(True)
        self.btn_shome.setFont(font3)
        self.btn_shome.setIcon(icon)
        self.btn_shome.setIconSize(QSize(32, 32))

        self.verticalLayout_menu_sbtn.addWidget(self.btn_shome)

        self.btn_slike = QPushButton(self.frame_smenu)
        self.btn_slike.setObjectName(u"btn_slike")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        self.btn_slike.setFont(font4)
        self.btn_slike.setIcon(icon1)
        self.btn_slike.setIconSize(QSize(32, 32))

        self.verticalLayout_menu_sbtn.addWidget(self.btn_slike)

        self.btn_strash = QPushButton(self.frame_smenu)
        self.btn_strash.setObjectName(u"btn_strash")
        font5 = QFont()
        font5.setPointSize(10)
        self.btn_strash.setFont(font5)
        self.btn_strash.setIcon(icon2)
        self.btn_strash.setIconSize(QSize(32, 32))

        self.verticalLayout_menu_sbtn.addWidget(self.btn_strash)

        self.btn_sfolder = QPushButton(self.frame_smenu)
        self.btn_sfolder.setObjectName(u"btn_sfolder")
        self.btn_sfolder.setFont(font5)
        self.btn_sfolder.setIcon(icon3)
        self.btn_sfolder.setIconSize(QSize(32, 32))

        self.verticalLayout_menu_sbtn.addWidget(self.btn_sfolder)


        self.verticalLayout_3.addLayout(self.verticalLayout_menu_sbtn)

        self.verticalSpacer_2 = QSpacerItem(20, 271, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.btn_slogout = QPushButton(self.frame_smenu)
        self.btn_slogout.setObjectName(u"btn_slogout")
        self.btn_slogout.setFont(font5)
        self.btn_slogout.setIcon(icon4)
        self.btn_slogout.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.btn_slogout)


        self.horizontalLayout_3.addWidget(self.frame_smenu)

        self.frame_body = QFrame(self.centralwidget)
        self.frame_body.setObjectName(u"frame_body")
        self.frame_body.setFrameShape(QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_body)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_header = QFrame(self.frame_body)
        self.frame_header.setObjectName(u"frame_header")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_header.sizePolicy().hasHeightForWidth())
        self.frame_header.setSizePolicy(sizePolicy)
        self.frame_header.setMaximumSize(QSize(16777215, 60))
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_menu = QPushButton(self.frame_header)
        self.btn_menu.setObjectName(u"btn_menu")
        icon5 = QIcon()
        icon5.addFile(u":/icons/feather/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon5)
        self.btn_menu.setIconSize(QSize(32, 32))
        self.btn_menu.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_menu, 0, Qt.AlignTop)

        self.horizontalSpacer_header_left = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_header_left)

        self.gridLayout_search = QGridLayout()
        self.gridLayout_search.setObjectName(u"gridLayout_search")
        self.gridLayout_search.setHorizontalSpacing(10)
        self.gridLayout_search.setVerticalSpacing(0)
        self.lineEdit_search = QLineEdit(self.frame_header)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setMinimumSize(QSize(0, 40))

        self.gridLayout_search.addWidget(self.lineEdit_search, 0, 0, 1, 1)

        self.btn_search = QPushButton(self.frame_header)
        self.btn_search.setObjectName(u"btn_search")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy1)
        icon6 = QIcon()
        icon6.addFile(u":/icons/feather/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon6)
        self.btn_search.setIconSize(QSize(32, 32))

        self.gridLayout_search.addWidget(self.btn_search, 0, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_search)

        self.horizontalSpacer_header_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_header_right)

        self.btn_user = QPushButton(self.frame_header)
        self.btn_user.setObjectName(u"btn_user")
        icon7 = QIcon()
        icon7.addFile(u":/icons/feather/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_user.setIcon(icon7)
        self.btn_user.setIconSize(QSize(60, 60))

        self.horizontalLayout.addWidget(self.btn_user, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.frame_header)

        self.frame_content = QFrame(self.frame_body)
        self.frame_content.setObjectName(u"frame_content")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(8)
        sizePolicy2.setHeightForWidth(self.frame_content.sizePolicy().hasHeightForWidth())
        self.frame_content.setSizePolicy(sizePolicy2)
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
        self.frame_home_content = QFrame(self.page_home)
        self.frame_home_content.setObjectName(u"frame_home_content")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(9)
        sizePolicy3.setHeightForWidth(self.frame_home_content.sizePolicy().hasHeightForWidth())
        self.frame_home_content.setSizePolicy(sizePolicy3)
        font6 = QFont()
        font6.setFamilies([u"\u5e7c\u5706"])
        self.frame_home_content.setFont(font6)
        self.frame_home_content.setFrameShape(QFrame.StyledPanel)
        self.frame_home_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_home_content)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_home_content_top = QHBoxLayout()
        self.horizontalLayout_home_content_top.setObjectName(u"horizontalLayout_home_content_top")
        self.label_home_welcome = QLabel(self.frame_home_content)
        self.label_home_welcome.setObjectName(u"label_home_welcome")
        font7 = QFont()
        font7.setFamilies([u"\u534e\u6587\u5f69\u4e91"])
        font7.setPointSize(16)
        font7.setBold(True)
        font7.setItalic(False)
        self.label_home_welcome.setFont(font7)

        self.horizontalLayout_home_content_top.addWidget(self.label_home_welcome)

        self.horizontalSpacer_3 = QSpacerItem(208, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_home_content_top.addItem(self.horizontalSpacer_3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lcdNumber_2 = QLCDNumber(self.frame_home_content)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setDigitCount(1)
        self.lcdNumber_2.setProperty("value", 2.000000000000000)

        self.gridLayout_3.addWidget(self.lcdNumber_2, 0, 1, 1, 1)

        self.lcdNumber_5 = QLCDNumber(self.frame_home_content)
        self.lcdNumber_5.setObjectName(u"lcdNumber_5")
        self.lcdNumber_5.setDigitCount(1)
        self.lcdNumber_5.setProperty("value", 2.000000000000000)

        self.gridLayout_3.addWidget(self.lcdNumber_5, 0, 3, 1, 1)

        self.label_home_colon = QLabel(self.frame_home_content)
        self.label_home_colon.setObjectName(u"label_home_colon")
        font8 = QFont()
        font8.setFamilies([u"Algerian"])
        font8.setPointSize(10)
        font8.setBold(True)
        self.label_home_colon.setFont(font8)
        self.label_home_colon.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_home_colon, 0, 2, 1, 1)

        self.lcdNumber_6 = QLCDNumber(self.frame_home_content)
        self.lcdNumber_6.setObjectName(u"lcdNumber_6")
        self.lcdNumber_6.setDigitCount(1)
        self.lcdNumber_6.setProperty("value", 2.000000000000000)

        self.gridLayout_3.addWidget(self.lcdNumber_6, 0, 4, 1, 1)

        self.lcdNumber_1 = QLCDNumber(self.frame_home_content)
        self.lcdNumber_1.setObjectName(u"lcdNumber_1")
        self.lcdNumber_1.setDigitCount(1)
        self.lcdNumber_1.setProperty("value", 1.000000000000000)

        self.gridLayout_3.addWidget(self.lcdNumber_1, 0, 0, 1, 1)


        self.horizontalLayout_home_content_top.addLayout(self.gridLayout_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_home_content_top)

        self.frame_home_tree = QFrame(self.frame_home_content)
        self.frame_home_tree.setObjectName(u"frame_home_tree")
        self.frame_home_tree.setFrameShape(QFrame.StyledPanel)
        self.frame_home_tree.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_home_tree)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.treeWidget_home = QTreeWidget(self.frame_home_tree)
        QTreeWidgetItem(self.treeWidget_home)
        QTreeWidgetItem(self.treeWidget_home)
        QTreeWidgetItem(self.treeWidget_home)
        QTreeWidgetItem(self.treeWidget_home)
        QTreeWidgetItem(self.treeWidget_home)
        QTreeWidgetItem(self.treeWidget_home)
        self.treeWidget_home.setObjectName(u"treeWidget_home")

        self.horizontalLayout_5.addWidget(self.treeWidget_home)


        self.verticalLayout_8.addWidget(self.frame_home_tree)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_4 = QSpacerItem(328, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.label_home_say = QLabel(self.frame_home_content)
        self.label_home_say.setObjectName(u"label_home_say")
        font9 = QFont()
        font9.setFamilies([u"\u534e\u6587\u5f69\u4e91"])
        font9.setPointSize(12)
        self.label_home_say.setFont(font9)
        self.label_home_say.setLayoutDirection(Qt.RightToLeft)
        self.label_home_say.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_home_say)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)


        self.verticalLayout_home_main.addWidget(self.frame_home_content)

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

        self.horizontalSpacer_home_bottom_right = QSpacerItem(428, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.frame_like_main = QFrame(self.page_like)
        self.frame_like_main.setObjectName(u"frame_like_main")
        self.frame_like_main.setGeometry(QRect(30, 200, 731, 411))
        self.frame_like_main.setFrameShape(QFrame.StyledPanel)
        self.frame_like_main.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_like_main)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 101, 54, 101))
        self.stackedWidget_content.addWidget(self.page_like)
        self.page_trash = QWidget()
        self.page_trash.setObjectName(u"page_trash")
        self.horizontalLayout_4 = QHBoxLayout(self.page_trash)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_trash_main = QVBoxLayout()
        self.verticalLayout_trash_main.setObjectName(u"verticalLayout_trash_main")
        self.frame_trash_content = QFrame(self.page_trash)
        self.frame_trash_content.setObjectName(u"frame_trash_content")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.frame_trash_content.sizePolicy().hasHeightForWidth())
        self.frame_trash_content.setSizePolicy(sizePolicy4)
        self.frame_trash_content.setFrameShape(QFrame.StyledPanel)
        self.frame_trash_content.setFrameShadow(QFrame.Raised)

        self.verticalLayout_trash_main.addWidget(self.frame_trash_content)

        self.frame_trash_head = QFrame(self.page_trash)
        self.frame_trash_head.setObjectName(u"frame_trash_head")
        sizePolicy2.setHeightForWidth(self.frame_trash_head.sizePolicy().hasHeightForWidth())
        self.frame_trash_head.setSizePolicy(sizePolicy2)
        self.frame_trash_head.setFrameShape(QFrame.StyledPanel)
        self.frame_trash_head.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_trash_head)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.treeWidget = QTreeWidget(self.frame_trash_head)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_4.addWidget(self.treeWidget)


        self.verticalLayout_trash_main.addWidget(self.frame_trash_head)


        self.horizontalLayout_4.addLayout(self.verticalLayout_trash_main)

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
        self.pushButton_16 = QPushButton(self.frame_folder_head)
        self.pushButton_16.setObjectName(u"pushButton_16")
        icon8 = QIcon()
        icon8.addFile(u":/icons/feather/copy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon8)
        self.pushButton_16.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.frame_folder_head)
        self.pushButton_17.setObjectName(u"pushButton_17")
        icon9 = QIcon()
        icon9.addFile(u":/icons/feather/disc.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon9)
        self.pushButton_17.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.frame_folder_head)
        self.pushButton_18.setObjectName(u"pushButton_18")
        icon10 = QIcon()
        icon10.addFile(u":/icons/feather/aperture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon10)
        self.pushButton_18.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.pushButton_18)

        self.horizontalSpacer = QSpacerItem(403, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_20 = QPushButton(self.frame_folder_head)
        self.pushButton_20.setObjectName(u"pushButton_20")
        icon11 = QIcon()
        icon11.addFile(u":/icons/feather/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u":/icons/feather/arrow-down-circle.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_20.setIcon(icon11)
        self.pushButton_20.setIconSize(QSize(32, 32))
        self.pushButton_20.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton_20)


        self.verticalLayout_folder_main.addWidget(self.frame_folder_head)

        self.gridLayout_folder_content = QGridLayout()
        self.gridLayout_folder_content.setObjectName(u"gridLayout_folder_content")
        self.frame_folder_tree = QFrame(self.page_folder)
        self.frame_folder_tree.setObjectName(u"frame_folder_tree")
        self.frame_folder_tree.setFrameShape(QFrame.StyledPanel)
        self.frame_folder_tree.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_folder_tree)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.treeWidget_folder = QTreeWidget(self.frame_folder_tree)
        QTreeWidgetItem(self.treeWidget_folder)
        QTreeWidgetItem(self.treeWidget_folder)
        QTreeWidgetItem(self.treeWidget_folder)
        QTreeWidgetItem(self.treeWidget_folder)
        self.treeWidget_folder.setObjectName(u"treeWidget_folder")

        self.verticalLayout.addWidget(self.treeWidget_folder)


        self.gridLayout_folder_content.addWidget(self.frame_folder_tree, 0, 0, 1, 1)

        self.frame_folder_table = QFrame(self.page_folder)
        self.frame_folder_table.setObjectName(u"frame_folder_table")
        self.frame_folder_table.setFrameShape(QFrame.StyledPanel)
        self.frame_folder_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_folder_table)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableWidget_folder = QTableWidget(self.frame_folder_table)
        if (self.tableWidget_folder.columnCount() < 6):
            self.tableWidget_folder.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_folder.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_folder.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_folder.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_folder.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_folder.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_folder.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget_folder.rowCount() < 5):
            self.tableWidget_folder.setRowCount(5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_folder.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_folder.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_folder.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_folder.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_folder.setVerticalHeaderItem(4, __qtablewidgetitem10)
        self.tableWidget_folder.setObjectName(u"tableWidget_folder")

        self.verticalLayout_7.addWidget(self.tableWidget_folder)


        self.gridLayout_folder_content.addWidget(self.frame_folder_table, 0, 1, 1, 1)

        self.frame_folder_right = QFrame(self.page_folder)
        self.frame_folder_right.setObjectName(u"frame_folder_right")
        self.frame_folder_right.setFrameShape(QFrame.StyledPanel)
        self.frame_folder_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_folder_right)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 10, 0, 5)
        self.verticalLayout_right_tool = QVBoxLayout()
        self.verticalLayout_right_tool.setObjectName(u"verticalLayout_right_tool")
        self.btn_folder_add = QPushButton(self.frame_folder_right)
        self.btn_folder_add.setObjectName(u"btn_folder_add")
        font12 = QFont()
        font12.setFamilies([u"\u5e7c\u5706"])
        font12.setPointSize(14)
        font12.setBold(True)
        font12.setItalic(False)
        self.btn_folder_add.setFont(font12)
        self.btn_folder_add.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/feather/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_folder_add.setIcon(icon12)
        self.btn_folder_add.setIconSize(QSize(32, 32))

        self.verticalLayout_right_tool.addWidget(self.btn_folder_add)

        self.btn_folder_delete = QPushButton(self.frame_folder_right)
        self.btn_folder_delete.setObjectName(u"btn_folder_delete")
        font13 = QFont()
        font13.setFamilies([u"\u5e7c\u5706"])
        font13.setPointSize(14)
        font13.setBold(True)
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

        self.verticalSpacer_4 = QSpacerItem(20, 212, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.horizontalLayout_folder_img = QHBoxLayout()
        self.horizontalLayout_folder_img.setSpacing(0)
        self.horizontalLayout_folder_img.setObjectName(u"horizontalLayout_folder_img")
        self.label_folder_img = QLabel(self.frame_folder_right)
        self.label_folder_img.setObjectName(u"label_folder_img")
        font14 = QFont()
        font14.setFamilies([u"Social Media Circled"])
        font14.setPointSize(25)
        self.label_folder_img.setFont(font14)
        self.label_folder_img.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_folder_img.addWidget(self.label_folder_img)


        self.verticalLayout_6.addLayout(self.horizontalLayout_folder_img)


        self.gridLayout_folder_content.addWidget(self.frame_folder_right, 0, 2, 1, 1, Qt.AlignTop)

        self.gridLayout_folder_content.setColumnStretch(0, 2)
        self.gridLayout_folder_content.setColumnStretch(1, 7)

        self.verticalLayout_folder_main.addLayout(self.gridLayout_folder_content)


        self.gridLayout.addLayout(self.verticalLayout_folder_main, 0, 0, 1, 1)

        self.stackedWidget_content.addWidget(self.page_folder)
        self.page_user = QWidget()
        self.page_user.setObjectName(u"page_user")
        self.stackedWidget_content.addWidget(self.page_user)

        self.gridLayout_5.addWidget(self.stackedWidget_content, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_content)


        self.horizontalLayout_3.addWidget(self.frame_body)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 985, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_menu.toggled.connect(self.frame_bmenu.setVisible)
        self.btn_menu.toggled.connect(self.frame_smenu.setHidden)
        self.pushButton_20.toggled.connect(self.frame_folder_right.setVisible)
        self.pushButton_20.toggled.connect(self.frame_folder_right.setHidden)

        self.stackedWidget_content.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_bimg.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn_bhome.setText("")
        self.btn_blike.setText("")
        self.btn_btrash.setText("")
        self.btn_bfolder.setText("")
        self.btn_blogout.setText("")
        self.label_simg.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.label_stitle.setText(QCoreApplication.translate("MainWindow", u"BurgressPM", None))
        self.btn_shome.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_slike.setText(QCoreApplication.translate("MainWindow", u"LIKE", None))
        self.btn_strash.setText(QCoreApplication.translate("MainWindow", u"TRASH", None))
        self.btn_sfolder.setText(QCoreApplication.translate("MainWindow", u"FOLDER", None))
        self.btn_slogout.setText(QCoreApplication.translate("MainWindow", u"LOGOUT", None))
        self.btn_menu.setText("")
        self.btn_search.setText("")
        self.btn_user.setText("")
        self.label_home_welcome.setText(QCoreApplication.translate("MainWindow", u"\u60a8\u597d\uff01\u6b22\u8fce\u4f7f\u7528BurgressPM\u5bc6\u7801\u7ba1\u7406\u5668\uff01", None))
        self.label_home_colon.setText(QCoreApplication.translate("MainWindow", u"\uff1a", None))
        ___qtreewidgetitem = self.treeWidget_home.headerItem()
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled = self.treeWidget_home.isSortingEnabled()
        self.treeWidget_home.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget_home.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem2 = self.treeWidget_home.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem3 = self.treeWidget_home.topLevelItem(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem4 = self.treeWidget_home.topLevelItem(3)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem5 = self.treeWidget_home.topLevelItem(4)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem6 = self.treeWidget_home.topLevelItem(5)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        self.treeWidget_home.setSortingEnabled(__sortingEnabled)

        self.label_home_say.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u5f85\u751f\u547d\uff0c\u4f60\u4e0d\u59a8\u5927\u80c6\u4e00\u70b9\uff0c\u56e0\u4e3a\u6211\u4eec\u59cb\u7ec8\u8981\u5931\u53bb\u5b83\u3002", None))
        self.label_home_left.setText(QCoreApplication.translate("MainWindow", u"\u7248\u6743\u6240\u6709 \u5907\u6848\u53f7\uff1a\u7696ICP\u590720231231\u53f7-217", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"like", None))
        ___qtreewidgetitem7 = self.treeWidget.headerItem()
        ___qtreewidgetitem7.setText(5, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtreewidgetitem7.setText(4, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtreewidgetitem7.setText(3, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtreewidgetitem7.setText(2, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtreewidgetitem7.setText(1, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled1 = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem8 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem9 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem10 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem11 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem12 = self.treeWidget.topLevelItem(4)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem13 = self.treeWidget.topLevelItem(5)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem14 = self.treeWidget.topLevelItem(6)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled1)

        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"copyuer", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"copymima", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_20.setText("")
        ___qtreewidgetitem15 = self.treeWidget_folder.headerItem()
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));

        __sortingEnabled2 = self.treeWidget_folder.isSortingEnabled()
        self.treeWidget_folder.setSortingEnabled(False)
        ___qtreewidgetitem16 = self.treeWidget_folder.topLevelItem(0)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem17 = self.treeWidget_folder.topLevelItem(1)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem18 = self.treeWidget_folder.topLevelItem(2)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem19 = self.treeWidget_folder.topLevelItem(3)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        self.treeWidget_folder.setSortingEnabled(__sortingEnabled2)

        ___qtablewidgetitem = self.tableWidget_folder.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem1 = self.tableWidget_folder.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem2 = self.tableWidget_folder.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem3 = self.tableWidget_folder.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem4 = self.tableWidget_folder.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem5 = self.tableWidget_folder.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem6 = self.tableWidget_folder.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem7 = self.tableWidget_folder.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem8 = self.tableWidget_folder.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem9 = self.tableWidget_folder.verticalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem10 = self.tableWidget_folder.verticalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        self.btn_folder_add.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.btn_folder_delete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.btn_folder_like.setText(QCoreApplication.translate("MainWindow", u"\u6536\u85cf", None))
        self.label_folder_img.setText(QCoreApplication.translate("MainWindow", u"3", None))
    # retranslateUi

