# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QSizePolicy,
    QSpacerItem, QStatusBar, QToolButton, QVBoxLayout,
    QWidget)

from fieldgview import FieldGView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 780)
        self.mainWidget = QWidget(MainWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.verticalLayout_2 = QVBoxLayout(self.mainWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainVLayout = QVBoxLayout()
        self.mainVLayout.setObjectName(u"mainVLayout")
        self.toolBarHLayout = QHBoxLayout()
        self.toolBarHLayout.setObjectName(u"toolBarHLayout")
        self.leftToolBarHLayout = QHBoxLayout()
        self.leftToolBarHLayout.setObjectName(u"leftToolBarHLayout")
        self.startSimulationTBtn = QToolButton(self.mainWidget)
        self.startSimulationTBtn.setObjectName(u"startSimulationTBtn")

        self.leftToolBarHLayout.addWidget(self.startSimulationTBtn)

        self.stopSimulationTBtn = QToolButton(self.mainWidget)
        self.stopSimulationTBtn.setObjectName(u"stopSimulationTBtn")

        self.leftToolBarHLayout.addWidget(self.stopSimulationTBtn)


        self.toolBarHLayout.addLayout(self.leftToolBarHLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.toolBarHLayout.addItem(self.horizontalSpacer)

        self.rightToolBarHLayout = QHBoxLayout()
        self.rightToolBarHLayout.setObjectName(u"rightToolBarHLayout")
        self.randomFieldTBtn = QToolButton(self.mainWidget)
        self.randomFieldTBtn.setObjectName(u"randomFieldTBtn")

        self.rightToolBarHLayout.addWidget(self.randomFieldTBtn)

        self.editFieldTBtn = QToolButton(self.mainWidget)
        self.editFieldTBtn.setObjectName(u"editFieldTBtn")

        self.rightToolBarHLayout.addWidget(self.editFieldTBtn)

        self.settingsTBtn = QToolButton(self.mainWidget)
        self.settingsTBtn.setObjectName(u"settingsTBtn")

        self.rightToolBarHLayout.addWidget(self.settingsTBtn)


        self.toolBarHLayout.addLayout(self.rightToolBarHLayout)


        self.mainVLayout.addLayout(self.toolBarHLayout)

        self.field = FieldGView(self.mainWidget)
        self.field.setObjectName(u"field")

        self.mainVLayout.addWidget(self.field)


        self.verticalLayout_2.addLayout(self.mainVLayout)

        MainWindow.setCentralWidget(self.mainWidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043c\u0443\u043b\u044f\u0446\u0438\u044f \u043f\u043e\u0436\u0430\u0440\u043e\u0432", None))
        self.startSimulationTBtn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0441\u0438\u043c\u0443\u043b\u044f\u0446\u0438\u044e", None))
        self.stopSimulationTBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043d\u0430 \u043f\u0430\u0443\u0437\u0443", None))
        self.randomFieldTBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0443\u0447\u0430\u0439\u043d\u043e\u0435 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435", None))
        self.editFieldTBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e\u043b\u0435", None))
        self.settingsTBtn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0438\u043c\u0443\u043b\u044f\u0446\u0438\u0438", None))
    # retranslateUi

