# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera_viewOqDtHd.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(961, 769)
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
"#stackedWidget, #widget_6, #widget_10{\n"
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
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_10 = QWidget(Form)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_10.setMinimumSize(QSize(0, 50))
        self.widget_10.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cam_1_pg_btn = QPushButton(self.widget_10)
        self.cam_1_pg_btn.setObjectName(u"cam_1_pg_btn")
        self.cam_1_pg_btn.setMaximumSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.cam_1_pg_btn)

        self.cam_2_pg_btn = QPushButton(self.widget_10)
        self.cam_2_pg_btn.setObjectName(u"cam_2_pg_btn")
        self.cam_2_pg_btn.setMaximumSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.cam_2_pg_btn)


        self.verticalLayout.addWidget(self.widget_10)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.cam_1_pg = QWidget()
        self.cam_1_pg.setObjectName(u"cam_1_pg")
        self.verticalLayout_5 = QVBoxLayout(self.cam_1_pg)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.widget_9 = QWidget(self.cam_1_pg)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_6 = QVBoxLayout(self.widget_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_20 = QWidget(self.widget_9)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(280, 0))
        self.widget_20.setMaximumSize(QSize(167777, 16777215))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cam_lbl_1 = QLabel(self.widget_20)
        self.cam_lbl_1.setObjectName(u"cam_lbl_1")
        self.cam_lbl_1.setMaximumSize(QSize(800, 16777215))

        self.horizontalLayout_5.addWidget(self.cam_lbl_1)


        self.verticalLayout_6.addWidget(self.widget_20)

        self.widget_4 = QWidget(self.widget_9)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 50))
        self.widget_4.setMaximumSize(QSize(167777, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.save_video_btn = QPushButton(self.widget_4)
        self.save_video_btn.setObjectName(u"save_video_btn")
        self.save_video_btn.setMaximumSize(QSize(120, 35))

        self.horizontalLayout_3.addWidget(self.save_video_btn)

        self.save_photo_btn = QPushButton(self.widget_4)
        self.save_photo_btn.setObjectName(u"save_photo_btn")
        self.save_photo_btn.setMaximumSize(QSize(120, 35))

        self.horizontalLayout_3.addWidget(self.save_photo_btn)


        self.verticalLayout_6.addWidget(self.widget_4)


        self.verticalLayout_5.addWidget(self.widget_9)

        self.stackedWidget.addWidget(self.cam_1_pg)
        self.cam_2_pg = QWidget()
        self.cam_2_pg.setObjectName(u"cam_2_pg")
        self.horizontalLayout_17 = QHBoxLayout(self.cam_2_pg)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(1, 1, 1, 1)
        self.widget_14 = QWidget(self.cam_2_pg)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_2 = QVBoxLayout(self.widget_14)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(0, 0))
        self.widget_15.setMaximumSize(QSize(16777, 16777215))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.cam_lbl_2 = QLabel(self.widget_15)
        self.cam_lbl_2.setObjectName(u"cam_lbl_2")
        self.cam_lbl_2.setMaximumSize(QSize(800, 16777215))

        self.horizontalLayout_12.addWidget(self.cam_lbl_2)


        self.verticalLayout_2.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.widget_14)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMaximumSize(QSize(16777, 50))
        self.verticalLayout_4 = QVBoxLayout(self.widget_16)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_19 = QWidget(self.widget_16)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(0, 50))
        self.widget_19.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.save_video_btn_2 = QPushButton(self.widget_19)
        self.save_video_btn_2.setObjectName(u"save_video_btn_2")
        self.save_video_btn_2.setMaximumSize(QSize(120, 35))

        self.horizontalLayout_15.addWidget(self.save_video_btn_2)

        self.save_photo_btn_2 = QPushButton(self.widget_19)
        self.save_photo_btn_2.setObjectName(u"save_photo_btn_2")
        self.save_photo_btn_2.setMaximumSize(QSize(120, 35))

        self.horizontalLayout_15.addWidget(self.save_photo_btn_2)


        self.verticalLayout_4.addWidget(self.widget_19)


        self.verticalLayout_2.addWidget(self.widget_16)


        self.horizontalLayout_17.addWidget(self.widget_14)

        self.stackedWidget.addWidget(self.cam_2_pg)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.widget_8 = QWidget(Form)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.start_ortophoto_btn = QPushButton(self.widget_8)
        self.start_ortophoto_btn.setObjectName(u"start_ortophoto_btn")
        self.start_ortophoto_btn.setMaximumSize(QSize(120, 35))

        self.horizontalLayout_7.addWidget(self.start_ortophoto_btn)

        self.widget_3 = QWidget(self.widget_8)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(200, 60))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.set_pos_le = QLineEdit(self.widget_3)
        self.set_pos_le.setObjectName(u"set_pos_le")
        self.set_pos_le.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.set_pos_le)

        self.set_pos_btn = QPushButton(self.widget_3)
        self.set_pos_btn.setObjectName(u"set_pos_btn")
        self.set_pos_btn.setMinimumSize(QSize(75, 30))

        self.horizontalLayout_6.addWidget(self.set_pos_btn)


        self.horizontalLayout_7.addWidget(self.widget_3)

        self.widget_ = QWidget(self.widget_8)
        self.widget_.setObjectName(u"widget_")
        self.widget_.setMaximumSize(QSize(200, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.left_btn = QPushButton(self.widget_)
        self.left_btn.setObjectName(u"left_btn")
        self.left_btn.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.left_btn)

        self.right_btn = QPushButton(self.widget_)
        self.right_btn.setObjectName(u"right_btn")
        self.right_btn.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.right_btn)


        self.horizontalLayout_7.addWidget(self.widget_)


        self.verticalLayout.addWidget(self.widget_8)

        self.widget_29 = QWidget(Form)
        self.widget_29.setObjectName(u"widget_29")
        sizePolicy.setHeightForWidth(self.widget_29.sizePolicy().hasHeightForWidth())
        self.widget_29.setSizePolicy(sizePolicy)
        self.widget_29.setMinimumSize(QSize(0, 100))
        self.widget_29.setMaximumSize(QSize(16777215, 110))
        self.horizontalLayout = QHBoxLayout(self.widget_29)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.widget_12 = QWidget(self.widget_29)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget_12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.widget_13)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_10.addWidget(self.label)

        self.currnet_action_lbl = QLabel(self.widget_13)
        self.currnet_action_lbl.setObjectName(u"currnet_action_lbl")

        self.horizontalLayout_10.addWidget(self.currnet_action_lbl)


        self.verticalLayout_3.addWidget(self.widget_13)

        self.orthophoto_pb = QProgressBar(self.widget_12)
        self.orthophoto_pb.setObjectName(u"orthophoto_pb")
        self.orthophoto_pb.setValue(0)
        self.orthophoto_pb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.orthophoto_pb)


        self.horizontalLayout.addWidget(self.widget_12)


        self.verticalLayout.addWidget(self.widget_29)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.cam_1_pg_btn.setText(QCoreApplication.translate("Form", u"1", None))
        self.cam_2_pg_btn.setText(QCoreApplication.translate("Form", u"2", None))
        self.cam_lbl_1.setText("")
        self.save_video_btn.setText(QCoreApplication.translate("Form", u"Ulo\u017eit video", None))
        self.save_photo_btn.setText(QCoreApplication.translate("Form", u"Ulo\u017eit foto", None))
        self.cam_lbl_2.setText("")
        self.save_video_btn_2.setText(QCoreApplication.translate("Form", u"Ulo\u017eit Video", None))
        self.save_photo_btn_2.setText(QCoreApplication.translate("Form", u"Ulo\u017eit foto", None))
        self.start_ortophoto_btn.setText(QCoreApplication.translate("Form", u"Za\u010d\u00edt ortophoto ", None))
        self.set_pos_btn.setText(QCoreApplication.translate("Form", u"P\u0159esunout", None))
        self.left_btn.setText("")
        self.right_btn.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Ortophoto:", None))
        self.currnet_action_lbl.setText("")
    # retranslateUi

