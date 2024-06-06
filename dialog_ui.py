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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QDoubleSpinBox, QHBoxLayout, QLabel, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(396, 117)
        self.verticalLayout_3 = QVBoxLayout(SettingsDialog)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.mainHLayout = QHBoxLayout()
        self.mainHLayout.setObjectName(u"mainHLayout")
        self.boxVLayout = QVBoxLayout()
        self.boxVLayout.setObjectName(u"boxVLayout")
        self.treeFactorBox = QSpinBox(SettingsDialog)
        self.treeFactorBox.setObjectName(u"treeFactorBox")
        self.treeFactorBox.setMinimum(5)
        self.treeFactorBox.setMaximum(100)
        self.treeFactorBox.setSingleStep(5)
        self.treeFactorBox.setValue(80)

        self.boxVLayout.addWidget(self.treeFactorBox)

        self.randomFireBox = QDoubleSpinBox(SettingsDialog)
        self.randomFireBox.setObjectName(u"randomFireBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.randomFireBox.sizePolicy().hasHeightForWidth())
        self.randomFireBox.setSizePolicy(sizePolicy)
        self.randomFireBox.setDecimals(3)
        self.randomFireBox.setMinimum(0.000000000000000)
        self.randomFireBox.setMaximum(50.000000000000000)
        self.randomFireBox.setSingleStep(0.005000000000000)
        self.randomFireBox.setValue(0.001000000000000)

        self.boxVLayout.addWidget(self.randomFireBox)

        self.newTreeBox = QDoubleSpinBox(SettingsDialog)
        self.newTreeBox.setObjectName(u"newTreeBox")
        sizePolicy.setHeightForWidth(self.newTreeBox.sizePolicy().hasHeightForWidth())
        self.newTreeBox.setSizePolicy(sizePolicy)
        self.newTreeBox.setDecimals(3)
        self.newTreeBox.setMinimum(0.000000000000000)
        self.newTreeBox.setMaximum(50.000000000000000)
        self.newTreeBox.setSingleStep(0.100000000000000)
        self.newTreeBox.setValue(0.050000000000000)

        self.boxVLayout.addWidget(self.newTreeBox)

        self.wetFactorBox = QSpinBox(SettingsDialog)
        self.wetFactorBox.setObjectName(u"wetFactorBox")

        self.boxVLayout.addWidget(self.wetFactorBox)


        self.mainHLayout.addLayout(self.boxVLayout)

        self.textVLayout = QVBoxLayout()
        self.textVLayout.setObjectName(u"textVLayout")
        self.treeFactorLabel = QLabel(SettingsDialog)
        self.treeFactorLabel.setObjectName(u"treeFactorLabel")

        self.textVLayout.addWidget(self.treeFactorLabel)

        self.randomFireLabel = QLabel(SettingsDialog)
        self.randomFireLabel.setObjectName(u"randomFireLabel")

        self.textVLayout.addWidget(self.randomFireLabel)

        self.newTreeLabel = QLabel(SettingsDialog)
        self.newTreeLabel.setObjectName(u"newTreeLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.newTreeLabel.sizePolicy().hasHeightForWidth())
        self.newTreeLabel.setSizePolicy(sizePolicy1)

        self.textVLayout.addWidget(self.newTreeLabel)

        self.wetFactorLabel = QLabel(SettingsDialog)
        self.wetFactorLabel.setObjectName(u"wetFactorLabel")

        self.textVLayout.addWidget(self.wetFactorLabel)


        self.mainHLayout.addLayout(self.textVLayout)


        self.verticalLayout_3.addLayout(self.mainHLayout)

        self.buttonBox = QDialogButtonBox(SettingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.NoButton)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.treeFactorBox.setSuffix(QCoreApplication.translate("SettingsDialog", u"%", None))
        self.treeFactorBox.setPrefix("")
        self.randomFireBox.setSuffix(QCoreApplication.translate("SettingsDialog", u"%", None))
        self.newTreeBox.setSuffix(QCoreApplication.translate("SettingsDialog", u"%", None))
        self.wetFactorBox.setSuffix(QCoreApplication.translate("SettingsDialog", u"%", None))
        self.treeFactorLabel.setText(QCoreApplication.translate("SettingsDialog", u"\u043f\u0440\u043e\u0446\u0435\u043d\u0442 \u043f\u043b\u043e\u0449\u0430\u0434\u0438 \u043f\u043e\u043b\u044f, \u0437\u0430\u043d\u0438\u043c\u0430\u0435\u043c\u043e\u0439 \u0434\u0435\u0440\u0435\u0432\u044c\u044f\u043c\u0438", None))
        self.randomFireLabel.setText(QCoreApplication.translate("SettingsDialog", u"\u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u043e\u0433\u043e \u0432\u043e\u0437\u0433\u043e\u0440\u0430\u043d\u0438\u044f \u0434\u0435\u0440\u0435\u0432\u0430", None))
        self.newTreeLabel.setText(QCoreApplication.translate("SettingsDialog", u"\u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043f\u043e\u044f\u0432\u043b\u0435\u043d\u0438\u044f \u043d\u043e\u0432\u043e\u0433\u043e \u0434\u0435\u0440\u0435\u0432\u0430 \u043d\u0430 \u043f\u043e\u043b\u0435", None))
        self.wetFactorLabel.setText(QCoreApplication.translate("SettingsDialog", u"\u0432\u043b\u0430\u0436\u043d\u043e\u0441\u0442\u044c", None))
    # retranslateUi

