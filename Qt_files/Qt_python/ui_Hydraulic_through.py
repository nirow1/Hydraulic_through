# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Hydraulic_throughQGRTTw.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1161, 745)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(250, 250, 250);\n"
"border-radius: 3px;\n"
"font: 11pt \\\"Yu Gothic UI\\\";\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid rgb(180, 180, 180);\n"
"	border-radius: 5px;\n"
"	\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4CAF50;\n"
"}\n"
"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid #4CAF50;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #729D1F;\n"
"}\n"
"\n"
"#widget_2000{\n"
"	border: 1px solid #ccc;\n"
"}\n"
"        \n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    border-image: url(:/images/up_arrow_disabled.png);\n"
"}\n"
"        \n"
"QScrollBar::add-line:vertical\n"
"{\n"
"     border-image: url(:/images/down_arrow_disabled.png);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setMaximumSize(QSize(180, 16777215))
        self.widget.setStyleSheet(u"QWidget{\n"
"	background-color: #ccc;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 70))
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.logo_4j_btn = QPushButton(self.widget_3)
        self.logo_4j_btn.setObjectName(u"logo_4j_btn")
        self.logo_4j_btn.setMinimumSize(QSize(150, 50))
        self.logo_4j_btn.setMaximumSize(QSize(150, 50))
        self.logo_4j_btn.setIconSize(QSize(150, 50))

        self.verticalLayout_2.addWidget(self.logo_4j_btn)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid #4CAF50;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #729D1F;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.settings_pg_btn = QPushButton(self.widget_4)
        self.settings_pg_btn.setObjectName(u"settings_pg_btn")
        self.settings_pg_btn.setMinimumSize(QSize(0, 0))
        self.settings_pg_btn.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_3.addWidget(self.settings_pg_btn)

        self.process_pg_btn = QPushButton(self.widget_4)
        self.process_pg_btn.setObjectName(u"process_pg_btn")
        self.process_pg_btn.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_3.addWidget(self.process_pg_btn)

        self.photo_pg_btn = QPushButton(self.widget_4)
        self.photo_pg_btn.setObjectName(u"photo_pg_btn")
        self.photo_pg_btn.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_3.addWidget(self.photo_pg_btn)

        self.cam_page_btn = QPushButton(self.widget_4)
        self.cam_page_btn.setObjectName(u"cam_page_btn")
        self.cam_page_btn.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_3.addWidget(self.cam_page_btn)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_1 = QWidget(self.widget)
        self.widget_1.setObjectName(u"widget_1")
        self.widget_1.setEnabled(True)
        self.widget_1.setMaximumSize(QSize(16777215, 16777215))
        self.widget_1.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid #FF3636;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FF2626;\n"
"}")
        self.horizontalLayout_143 = QHBoxLayout(self.widget_1)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")

        self.verticalLayout.addWidget(self.widget_1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 60))
        self.widget_5.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid #FF3636;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FF2626;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stop_btn = QPushButton(self.widget_5)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setMaximumSize(QSize(1000, 40))

        self.verticalLayout_6.addWidget(self.stop_btn)


        self.verticalLayout_5.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.widget_2)


        self.horizontalLayout.addWidget(self.widget)

        self.expand_wgt = QWidget(self.centralwidget)
        self.expand_wgt.setObjectName(u"expand_wgt")
        self.expand_wgt.setMinimumSize(QSize(40, 0))
        self.expand_wgt.setMaximumSize(QSize(40, 16777215))
        self.verticalLayout_17 = QVBoxLayout(self.expand_wgt)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 24, 0, 0)
        self.expand_menu_btn = QPushButton(self.expand_wgt)
        self.expand_menu_btn.setObjectName(u"expand_menu_btn")
        self.expand_menu_btn.setMaximumSize(QSize(40, 40))
        self.expand_menu_btn.setIconSize(QSize(40, 40))

        self.verticalLayout_17.addWidget(self.expand_menu_btn)

        self.widget_17 = QWidget(self.expand_wgt)
        self.widget_17.setObjectName(u"widget_17")

        self.verticalLayout_17.addWidget(self.widget_17)


        self.horizontalLayout.addWidget(self.expand_wgt)

        self.widget_2000 = QWidget(self.centralwidget)
        self.widget_2000.setObjectName(u"widget_2000")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2000)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.widget_2000)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.widget_2000)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1161, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_4j_btn.setText("")
        self.settings_pg_btn.setText(QCoreApplication.translate("MainWindow", u"Nastaven\u00ed pl\u00e1nu", None))
        self.process_pg_btn.setText(QCoreApplication.translate("MainWindow", u"Testov\u00fd pl\u00e1n", None))
        self.photo_pg_btn.setText(QCoreApplication.translate("MainWindow", u"Photogrammetrie", None))
        self.cam_page_btn.setText(QCoreApplication.translate("MainWindow", u"Kamery", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.expand_menu_btn.setText("")
    # retranslateUi

