# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(419, 209)
        SettingsDialog.setStyleSheet(u"QDialog {border:1px solid black}")
        self.verticalLayout = QVBoxLayout(SettingsDialog)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(SettingsDialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setLineWidth(3)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.closePBtn = QPushButton(SettingsDialog)
        self.closePBtn.setObjectName(u"closePBtn")
        sizePolicy.setHeightForWidth(self.closePBtn.sizePolicy().hasHeightForWidth())
        self.closePBtn.setSizePolicy(sizePolicy)
        self.closePBtn.setMinimumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u"res/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closePBtn.setIcon(icon)
        self.closePBtn.setIconSize(QSize(25, 25))
        self.closePBtn.setFlat(True)

        self.horizontalLayout.addWidget(self.closePBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(SettingsDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.randomFireLabel = QLabel(SettingsDialog)
        self.randomFireLabel.setObjectName(u"randomFireLabel")

        self.gridLayout.addWidget(self.randomFireLabel, 1, 1, 1, 1)

        self.newTreeLabel = QLabel(SettingsDialog)
        self.newTreeLabel.setObjectName(u"newTreeLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.newTreeLabel.sizePolicy().hasHeightForWidth())
        self.newTreeLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.newTreeLabel, 2, 1, 1, 1)

        self.windCBox = QComboBox(SettingsDialog)
        self.windCBox.addItem("")
        self.windCBox.addItem("")
        self.windCBox.addItem("")
        self.windCBox.addItem("")
        self.windCBox.addItem("")
        self.windCBox.addItem("")
        self.windCBox.addItem("")
        self.windCBox.addItem("")
        self.windCBox.addItem("")
        self.windCBox.setObjectName(u"windCBox")
        self.windCBox.setEditable(False)

        self.gridLayout.addWidget(self.windCBox, 3, 0, 1, 1)

        self.randomFireBox = QDoubleSpinBox(SettingsDialog)
        self.randomFireBox.setObjectName(u"randomFireBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.randomFireBox.sizePolicy().hasHeightForWidth())
        self.randomFireBox.setSizePolicy(sizePolicy2)
        self.randomFireBox.setDecimals(3)
        self.randomFireBox.setMinimum(0.000000000000000)
        self.randomFireBox.setMaximum(50.000000000000000)
        self.randomFireBox.setSingleStep(0.005000000000000)
        self.randomFireBox.setValue(0.001000000000000)

        self.gridLayout.addWidget(self.randomFireBox, 1, 0, 1, 1)

        self.label_2 = QLabel(SettingsDialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

        self.treeFactorBox = QSpinBox(SettingsDialog)
        self.treeFactorBox.setObjectName(u"treeFactorBox")
        self.treeFactorBox.setMinimum(5)
        self.treeFactorBox.setMaximum(100)
        self.treeFactorBox.setSingleStep(5)
        self.treeFactorBox.setValue(80)

        self.gridLayout.addWidget(self.treeFactorBox, 0, 0, 1, 1)

        self.newTreeBox = QDoubleSpinBox(SettingsDialog)
        self.newTreeBox.setObjectName(u"newTreeBox")
        sizePolicy2.setHeightForWidth(self.newTreeBox.sizePolicy().hasHeightForWidth())
        self.newTreeBox.setSizePolicy(sizePolicy2)
        self.newTreeBox.setDecimals(3)
        self.newTreeBox.setMinimum(0.000000000000000)
        self.newTreeBox.setMaximum(50.000000000000000)
        self.newTreeBox.setSingleStep(0.100000000000000)
        self.newTreeBox.setValue(0.050000000000000)

        self.gridLayout.addWidget(self.newTreeBox, 2, 0, 1, 1)

        self.treeFactorLabel = QLabel(SettingsDialog)
        self.treeFactorLabel.setObjectName(u"treeFactorLabel")

        self.gridLayout.addWidget(self.treeFactorLabel, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox_2 = QDialogButtonBox(SettingsDialog)
        self.buttonBox_2.setObjectName(u"buttonBox_2")
        self.buttonBox_2.setOrientation(Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox_2)

        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(SettingsDialog)
        self.buttonBox_2.accepted.connect(SettingsDialog.accept)
        self.buttonBox_2.rejected.connect(SettingsDialog.reject)

        self.windCBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0440\u0435\u0434\u044b \u0441\u0438\u043c\u0443\u043b\u044f\u0446\u0438\u0438", None))
        self.closePBtn.setText("")
        self.randomFireLabel.setText(QCoreApplication.translate("SettingsDialog", u"\u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u043e\u0433\u043e \u0432\u043e\u0437\u0433\u043e\u0440\u0430\u043d\u0438\u044f \u0434\u0435\u0440\u0435\u0432\u0430", None))
        self.newTreeLabel.setText(QCoreApplication.translate("SettingsDialog", u"\u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043f\u043e\u044f\u0432\u043b\u0435\u043d\u0438\u044f \u043d\u043e\u0432\u043e\u0433\u043e \u0434\u0435\u0440\u0435\u0432\u0430 \u043d\u0430 \u043f\u043e\u043b\u0435", None))
        self.windCBox.setItemText(0, QCoreApplication.translate("SettingsDialog", u"\u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.windCBox.setItemText(1, QCoreApplication.translate("SettingsDialog", u"\u0441\u0435\u0432\u0435\u0440\u043d\u044b\u0439", None))
        self.windCBox.setItemText(2, QCoreApplication.translate("SettingsDialog", u"\u044e\u0436\u043d\u044b\u0439", None))
        self.windCBox.setItemText(3, QCoreApplication.translate("SettingsDialog", u"\u0437\u0430\u043f\u0430\u0434\u043d\u044b\u0439", None))
        self.windCBox.setItemText(4, QCoreApplication.translate("SettingsDialog", u"\u0432\u043e\u0441\u0442\u043e\u0447\u043d\u044b\u0439", None))
        self.windCBox.setItemText(5, QCoreApplication.translate("SettingsDialog", u"\u0441-\u0437\u0430\u043f\u0430\u0434\u043d\u044b\u0439", None))
        self.windCBox.setItemText(6, QCoreApplication.translate("SettingsDialog", u"\u0441-\u0432\u043e\u0441\u0442\u043e\u0447\u043d\u044b\u0439", None))
        self.windCBox.setItemText(7, QCoreApplication.translate("SettingsDialog", u"\u044e-\u0437\u0430\u043f\u0430\u0434\u043d\u044b\u0439", None))
        self.windCBox.setItemText(8, QCoreApplication.translate("SettingsDialog", u"\u044e-\u0432\u043e\u0441\u0442\u043e\u0447\u043d\u044b\u0439", None))

        self.windCBox.setCurrentText(QCoreApplication.translate("SettingsDialog", u"\u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.randomFireBox.setSuffix(QCoreApplication.translate("SettingsDialog", u"%", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"\u0432\u0435\u0442\u0435\u0440", None))
        self.treeFactorBox.setSuffix(QCoreApplication.translate("SettingsDialog", u"%", None))
        self.treeFactorBox.setPrefix("")
        self.newTreeBox.setSuffix(QCoreApplication.translate("SettingsDialog", u"%", None))
        self.treeFactorLabel.setText(QCoreApplication.translate("SettingsDialog", u"\u043f\u0440\u043e\u0446\u0435\u043d\u0442 \u043f\u043b\u043e\u0449\u0430\u0434\u0438 \u043f\u043e\u043b\u044f, \u0437\u0430\u043d\u0438\u043c\u0430\u0435\u043c\u043e\u0439 \u0434\u0435\u0440\u0435\u0432\u044c\u044f\u043c\u0438", None))
    # retranslateUi

