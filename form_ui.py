# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

from fieldgview import FieldGView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1542, 788)
        MainWindow.setStyleSheet(u"QMainWindow {border:1px solid black}")
        self.mainWidget = QWidget(MainWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.verticalLayout = QVBoxLayout(self.mainWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.minimizePBtn = QPushButton(self.mainWidget)
        self.minimizePBtn.setObjectName(u"minimizePBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimizePBtn.sizePolicy().hasHeightForWidth())
        self.minimizePBtn.setSizePolicy(sizePolicy)
        self.minimizePBtn.setMinimumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u"res/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizePBtn.setIcon(icon)
        self.minimizePBtn.setIconSize(QSize(25, 25))
        self.minimizePBtn.setFlat(True)

        self.horizontalLayout.addWidget(self.minimizePBtn)

        self.maximizePBtn = QPushButton(self.mainWidget)
        self.maximizePBtn.setObjectName(u"maximizePBtn")
        sizePolicy.setHeightForWidth(self.maximizePBtn.sizePolicy().hasHeightForWidth())
        self.maximizePBtn.setSizePolicy(sizePolicy)
        self.maximizePBtn.setMinimumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u"res/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizePBtn.setIcon(icon1)
        self.maximizePBtn.setIconSize(QSize(25, 25))
        self.maximizePBtn.setFlat(True)

        self.horizontalLayout.addWidget(self.maximizePBtn)

        self.closePBtn = QPushButton(self.mainWidget)
        self.closePBtn.setObjectName(u"closePBtn")
        sizePolicy.setHeightForWidth(self.closePBtn.sizePolicy().hasHeightForWidth())
        self.closePBtn.setSizePolicy(sizePolicy)
        self.closePBtn.setMinimumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u"res/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closePBtn.setIcon(icon2)
        self.closePBtn.setIconSize(QSize(25, 25))
        self.closePBtn.setFlat(True)

        self.horizontalLayout.addWidget(self.closePBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(self.mainWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.mainVLayout = QVBoxLayout()
        self.mainVLayout.setObjectName(u"mainVLayout")
        self.toolBarHLayout = QHBoxLayout()
        self.toolBarHLayout.setObjectName(u"toolBarHLayout")
        self.leftToolBarHLayout = QHBoxLayout()
        self.leftToolBarHLayout.setObjectName(u"leftToolBarHLayout")
        self.startSimulationTBtn = QPushButton(self.mainWidget)
        self.startSimulationTBtn.setObjectName(u"startSimulationTBtn")
        self.startSimulationTBtn.setMinimumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u"res/play-Photoroom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startSimulationTBtn.setIcon(icon3)
        self.startSimulationTBtn.setIconSize(QSize(25, 25))
        self.startSimulationTBtn.setFlat(True)

        self.leftToolBarHLayout.addWidget(self.startSimulationTBtn)

        self.stepSimPBtn = QPushButton(self.mainWidget)
        self.stepSimPBtn.setObjectName(u"stepSimPBtn")
        sizePolicy.setHeightForWidth(self.stepSimPBtn.sizePolicy().hasHeightForWidth())
        self.stepSimPBtn.setSizePolicy(sizePolicy)
        self.stepSimPBtn.setMinimumSize(QSize(30, 30))
        icon4 = QIcon()
        icon4.addFile(u"res/sim_step.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stepSimPBtn.setIcon(icon4)
        self.stepSimPBtn.setIconSize(QSize(25, 25))
        self.stepSimPBtn.setAutoRepeat(True)
        self.stepSimPBtn.setFlat(True)

        self.leftToolBarHLayout.addWidget(self.stepSimPBtn)

        self.stopSimulationTBtn = QPushButton(self.mainWidget)
        self.stopSimulationTBtn.setObjectName(u"stopSimulationTBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(30)
        sizePolicy1.setVerticalStretch(30)
        sizePolicy1.setHeightForWidth(self.stopSimulationTBtn.sizePolicy().hasHeightForWidth())
        self.stopSimulationTBtn.setSizePolicy(sizePolicy1)
        icon5 = QIcon()
        icon5.addFile(u"res/pause-Photoroom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopSimulationTBtn.setIcon(icon5)
        self.stopSimulationTBtn.setIconSize(QSize(25, 25))
        self.stopSimulationTBtn.setFlat(True)

        self.leftToolBarHLayout.addWidget(self.stopSimulationTBtn)


        self.toolBarHLayout.addLayout(self.leftToolBarHLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.toolBarHLayout.addItem(self.horizontalSpacer)

        self.rightToolBarHLayout = QHBoxLayout()
        self.rightToolBarHLayout.setObjectName(u"rightToolBarHLayout")
        self.editFieldTBtn = QPushButton(self.mainWidget)
        self.editFieldTBtn.setObjectName(u"editFieldTBtn")
        self.editFieldTBtn.setMinimumSize(QSize(30, 30))
        icon6 = QIcon()
        icon6.addFile(u"res/forest_settings-Photoroom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editFieldTBtn.setIcon(icon6)
        self.editFieldTBtn.setIconSize(QSize(25, 25))
        self.editFieldTBtn.setFlat(True)

        self.rightToolBarHLayout.addWidget(self.editFieldTBtn)

        self.settingsTBtn = QPushButton(self.mainWidget)
        self.settingsTBtn.setObjectName(u"settingsTBtn")
        self.settingsTBtn.setMinimumSize(QSize(30, 30))
        icon7 = QIcon()
        icon7.addFile(u"res/simulation_settings-Photoroom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTBtn.setIcon(icon7)
        self.settingsTBtn.setIconSize(QSize(25, 25))
        self.settingsTBtn.setFlat(True)

        self.rightToolBarHLayout.addWidget(self.settingsTBtn)


        self.toolBarHLayout.addLayout(self.rightToolBarHLayout)


        self.mainVLayout.addLayout(self.toolBarHLayout)

        self.line_2 = QFrame(self.mainWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.mainVLayout.addWidget(self.line_2)

        self.field = FieldGView(self.mainWidget)
        self.field.setObjectName(u"field")

        self.mainVLayout.addWidget(self.field)


        self.verticalLayout.addLayout(self.mainVLayout)

        MainWindow.setCentralWidget(self.mainWidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043c\u0443\u043b\u044f\u0446\u0438\u044f \u043f\u043e\u0436\u0430\u0440\u043e\u0432", None))
        self.minimizePBtn.setText("")
        self.maximizePBtn.setText("")
        self.closePBtn.setText("")
        self.startSimulationTBtn.setText("")
        self.stepSimPBtn.setText("")
        self.stopSimulationTBtn.setText("")
        self.editFieldTBtn.setText("")
        self.settingsTBtn.setText("")
    # retranslateUi

