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
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
import end.ui.image_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(1080, 720)
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
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.page_header = QWidget(self.centralwidget)
        self.page_header.setObjectName(u"page_header")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.page_header.sizePolicy().hasHeightForWidth())
        self.page_header.setSizePolicy(sizePolicy)
        self.page_header.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_usr = QFrame(self.page_header)
        self.frame_usr.setObjectName(u"frame_usr")
        self.frame_usr.setGeometry(QRect(0, 16, 200, 40))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_usr.sizePolicy().hasHeightForWidth())
        self.frame_usr.setSizePolicy(sizePolicy1)
        self.frame_usr.setMinimumSize(QSize(200, 40))
        self.label_img = QLabel(self.frame_usr)
        self.label_img.setObjectName(u"label_img")
        self.label_img.setGeometry(QRect(10, 10, 151, 31))
        self.label_img.setScaledContents(False)
        self.label_img.setAlignment(Qt.AlignCenter)
        self.widget_2 = QWidget(self.page_header)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(540, 0, 491, 80))
        self.infomation = QFrame(self.widget_2)
        self.infomation.setObjectName(u"infomation")
        self.infomation.setGeometry(QRect(120, 0, 337, 60))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.infomation.sizePolicy().hasHeightForWidth())
        self.infomation.setSizePolicy(sizePolicy2)
        self.infomation.setStyleSheet(u"background-color: rgb(0, 170, 127);")
        self.infomation.setFrameShape(QFrame.StyledPanel)
        self.infomation.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.infomation)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.infomation)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.infomation)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.btn_usr_info = QPushButton(self.infomation)
        self.btn_usr_info.setObjectName(u"btn_usr_info")
        font1 = QFont()
        font1.setFamilies([u"Garamond"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setKerning(True)
        self.btn_usr_info.setFont(font1)
        self.btn_usr_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_usr_info.setLayoutDirection(Qt.LeftToRight)
        icon11 = QIcon()
        icon11.addFile(u":/icons/feather/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_usr_info.setIcon(icon11)
        self.btn_usr_info.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_usr_info)

        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(-10, 20, 113, 21))

        self.verticalLayout.addWidget(self.page_header)

        self.content_main = QWidget(self.centralwidget)
        self.content_main.setObjectName(u"content_main")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(8)
        sizePolicy3.setHeightForWidth(self.content_main.sizePolicy().hasHeightForWidth())
        self.content_main.setSizePolicy(sizePolicy3)
        self.content_main.setStyleSheet(u"background-color: rgb(154, 190, 175);\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.content_main)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.content_left = QWidget(self.content_main)
        self.content_left.setObjectName(u"content_left")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.content_left.sizePolicy().hasHeightForWidth())
        self.content_left.setSizePolicy(sizePolicy4)
        self.content_left.setMinimumSize(QSize(260, 0))
        self.content_left.setStyleSheet(u"border: 1px solid rgb(0, 0, 0);")
        self.horizontalLayout_5 = QHBoxLayout(self.content_left)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 25, 10, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.option_btn = QWidget(self.content_left)
        self.option_btn.setObjectName(u"option_btn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(3)
        sizePolicy5.setHeightForWidth(self.option_btn.sizePolicy().hasHeightForWidth())
        self.option_btn.setSizePolicy(sizePolicy5)
        self.option_btn.setStyleSheet(u"\n"
"/*============================================*/\n"
"/*btn*/\n"
"#option_btn QPushButton\n"
"{\n"
"\n"
"	background-color: rgb(170, 170, 0);\n"
"	\n"
"\n"
"	text-align: left;\n"
"	border: None;\n"
"	\n"
"}\n"
"#option_btn QPushButton:hover\n"
"{\n"
"		background-color: rgb(54, 40, 43);\n"
"}\n"
"#option_btn QPushButton:pressed\n"
"{\n"
"		padding-left: 5px;\n"
"		padding-top: 5px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.option_btn)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.btn_home = QPushButton(self.option_btn)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy6)
        font2 = QFont()
        font2.setFamilies([u"Algerian"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setKerning(True)
        self.btn_home.setFont(font2)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        icon12 = QIcon()
        icon12.addFile(u":/icons/feather/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon12)
        self.btn_home.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_like = QPushButton(self.option_btn)
        self.btn_like.setObjectName(u"btn_like")
        sizePolicy6.setHeightForWidth(self.btn_like.sizePolicy().hasHeightForWidth())
        self.btn_like.setSizePolicy(sizePolicy6)
        self.btn_like.setFont(font2)
        self.btn_like.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/feather/heart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_like.setIcon(icon13)
        self.btn_like.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.btn_like)

        self.btn_trash = QPushButton(self.option_btn)
        self.btn_trash.setObjectName(u"btn_trash")
        sizePolicy6.setHeightForWidth(self.btn_trash.sizePolicy().hasHeightForWidth())
        self.btn_trash.setSizePolicy(sizePolicy6)
        self.btn_trash.setFont(font2)
        self.btn_trash.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_trash.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon14 = QIcon()
        icon14.addFile(u":/icons/feather/trash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_trash.setIcon(icon14)
        self.btn_trash.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.btn_trash)


        self.verticalLayout_2.addWidget(self.option_btn, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pwd_folder = QWidget(self.content_left)
        self.pwd_folder.setObjectName(u"pwd_folder")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(7)
        sizePolicy7.setHeightForWidth(self.pwd_folder.sizePolicy().hasHeightForWidth())
        self.pwd_folder.setSizePolicy(sizePolicy7)
        self.pwd_folder.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout_3 = QHBoxLayout(self.pwd_folder)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.treeWidget = QTreeWidget(self.pwd_folder)
        self.treeWidget.headerItem().setText(0, "")
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem.setIcon(0, icon2);
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1.setIcon(0, icon2);
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.treeWidget.setHeaderHidden(True)

        self.horizontalLayout_3.addWidget(self.treeWidget)


        self.verticalLayout_2.addWidget(self.pwd_folder)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.horizontalLayout_4.addWidget(self.content_left)

        self.content_right = QWidget(self.content_main)
        self.content_right.setObjectName(u"content_right")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(6)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.content_right.sizePolicy().hasHeightForWidth())
        self.content_right.setSizePolicy(sizePolicy8)
        self.verticalLayout_4 = QVBoxLayout(self.content_right)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.content_right)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setFrameShape(QFrame.Box)
        self.stackedWidget.setLineWidth(1)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.horizontalLayout_9 = QHBoxLayout(self.page_home)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_7 = QWidget(self.page_home)
        self.widget_7.setObjectName(u"widget_7")
        self.label = QLabel(self.widget_7)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 190, 53, 22))
        font3 = QFont()
        font3.setFamilies([u"Algerian"])
        font3.setPointSize(15)
        font3.setBold(False)
        font3.setKerning(True)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)
        self.listWidget = QListWidget(self.widget_7)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(110, 100, 256, 192))

        self.horizontalLayout_9.addWidget(self.widget_7)

        self.stackedWidget.addWidget(self.page_home)
        self.page_like = QWidget()
        self.page_like.setObjectName(u"page_like")
        self.widget_8 = QWidget(self.page_like)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(300, 160, 271, 221))
        self.label_3 = QLabel(self.widget_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 30, 53, 15))
        self.label_3.setFont(font3)
        self.stackedWidget.addWidget(self.page_like)
        self.page_trash = QWidget()
        self.page_trash.setObjectName(u"page_trash")
        self.horizontalLayout_8 = QHBoxLayout(self.page_trash)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.content_trash_left = QWidget(self.page_trash)
        self.content_trash_left.setObjectName(u"content_trash_left")
        sizePolicy8.setHeightForWidth(self.content_trash_left.sizePolicy().hasHeightForWidth())
        self.content_trash_left.setSizePolicy(sizePolicy8)
        self.content_trash_left.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget = QTableWidget(self.content_trash_left)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(80, 30, 256, 192))
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget_2 = QTableWidget(self.content_trash_left)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        if (self.tableWidget_2.rowCount() < 4):
            self.tableWidget_2.setRowCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem11)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(70, 280, 256, 192))

        self.horizontalLayout_6.addWidget(self.content_trash_left)

        self.content_trash_right = QWidget(self.page_trash)
        self.content_trash_right.setObjectName(u"content_trash_right")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(4)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.content_trash_right.sizePolicy().hasHeightForWidth())
        self.content_trash_right.setSizePolicy(sizePolicy9)
        self.label_6 = QLabel(self.content_trash_right)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 140, 200, 240))
        self.label_6.setPixmap(QPixmap(u":/icons/img/\u6682\u65e0\u6570\u636e.svg"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.content_trash_right)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.page_trash)
        self.page_folder = QWidget()
        self.page_folder.setObjectName(u"page_folder")
        self.widget_10 = QWidget(self.page_folder)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(50, 0, 613, 495))
        self.label_5 = QLabel(self.widget_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 130, 161, 191))
        self.label_5.setFont(font3)
        self.stackedWidget.addWidget(self.page_folder)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.content_right)


        self.verticalLayout.addWidget(self.content_main)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 21))
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

        self.stackedWidget.setCurrentIndex(0)


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
        self.label_img.setText(QCoreApplication.translate("MainWindow", u"adadasdsa", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_usr_info.setText(QCoreApplication.translate("MainWindow", u"1716285375@qq.com", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"  home", None))
        self.btn_like.setText(QCoreApplication.translate("MainWindow", u"  like", None))
        self.btn_trash.setText(QCoreApplication.translate("MainWindow", u"  trash", None))

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u6211\u7684\u5bc6\u7801\u5e93", None));
        ___qtreewidgetitem1 = ___qtreewidgetitem.child(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u5bc6\u7801\u5e93", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"home", None))

        __sortingEnabled1 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem7 = self.listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem8 = self.listWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem9 = self.listWidget.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        self.listWidget.setSortingEnabled(__sortingEnabled1)

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"like", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u6240\u5c5e\u5bc6\u7801\u5e93", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u65e5\u671f", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u5927\u5c0f", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem8 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem9 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem10 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem11 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        self.label_6.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"folder", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_edit.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_view.setTitle(QCoreApplication.translate("MainWindow", u"\u67e5\u770b", None))
        self.menu_option.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

