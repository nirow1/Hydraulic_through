# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Photogrammetry_viewkskBjU.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1082, 693)
        Form.setStyleSheet(u"QWidget{\n"
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
"    border-radius: 10px;\n"
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
"#widget_2, #widget_3, #tableWidget{\n"
"	border: 1px solid #ccc;\n"
"}\n"
"\n"
"#widget_165{\n"
"background-color: #ccc;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_9 = QWidget(Form)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMaximumSize(QSize(16777215, 70))

        self.verticalLayout.addWidget(self.widget_9)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_10 = QWidget(self.widget_3)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_4.addWidget(self.widget_10)

        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(220, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.widget_7)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.tableWidget = QTableWidget(self.widget_7)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.widget_1 = QWidget(self.widget_7)
        self.widget_1.setObjectName(u"widget_1")
        self.widget_1.setMinimumSize(QSize(0, 45))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.add_phtgrm_btn = QPushButton(self.widget_1)
        self.add_phtgrm_btn.setObjectName(u"add_phtgrm_btn")
        self.add_phtgrm_btn.setMinimumSize(QSize(0, 30))
        self.add_phtgrm_btn.setMaximumSize(QSize(55, 30))

        self.horizontalLayout_5.addWidget(self.add_phtgrm_btn)

        self.save_phtfrm_tab_btn = QPushButton(self.widget_1)
        self.save_phtfrm_tab_btn.setObjectName(u"save_phtfrm_tab_btn")
        self.save_phtfrm_tab_btn.setMaximumSize(QSize(55, 30))

        self.horizontalLayout_5.addWidget(self.save_phtfrm_tab_btn)


        self.verticalLayout_3.addWidget(self.widget_1)


        self.horizontalLayout_4.addWidget(self.widget_7)

        self.widget_11 = QWidget(self.widget_3)
        self.widget_11.setObjectName(u"widget_11")

        self.horizontalLayout_4.addWidget(self.widget_11)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 180))
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout = QHBoxLayout(self.widget_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(330, 100))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.start_new_phtgrm_btn = QPushButton(self.widget_8)
        self.start_new_phtgrm_btn.setObjectName(u"start_new_phtgrm_btn")
        self.start_new_phtgrm_btn.setMaximumSize(QSize(160, 40))

        self.horizontalLayout_7.addWidget(self.start_new_phtgrm_btn)

        self.continue_phtgrm_btn = QPushButton(self.widget_8)
        self.continue_phtgrm_btn.setObjectName(u"continue_phtgrm_btn")
        self.continue_phtgrm_btn.setMaximumSize(QSize(160, 40))

        self.horizontalLayout_7.addWidget(self.continue_phtgrm_btn)


        self.horizontalLayout.addWidget(self.widget_8)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_5)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_2.addWidget(self.widget)

        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(164, 30))

        self.horizontalLayout_2.addWidget(self.label)

        self.progress_lbl = QLabel(self.widget_5)
        self.progress_lbl.setObjectName(u"progress_lbl")

        self.horizontalLayout_2.addWidget(self.progress_lbl)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.progressBar = QProgressBar(self.widget_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(600, 16777215))
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout_3.addWidget(self.progressBar)


        self.verticalLayout_2.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_12 = QWidget(Form)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMaximumSize(QSize(16777215, 70))

        self.verticalLayout.addWidget(self.widget_12)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Napl\u00e1novan\u00e9 photogrametrie", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Datum", None));
        self.add_phtgrm_btn.setText(QCoreApplication.translate("Form", u"P\u0159idat", None))
        self.save_phtfrm_tab_btn.setText(QCoreApplication.translate("Form", u"Ulo\u017eit", None))
        self.start_new_phtgrm_btn.setText(QCoreApplication.translate("Form", u"Za\u010d\u00edt photogrammetrii", None))
        self.continue_phtgrm_btn.setText(QCoreApplication.translate("Form", u"pokra\u010dovat", None))
        self.label.setText(QCoreApplication.translate("Form", u"Pr\u016fb\u011bh fotogrammetrie:", None))
        self.progress_lbl.setText("")
    # retranslateUi

