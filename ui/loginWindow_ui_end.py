
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont, QIcon)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QWidget)
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import end.ui.image_rc


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(550, 500)
        Form.setWindowIcon(QIcon(u':/icons/feather/command.svg'))
        # 去掉窗口边框
        Form.setWindowFlags(Qt.FramelessWindowHint)
        Form.setAttribute(Qt.WA_TranslucentBackground)



        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 550, 500))
        self.label_image = QLabel(self.widget)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(40, 30, 280, 430))
        self.label_image.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.label_image.setStyleSheet(u"border-image: url(:/icons/feather/night_bg);\n"
"border-top-left-radius:50px;")
        self.label_imageBg = QLabel(self.widget)
        self.label_imageBg.setObjectName(u"label_imageBg")
        self.label_imageBg.setGeometry(QRect(40, 30, 280, 430))
        self.label_imageBg.setStyleSheet(u"background-color: rgba(0, 0, 0, 20);\n"
"border-top-left-radius:50px;")
        self.label_content = QLabel(self.widget)
        self.label_content.setObjectName(u"label_content")
        self.label_content.setGeometry(QRect(270, 30, 240, 430))
        self.label_content.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.label_content.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius:50px;")
        self.label_titleLog = QLabel(self.widget)
        self.label_titleLog.setObjectName(u"label_titleLog")
        self.label_titleLog.setGeometry(QRect(340, 80, 100, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_titleLog.setFont(font)
        self.label_titleLog.setStyleSheet(u"color:rgba(0,0,0,200);")
        self.lineEdit_usr = QLineEdit(self.widget)
        self.lineEdit_usr.setObjectName(u"lineEdit_usr")
        self.lineEdit_usr.setGeometry(QRect(295, 150, 190, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit_usr.setFont(font1)
        self.lineEdit_usr.setStyleSheet(u"border:none;\n"
                                        "border-bottom:2px solid rgba(46,82,101,200);\n"
                                        "color: rgba(0, 0, 0, 240);\n"
                                        "padding-bottom:7px;")
        self.lineEdit_pwd = QLineEdit(self.widget)
        self.lineEdit_pwd.setObjectName(u"lineEdit_pwd")
        self.lineEdit_pwd.setGeometry(QRect(295, 215, 190, 40))
        self.lineEdit_pwd.setFont(font1)
        self.lineEdit_pwd.setStyleSheet(u"border:none;\n"
                                        "border-bottom:2px solid rgba(46,82,101,200);\n"
                                        "color: rgba(0, 0, 0, 240);\n"
                                        "padding-bottom:7px;")
        self.lineEdit_pwd.setEchoMode(QLineEdit.Password)
        self.pushButton_login = QPushButton(self.widget)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setGeometry(QRect(295, 295, 190, 40))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.pushButton_login.setFont(font2)
        self.pushButton_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_login.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=10, xOffset=3, yOffset=3))
        self.pushButton_login.setStyleSheet(u"QPushButton#pushButton_login{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255,255,255,210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_login:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0  rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#pushButton_login:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color: rgba(150, 123, 111, 255);\n"
"}")


        self.label_findAccount = QLabel(self.widget)
        self.label_findAccount.setObjectName(u"label_findAccount")
        self.label_findAccount.setOpenExternalLinks(True)
        self.label_findAccount.setGeometry(QRect(310, 350, 180, 16))
        font3 = QFont()
        font3.setPointSize(7)
        self.label_findAccount.setFont(font3)
        self.label_findAccount.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_findAccount.setStyleSheet(u"color: rgba(0, 0, 0, 210);")
        self.pushButton_close = QPushButton(self.widget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(485, 35, 20, 20))
        self.pushButton_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_close.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/icons/feather/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close.setIcon(icon)
        self.pushButton_minimize = QPushButton(self.widget)
        self.pushButton_minimize.setObjectName(u"pushButton_minimize")
        self.pushButton_minimize.setGeometry(QRect(460, 35, 20, 20))
        self.pushButton_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_minimize.setStyleSheet(u"border:none;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/feather/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_minimize.setIcon(icon1)
        self.horizontalLayoutWidget = QWidget(self.widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(320, 380, 143, 32))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_github = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_github.setObjectName(u"pushButton_github")
        font4 = QFont()
        font4.setFamilies([u"Social Media Circled"])
        font4.setPointSize(16)
        self.pushButton_github.setFont(font4)
        self.pushButton_github.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_github.setStyleSheet(u"QPushButton#pushButton_github{\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:rgba(85, 98, 112, 255);\n"
"	border-radius:2px;\n"
"}\n"
"QPushButton#pushButton_github:hover{\n"
"	color: rgba(134, 96, 53, 255);\n"
"}\n"
"QPushButton#pushButton_github:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	color: rgba(91, 88, 53, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_github)

        self.pushButton_youtube = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_youtube.setObjectName(u"pushButton_youtube")
        self.pushButton_youtube.setFont(font4)
        self.pushButton_youtube.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_youtube.setStyleSheet(u"QPushButton#pushButton_youtube{\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:rgba(85, 98, 112, 255);\n"
"	border-radius:2px;\n"
"}\n"
"QPushButton#pushButton_youtube:hover{\n"
"	color: rgba(134, 96, 53, 255);\n"
"}\n"
"QPushButton#pushButton_youtube:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	color: rgba(91, 88, 53, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_youtube)

        self.pushButton_twitter = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_twitter.setObjectName(u"pushButton_twitter")
        self.pushButton_twitter.setFont(font4)
        self.pushButton_twitter.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_twitter.setStyleSheet(u"QPushButton#pushButton_twitter{\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:rgba(85, 98, 112, 255);\n"
"	border-radius:2px;\n"
"}\n"
"QPushButton#pushButton_twitter:hover{\n"
"	color: rgba(134, 96, 53, 255);\n"
"}\n"
"QPushButton#pushButton_twitter:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	color: rgba(91, 88, 53, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_twitter)

        self.pushButton_telegram = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_telegram.setObjectName(u"pushButton_telegram")
        self.pushButton_telegram.setFont(font4)
        self.pushButton_telegram.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_telegram.setStyleSheet(u"QPushButton#pushButton_telegram{\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:rgba(85, 98, 112, 255);\n"
"	border-radius:2px;\n"
"}\n"
"QPushButton#pushButton_telegram:hover{\n"
"	color: rgba(134, 96, 53, 255);\n"
"}\n"
"QPushButton#pushButton_telegram:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	color: rgba(91, 88, 53, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_telegram)

        self.label_titleMask = QLabel(self.widget)
        self.label_titleMask.setObjectName(u"label_titleMask")
        self.label_titleMask.setGeometry(QRect(40, 80, 230, 130))
        self.label_titleMask.setStyleSheet(u"background-color: rgba(0, 0, 0, 75);")
        self.label_titleName = QLabel(self.widget)
        self.label_titleName.setObjectName(u"label_titleName")
        self.label_titleName.setGeometry(QRect(50, 80, 180, 40))
        font5 = QFont()
        font5.setFamilies([u"Book Antiqua"])
        font5.setPointSize(22)
        font5.setBold(True)
        self.label_titleName.setFont(font5)
        self.label_titleName.setStyleSheet(u"color: rgba(255, 255, 255, 200);")
        self.label_titleWelcome = QLabel(self.widget)
        self.label_titleWelcome.setObjectName(u"label_titleWelcome")
        self.label_titleWelcome.setGeometry(QRect(50, 140, 220, 55))
        self.label_titleWelcome.setAlignment(Qt.AlignCenter)
        font6 = QFont()
        font6.setFamilies([u"Garamond"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.label_titleWelcome.setFont(font6)
        self.label_titleWelcome.setStyleSheet(u"color: rgba(255, 255, 255, 170);")

        self.retranslateUi(Form)
        self.pushButton_minimize.clicked.connect(Form.showMinimized)
        self.pushButton_close.clicked.connect(Form.close)

        # 窗口居中
        self.center(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_image.setText("")
        self.label_imageBg.setText("")
        self.label_content.setText("")
        self.label_titleLog.setText(QCoreApplication.translate("Form", u"Log In", None))
        self.lineEdit_usr.setText("")
        self.lineEdit_usr.setPlaceholderText(QCoreApplication.translate("Form", u"User Name", None))
        self.lineEdit_pwd.setText("")
        self.lineEdit_pwd.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.pushButton_login.setText(QCoreApplication.translate("Form", u"Log In", None))
        self.label_findAccount.setText(QCoreApplication.translate("Form", u"<A href='http://www.mysmth.net/'>Forgot your User Name or Password?</A>", None))
        self.pushButton_close.setText("")
        self.pushButton_minimize.setText("")
        self.pushButton_github.setText(QCoreApplication.translate("Form", u")", None))
        self.pushButton_youtube.setText(QCoreApplication.translate("Form", u"P", None))
        self.pushButton_twitter.setText(QCoreApplication.translate("Form", u"D", None))
        self.pushButton_telegram.setText(QCoreApplication.translate("Form", u"(", None))
        self.label_titleMask.setText("")
        self.label_titleName.setText(QCoreApplication.translate("Form", u"BurgressPM", None))
        self.label_titleWelcome.setText(QCoreApplication.translate("Form", u"Hi,\n"
"Welcome to burgress pm.\n"
"Have a nice day!", None))

    @staticmethod
    def center(Form):
        device_screen = QGuiApplication.primaryScreen().geometry()
        currentWidth = device_screen.width()
        currentHeight = device_screen.height()
        width = Form.width()
        height = Form.height()
        Form.move((currentWidth-width)/2, (currentHeight-height)/2)



    # retranslateUi

