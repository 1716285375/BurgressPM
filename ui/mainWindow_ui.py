# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import end.ui.image_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(1129, 690)
        font = QFont()
        font.setBold(False)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"/*============================================*/\n"
"/*btn*/\n"
"")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon = QIcon()
        icon.addFile(u":/icons/feather/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon1 = QIcon()
        icon1.addFile(u":/icons/feather/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setMenuRole(QAction.NoRole)
        self.actionFolder = QAction(MainWindow)
        self.actionFolder.setObjectName(u"actionFolder")
        icon2 = QIcon()
        icon2.addFile(u":/icons/feather/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFolder.setIcon(icon2)
        self.actionFolder.setMenuRole(QAction.NoRole)
        self.actionOutput = QAction(MainWindow)
        self.actionOutput.setObjectName(u"actionOutput")
        icon3 = QIcon()
        icon3.addFile(u":/icons/feather/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOutput.setIcon(icon3)
        self.actionOutput.setMenuRole(QAction.NoRole)
        self.actionInput = QAction(MainWindow)
        self.actionInput.setObjectName(u"actionInput")
        icon4 = QIcon()
        icon4.addFile(u":/icons/feather/log-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionInput.setIcon(icon4)
        self.actionInput.setMenuRole(QAction.NoRole)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon5 = QIcon()
        icon5.addFile(u":/icons/feather/power.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon5)
        self.actionExit.setMenuRole(QAction.NoRole)
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        icon6 = QIcon()
        icon6.addFile(u":/icons/feather/corner-left-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUndo.setIcon(icon6)
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        icon7 = QIcon()
        icon7.addFile(u":/icons/feather/corner-right-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRedo.setIcon(icon7)
        self.actionRedo.setMenuRole(QAction.NoRole)
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        icon8 = QIcon()
        icon8.addFile(u":/icons/feather/scissors.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCut.setIcon(icon8)
        self.actionCut.setMenuRole(QAction.NoRole)
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        icon9 = QIcon()
        icon9.addFile(u":/icons/feather/copy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCopy.setIcon(icon9)
        self.actionCopy.setMenuRole(QAction.NoRole)
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        icon10 = QIcon()
        icon10.addFile(u":/icons/feather/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPaste.setIcon(icon10)
        self.actionPaste.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.page_header = QWidget(self.widget)
        self.page_header.setObjectName(u"page_header")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.page_header.sizePolicy().hasHeightForWidth())
        self.page_header.setSizePolicy(sizePolicy)
        self.page_header.setStyleSheet(u"#page_header{\n"
"	color:rgba(255,255,255,210);\n"
"}")
        self.horizontalLayout_11 = QHBoxLayout(self.page_header)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_header = QHBoxLayout()
        self.horizontalLayout_header.setSpacing(10)
        self.horizontalLayout_header.setObjectName(u"horizontalLayout_header")
        self.header_left = QFrame(self.page_header)
        self.header_left.setObjectName(u"header_left")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header_left.sizePolicy().hasHeightForWidth())
        self.header_left.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.header_left)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_header = QLabel(self.header_left)
        self.label_header.setObjectName(u"label_header")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_header.sizePolicy().hasHeightForWidth())
        self.label_header.setSizePolicy(sizePolicy2)
        self.label_header.setMinimumSize(QSize(120, 0))
        font1 = QFont()
        font1.setFamilies([u"Algerian"])
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        self.label_header.setFont(font1)
        self.label_header.setAutoFillBackground(False)
        self.label_header.setStyleSheet(u"color: rgba(255, 255, 255, 200);")
        self.label_header.setTextFormat(Qt.PlainText)
        self.label_header.setScaledContents(False)
        self.label_header.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_header)


        self.horizontalLayout_header.addWidget(self.header_left)

        self.header_right = QWidget(self.page_header)
        self.header_right.setObjectName(u"header_right")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(7)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.header_right.sizePolicy().hasHeightForWidth())
        self.header_right.setSizePolicy(sizePolicy3)
        self.horizontalLayout_12 = QHBoxLayout(self.header_right)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lineEdit = QLineEdit(self.header_right)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy4)
        self.lineEdit.setMinimumSize(QSize(300, 40))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(18)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;")
        self.lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.lineEdit, 0, Qt.AlignRight)

        self.infomation = QFrame(self.header_right)
        self.infomation.setObjectName(u"infomation")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.infomation.sizePolicy().hasHeightForWidth())
        self.infomation.setSizePolicy(sizePolicy5)
        self.infomation.setStyleSheet(u"")
        self.infomation.setFrameShape(QFrame.StyledPanel)
        self.infomation.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.infomation)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.infomation)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.infomation)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.btn_usr_info = QPushButton(self.infomation)
        self.btn_usr_info.setObjectName(u"btn_usr_info")
        font3 = QFont()
        font3.setFamilies([u"Garamond"])
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setKerning(True)
        self.btn_usr_info.setFont(font3)
        self.btn_usr_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_usr_info.setLayoutDirection(Qt.LeftToRight)
        icon11 = QIcon()
        icon11.addFile(u":/icons/feather/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_usr_info.setIcon(icon11)
        self.btn_usr_info.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_usr_info)


        self.horizontalLayout_10.addWidget(self.infomation, 0, Qt.AlignRight)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_header.addWidget(self.header_right)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_header)


        self.verticalLayout.addWidget(self.page_header)

        self.content_main = QWidget(self.widget)
        self.content_main.setObjectName(u"content_main")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(8)
        sizePolicy6.setHeightForWidth(self.content_main.sizePolicy().hasHeightForWidth())
        self.content_main.setSizePolicy(sizePolicy6)
        self.content_main.setStyleSheet(u"#content_main \n"
"{\n"
"	background-color: rgb(235,237,238);\n"
"}\n"
"\n"
"#content_main #treeWidget\n"
"{\n"
"	border: None;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.content_main)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.content_left = QFrame(self.content_main)
        self.content_left.setObjectName(u"content_left")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(3)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.content_left.sizePolicy().hasHeightForWidth())
        self.content_left.setSizePolicy(sizePolicy7)
        self.content_left.setMaximumSize(QSize(300, 16777215))
        self.content_left.setStyleSheet(u"#content_left\n"
"{\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"	background-color: rgb(244, 254, 255);\n"
"}\n"
"\n"
"\n"
"#content_left #treeWidget_pwd\n"
"{\n"
"	border: None;\n"
"}\n"
"\n"
"#content_left #pwd_folder\n"
"{\n"
"	border-top: 1px solid rgb(0, 0, 0);\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.content_left)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.option_btn = QWidget(self.content_left)
        self.option_btn.setObjectName(u"option_btn")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(3)
        sizePolicy8.setHeightForWidth(self.option_btn.sizePolicy().hasHeightForWidth())
        self.option_btn.setSizePolicy(sizePolicy8)
        self.option_btn.setStyleSheet(u"\n"
"/*============================================*/\n"
"/*btn*/\n"
"#option_btn\n"
"{\n"
"\n"
"}\n"
"\n"
"\n"
"#option_btn QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(32,226,215, 100), stop:1 rgba(249,254,165, 200));\n"
"\n"
"	text-align: left;\n"
"	border: None;\n"
"	margin-bottom: 15px;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	padding-left: 5px;\n"
"	\n"
"	\n"
"}\n"
"#option_btn QPushButton:hover\n"
"{\n"
"		background-color: rgb(152,251,152);\n"
"}\n"
"#option_btn QPushButton:pressed\n"
"{\n"
"		padding-left: 10px;\n"
"		padding-top: 5px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.option_btn)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 20, 15, 0)
        self.btn_home = QPushButton(self.option_btn)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy4.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy4)
        self.btn_home.setMinimumSize(QSize(0, 60))
        self.btn_home.setMaximumSize(QSize(16777215, 60))
        font4 = QFont()
        font4.setFamilies([u"Algerian"])
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setKerning(True)
        self.btn_home.setFont(font4)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        icon12 = QIcon()
        icon12.addFile(u":/icons/feather/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon12)
        self.btn_home.setIconSize(QSize(44, 44))

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_like = QPushButton(self.option_btn)
        self.btn_like.setObjectName(u"btn_like")
        sizePolicy4.setHeightForWidth(self.btn_like.sizePolicy().hasHeightForWidth())
        self.btn_like.setSizePolicy(sizePolicy4)
        self.btn_like.setMinimumSize(QSize(0, 60))
        self.btn_like.setFont(font4)
        self.btn_like.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/feather/heart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_like.setIcon(icon13)
        self.btn_like.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.btn_like)

        self.btn_trash = QPushButton(self.option_btn)
        self.btn_trash.setObjectName(u"btn_trash")
        sizePolicy4.setHeightForWidth(self.btn_trash.sizePolicy().hasHeightForWidth())
        self.btn_trash.setSizePolicy(sizePolicy4)
        self.btn_trash.setMinimumSize(QSize(0, 60))
        self.btn_trash.setFont(font4)
        self.btn_trash.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_trash.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon14 = QIcon()
        icon14.addFile(u":/icons/feather/trash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_trash.setIcon(icon14)
        self.btn_trash.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.btn_trash)


        self.verticalLayout_2.addWidget(self.option_btn, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pwd_folder = QWidget(self.content_left)
        self.pwd_folder.setObjectName(u"pwd_folder")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(7)
        sizePolicy9.setHeightForWidth(self.pwd_folder.sizePolicy().hasHeightForWidth())
        self.pwd_folder.setSizePolicy(sizePolicy9)
        self.pwd_folder.setStyleSheet(u"/*\n"
"background-color: rgb(230,233,240);\n"
"*/")
        self.horizontalLayout_3 = QHBoxLayout(self.pwd_folder)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 20, 0, 0)
        self.treeWidget_pwd = QTreeWidget(self.pwd_folder)
        self.treeWidget_pwd.headerItem().setText(0, "")
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget_pwd)
        __qtreewidgetitem.setIcon(0, icon2);
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1.setIcon(0, icon2);
        self.treeWidget_pwd.setObjectName(u"treeWidget_pwd")
        self.treeWidget_pwd.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.treeWidget_pwd.setStyleSheet(u"")
        self.treeWidget_pwd.setHeaderHidden(True)

        self.horizontalLayout_3.addWidget(self.treeWidget_pwd)


        self.verticalLayout_2.addWidget(self.pwd_folder)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.horizontalLayout_4.addWidget(self.content_left)

        self.content_right = QWidget(self.content_main)
        self.content_right.setObjectName(u"content_right")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(8)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.content_right.sizePolicy().hasHeightForWidth())
        self.content_right.setSizePolicy(sizePolicy10)
        self.verticalLayout_4 = QVBoxLayout(self.content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_content = QStackedWidget(self.content_right)
        self.stackedWidget_content.setObjectName(u"stackedWidget_content")
        sizePolicy3.setHeightForWidth(self.stackedWidget_content.sizePolicy().hasHeightForWidth())
        self.stackedWidget_content.setSizePolicy(sizePolicy3)
        self.stackedWidget_content.setStyleSheet(u"")
        self.stackedWidget_content.setFrameShape(QFrame.Box)
        self.stackedWidget_content.setLineWidth(1)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.horizontalLayout_9 = QHBoxLayout(self.page_home)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_2 = QLabel(self.page_home)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_9.addWidget(self.label_2)

        self.stackedWidget_content.addWidget(self.page_home)
        self.page_like = QWidget()
        self.page_like.setObjectName(u"page_like")
        self.horizontalLayout_16 = QHBoxLayout(self.page_like)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_4 = QLabel(self.page_like)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_16.addWidget(self.label_4)

        self.stackedWidget_content.addWidget(self.page_like)
        self.page_trash = QWidget()
        self.page_trash.setObjectName(u"page_trash")
        self.horizontalLayout_8 = QHBoxLayout(self.page_trash)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.page_trash)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.stackedWidget_content.addWidget(self.page_trash)
        self.page_folder = QWidget()
        self.page_folder.setObjectName(u"page_folder")
        self.tableWidget = QTableWidget(self.page_folder)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(80, 60, 411, 321))
        self.tableWidget.verticalHeader().setVisible(True)
        self.stackedWidget_content.addWidget(self.page_folder)

        self.verticalLayout_4.addWidget(self.stackedWidget_content)


        self.horizontalLayout_4.addWidget(self.content_right)


        self.verticalLayout.addWidget(self.content_main)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1129, 21))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_edit = QMenu(self.menubar)
        self.menu_edit.setObjectName(u"menu_edit")
        self.menu_view = QMenu(self.menubar)
        self.menu_view.setObjectName(u"menu_view")
        self.menu_option = QMenu(self.menubar)
        self.menu_option.setObjectName(u"menu_option")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_option.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.actionNew)
        self.menu_file.addAction(self.actionFolder)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.actionSave)
        self.menu_file.addAction(self.actionInput)
        self.menu_file.addAction(self.actionOutput)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.actionExit)
        self.menu_edit.addAction(self.actionUndo)
        self.menu_edit.addAction(self.actionRedo)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.actionCut)
        self.menu_edit.addAction(self.actionCopy)
        self.menu_edit.addAction(self.actionPaste)

        self.retranslateUi(MainWindow)
        self.pushButton.toggled.connect(self.lineEdit.setVisible)
        self.pushButton.toggled.connect(self.lineEdit.setHidden)

        self.stackedWidget_content.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
