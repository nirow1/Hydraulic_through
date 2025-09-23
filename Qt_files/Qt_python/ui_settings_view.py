# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_viewiSAPBO.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1087, 705)
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
"#widget_14, #widget, #widget_15{\n"
"	border: 1px solid #ccc;\n"
"}\n"
"\n"
"#widget_165{\n"
"background-color: #ccc;\n"
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
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_49 = QWidget(Form)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setMinimumSize(QSize(0, 50))
        self.verticalLayout_3 = QVBoxLayout(self.widget_49)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_15 = QWidget(self.widget_49)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_4 = QVBoxLayout(self.widget_15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 3, 5, 3)
        self.widget_2 = QWidget(self.widget_15)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_2.addWidget(self.label_9)

        self.set_saving_path_le = QLineEdit(self.widget_2)
        self.set_saving_path_le.setObjectName(u"set_saving_path_le")
        self.set_saving_path_le.setEnabled(False)
        self.set_saving_path_le.setMinimumSize(QSize(0, 35))
        self.set_saving_path_le.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_2.addWidget(self.set_saving_path_le)

        self.save_path_dir_btn = QPushButton(self.widget_2)
        self.save_path_dir_btn.setObjectName(u"save_path_dir_btn")
        self.save_path_dir_btn.setMinimumSize(QSize(40, 0))
        self.save_path_dir_btn.setMaximumSize(QSize(16777215, 35))
        self.save_path_dir_btn.setIconSize(QSize(40, 35))

        self.horizontalLayout_2.addWidget(self.save_path_dir_btn)

        self.set_saving_path_btn = QPushButton(self.widget_2)
        self.set_saving_path_btn.setObjectName(u"set_saving_path_btn")
        self.set_saving_path_btn.setMinimumSize(QSize(70, 0))
        self.set_saving_path_btn.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_2.addWidget(self.set_saving_path_btn)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget_15)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(126, 16777215))
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.current_saving_path_lbl = QLabel(self.widget_3)
        self.current_saving_path_lbl.setObjectName(u"current_saving_path_lbl")

        self.horizontalLayout_3.addWidget(self.current_saving_path_lbl)


        self.verticalLayout_4.addWidget(self.widget_3)


        self.verticalLayout_3.addWidget(self.widget_15)

        self.widget_14 = QWidget(self.widget_49)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 3, 5, 3)
        self.label_8 = QLabel(self.widget_14)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.xml_file_dir_le = QLineEdit(self.widget_14)
        self.xml_file_dir_le.setObjectName(u"xml_file_dir_le")
        self.xml_file_dir_le.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_7.addWidget(self.xml_file_dir_le)

        self.xml_file_dir_btn = QPushButton(self.widget_14)
        self.xml_file_dir_btn.setObjectName(u"xml_file_dir_btn")
        self.xml_file_dir_btn.setMinimumSize(QSize(40, 35))
        self.xml_file_dir_btn.setIconSize(QSize(40, 35))

        self.horizontalLayout_7.addWidget(self.xml_file_dir_btn)


        self.verticalLayout_3.addWidget(self.widget_14)

        self.widget_5 = QWidget(self.widget_49)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_13 = QVBoxLayout(self.widget_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 5, 0, 5)
        self.widget = QWidget(self.widget_5)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.widget_13 = QWidget(self.widget)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.widget_13)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.add_row_btn = QPushButton(self.widget_13)
        self.add_row_btn.setObjectName(u"add_row_btn")
        self.add_row_btn.setMaximumSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.add_row_btn)

        self.delete_row_btn = QPushButton(self.widget_13)
        self.delete_row_btn.setObjectName(u"delete_row_btn")
        self.delete_row_btn.setMaximumSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.delete_row_btn)


        self.verticalLayout_2.addWidget(self.widget_13)


        self.verticalLayout_13.addWidget(self.widget)

        self.widget_28 = QWidget(self.widget_5)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.generate_test_plan_btn = QPushButton(self.widget_28)
        self.generate_test_plan_btn.setObjectName(u"generate_test_plan_btn")
        self.generate_test_plan_btn.setMaximumSize(QSize(200, 35))

        self.horizontalLayout_4.addWidget(self.generate_test_plan_btn)


        self.verticalLayout_13.addWidget(self.widget_28)


        self.verticalLayout_3.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.widget_49)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Nastaven\u00ed ulo\u017ei\u0161t\u011b:", None))
        self.save_path_dir_btn.setText("")
        self.set_saving_path_btn.setText(QCoreApplication.translate("Form", u"Nastavit", None))
        self.label.setText(QCoreApplication.translate("Form", u"Aktu\u00e1ln\u00ed ulo\u017ei\u0161t\u011b: ", None))
        self.current_saving_path_lbl.setText(QCoreApplication.translate("Form", u"./", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Na\u010d\u00edst pl\u00e1n:", None))
        self.xml_file_dir_btn.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Den", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Hod", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Min", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Sek", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Pr\u016ftok", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Photogrammetrie", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Orthophoto", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Foto 1", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Foto 2", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Video 1", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Video 2", None));
        self.add_row_btn.setText(QCoreApplication.translate("Form", u"+", None))
        self.delete_row_btn.setText(QCoreApplication.translate("Form", u"-", None))
        self.generate_test_plan_btn.setText(QCoreApplication.translate("Form", u"Vygeneruj test pl\u00e1n", None))
    # retranslateUi

