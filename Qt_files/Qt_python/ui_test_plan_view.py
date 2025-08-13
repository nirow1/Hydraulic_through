# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_plan_viewbWGdgc.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1123, 798)
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
"#widget_2, #widget_3, #widget_,#photo_tw, #phtgrm_tw, #flow_tw, #orthophoto_tw{\n"
"	border: 1px solid #ccc;\n"
"}\n"
"\n"
"#widget_165{\n"
"background-color: #ccc;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_10 = QWidget(Form)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout.addWidget(self.widget_10)

        self.widget_ = QWidget(Form)
        self.widget_.setObjectName(u"widget_")
        self.widget_.setMaximumSize(QSize(16777215, 280))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.phtgrm_tw = QTableWidget(self.widget_)
        if (self.phtgrm_tw.columnCount() < 2):
            self.phtgrm_tw.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.phtgrm_tw.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.phtgrm_tw.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.phtgrm_tw.setObjectName(u"phtgrm_tw")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phtgrm_tw.sizePolicy().hasHeightForWidth())
        self.phtgrm_tw.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.phtgrm_tw)

        self.flow_tw = QTableWidget(self.widget_)
        if (self.flow_tw.columnCount() < 3):
            self.flow_tw.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.flow_tw.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.flow_tw.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.flow_tw.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.flow_tw.setObjectName(u"flow_tw")
        sizePolicy.setHeightForWidth(self.flow_tw.sizePolicy().hasHeightForWidth())
        self.flow_tw.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.flow_tw)

        self.orthophoto_tw = QTableWidget(self.widget_)
        if (self.orthophoto_tw.columnCount() < 2):
            self.orthophoto_tw.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.orthophoto_tw.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.orthophoto_tw.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.orthophoto_tw.setObjectName(u"orthophoto_tw")
        sizePolicy.setHeightForWidth(self.orthophoto_tw.sizePolicy().hasHeightForWidth())
        self.orthophoto_tw.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.orthophoto_tw)

        self.photo_tw = QTableWidget(self.widget_)
        if (self.photo_tw.columnCount() < 4):
            self.photo_tw.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.photo_tw.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.photo_tw.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.photo_tw.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.photo_tw.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.photo_tw.setObjectName(u"photo_tw")

        self.horizontalLayout_5.addWidget(self.photo_tw)


        self.verticalLayout.addWidget(self.widget_)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 210))
        self.widget_2.setMaximumSize(QSize(16777215, 240))
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.label_4)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout = QHBoxLayout(self.widget_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.load_btn = QPushButton(self.widget_6)
        self.load_btn.setObjectName(u"load_btn")
        self.load_btn.setMaximumSize(QSize(100, 40))

        self.horizontalLayout.addWidget(self.load_btn)

        self.start_plan_btn = QPushButton(self.widget_6)
        self.start_plan_btn.setObjectName(u"start_plan_btn")
        self.start_plan_btn.setMaximumSize(QSize(150, 40))

        self.horizontalLayout.addWidget(self.start_plan_btn)

        self.continue_plan_btn = QPushButton(self.widget_6)
        self.continue_plan_btn.setObjectName(u"continue_plan_btn")
        self.continue_plan_btn.setMaximumSize(QSize(100, 40))

        self.horizontalLayout.addWidget(self.continue_plan_btn)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(200, 30))

        self.horizontalLayout_2.addWidget(self.label)


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
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.horizontalLayout_3.addWidget(self.progressBar)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.widget_1 = QWidget(self.widget_7)
        self.widget_1.setObjectName(u"widget_1")
        self.widget_1.setMaximumSize(QSize(66, 16777215))

        self.horizontalLayout_4.addWidget(self.widget_1)

        self.label_2 = QLabel(self.widget_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_4.addWidget(self.label_2)

        self.date_lbl = QLabel(self.widget_7)
        self.date_lbl.setObjectName(u"date_lbl")
        self.date_lbl.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_4.addWidget(self.date_lbl)

        self.through_lbl = QLabel(self.widget_7)
        self.through_lbl.setObjectName(u"through_lbl")
        self.through_lbl.setMaximumSize(QSize(32, 16777215))

        self.horizontalLayout_4.addWidget(self.through_lbl)

        self.label_8 = QLabel(self.widget_7)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")

        self.horizontalLayout_4.addWidget(self.widget_8)


        self.verticalLayout_2.addWidget(self.widget_7)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 100))
        self.widget_3.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.label_5)

        self.widget_11 = QWidget(self.widget_3)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMaximumSize(QSize(16777215, 400))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.widget_12)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.current_flow_lbl = QLabel(self.widget_12)
        self.current_flow_lbl.setObjectName(u"current_flow_lbl")

        self.horizontalLayout_8.addWidget(self.current_flow_lbl)

        self.label_7 = QLabel(self.widget_12)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)


        self.horizontalLayout_7.addWidget(self.widget_12)

        self.widget_9 = QWidget(self.widget_11)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMaximumSize(QSize(260, 200))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.widget_9)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.send_through_le = QLineEdit(self.widget_9)
        self.send_through_le.setObjectName(u"send_through_le")
        self.send_through_le.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_6.addWidget(self.send_through_le)

        self.send_through_btn = QPushButton(self.widget_9)
        self.send_through_btn.setObjectName(u"send_through_btn")
        self.send_through_btn.setMinimumSize(QSize(50, 0))
        self.send_through_btn.setMaximumSize(QSize(50, 35))

        self.horizontalLayout_6.addWidget(self.send_through_btn)


        self.horizontalLayout_7.addWidget(self.widget_9)


        self.verticalLayout_3.addWidget(self.widget_11)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.phtgrm_tw.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Photogrammerie ", None));
        ___qtablewidgetitem1 = self.phtgrm_tw.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Stav", None));
        ___qtablewidgetitem2 = self.flow_tw.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Datum", None));
        ___qtablewidgetitem3 = self.flow_tw.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Tok", None));
        ___qtablewidgetitem4 = self.flow_tw.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Stav", None));
        ___qtablewidgetitem5 = self.orthophoto_tw.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Orthophoto", None));
        ___qtablewidgetitem6 = self.orthophoto_tw.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Stav", None));
        ___qtablewidgetitem7 = self.photo_tw.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Datum", None));
        ___qtablewidgetitem8 = self.photo_tw.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Pozice", None));
        ___qtablewidgetitem9 = self.photo_tw.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Druh", None));
        ___qtablewidgetitem10 = self.photo_tw.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Stav", None));
        self.label_4.setText(QCoreApplication.translate("Form", u"Postup procesu:", None))
        self.load_btn.setText(QCoreApplication.translate("Form", u"Na\u010d\u00edst", None))
        self.start_plan_btn.setText(QCoreApplication.translate("Form", u"Za\u010d\u00edt pl\u00e1n", None))
        self.continue_plan_btn.setText(QCoreApplication.translate("Form", u"Pokra\u010dovat", None))
        self.label.setText(QCoreApplication.translate("Form", u"Pr\u016fb\u011bh testov\u00e9ho pl\u00e1nu...", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Dal\u0161\u00ed zm\u011bna toku:", None))
        self.date_lbl.setText(QCoreApplication.translate("Form", u"__._.____ __:__", None))
        self.through_lbl.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"l   pr\u016ftoku", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Ru\u010dn\u00ed ovl\u00e1d\u00e1n\u00ed:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Aktu\u00e1ln\u00ed pr\u016ftok:", None))
        self.current_flow_lbl.setText(QCoreApplication.translate("Form", u"00.0", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"l", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Po\u017eadovan\u00fd pr\u016ftok:", None))
        self.send_through_btn.setText(QCoreApplication.translate("Form", u"Poslat", None))
    # retranslateUi