#if QT_CONFIG(tooltip)
        self.actionNew.setToolTip(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
#endif // QT_CONFIG(tooltip)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.actionFolder.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5bc6\u7801\u5e93", None))
#if QT_CONFIG(tooltip)
        self.actionFolder.setToolTip(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5bc6\u7801\u5e93", None))
#endif // QT_CONFIG(tooltip)
        self.actionOutput.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
#if QT_CONFIG(tooltip)
        self.actionOutput.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
#endif // QT_CONFIG(tooltip)
        self.actionInput.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
#if QT_CONFIG(tooltip)
        self.actionInput.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
#endif // QT_CONFIG(tooltip)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
#if QT_CONFIG(tooltip)
        self.actionExit.setToolTip(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
#endif // QT_CONFIG(tooltip)
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"\u64a4\u9500(U)", None))
#if QT_CONFIG(tooltip)
        self.actionUndo.setToolTip(QCoreApplication.translate("MainWindow", u"\u64a4\u9500", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionUndo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u505a(R)", None))
#if QT_CONFIG(tooltip)
        self.actionRedo.setToolTip(QCoreApplication.translate("MainWindow", u"\u91cd\u505a", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionRedo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Y", None))
#endif // QT_CONFIG(shortcut)
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"\u526a\u5207", None))
#if QT_CONFIG(tooltip)
        self.actionCut.setToolTip(QCoreApplication.translate("MainWindow", u"\u526a\u5207", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionCut.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
#if QT_CONFIG(tooltip)
        self.actionCopy.setToolTip(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"\u7c98\u8d34", None))
#if QT_CONFIG(tooltip)
        self.actionPaste.setToolTip(QCoreApplication.translate("MainWindow", u"\u7c98\u8d34", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionPaste.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.label_header.setText(QCoreApplication.translate("MainWindow", u"BurgressPM", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_usr_info.setText(QCoreApplication.translate("MainWindow", u"1716285375@qq.com", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"  home", None))
        self.btn_like.setText(QCoreApplication.translate("MainWindow", u"  like", None))
        self.btn_trash.setText(QCoreApplication.translate("MainWindow", u"  trash", None))

        __sortingEnabled = self.treeWidget_pwd.isSortingEnabled()
        self.treeWidget_pwd.setSortingEnabled(False)
        ___qtreewidgetitem = self.treeWidget_pwd.topLevelItem(0)
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u6211\u7684\u5bc6\u7801\u5e93", None));
        ___qtreewidgetitem1 = ___qtreewidgetitem.child(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u5bc6\u7801\u5e93", None));
        self.treeWidget_pwd.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"home", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"like", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"trash", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_edit.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_view.setTitle(QCoreApplication.translate("MainWindow", u"\u67e5\u770b", None))
        self.menu_option.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

