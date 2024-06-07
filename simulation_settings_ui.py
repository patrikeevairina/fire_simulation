# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulation_settings.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(529, 191)
        Dialog.setStyleSheet(u"QDialog {border:1px solid black}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
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
        self.label.setFrameShadow(QFrame.Shadow.Plain)
        self.label.setLineWidth(3)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.closePBtn = QPushButton(Dialog)
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

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.timerLbl = QLabel(Dialog)
        self.timerLbl.setObjectName(u"timerLbl")

        self.gridLayout.addWidget(self.timerLbl, 0, 1, 1, 1)

        self.fieldSizeLbl = QLabel(Dialog)
        self.fieldSizeLbl.setObjectName(u"fieldSizeLbl")

        self.gridLayout.addWidget(self.fieldSizeLbl, 1, 1, 1, 1)

        self.cellSBox = QSpinBox(Dialog)
        self.cellSBox.setObjectName(u"cellSBox")
        self.cellSBox.setMinimum(5)
        self.cellSBox.setMaximum(100)
        self.cellSBox.setSingleStep(5)
        self.cellSBox.setValue(50)

        self.gridLayout.addWidget(self.cellSBox, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widthSBox = QSpinBox(Dialog)
        self.widthSBox.setObjectName(u"widthSBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widthSBox.sizePolicy().hasHeightForWidth())
        self.widthSBox.setSizePolicy(sizePolicy1)
        self.widthSBox.setMinimum(1)
        self.widthSBox.setMaximum(600)
        self.widthSBox.setSingleStep(10)
        self.widthSBox.setValue(30)

        self.horizontalLayout_2.addWidget(self.widthSBox)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.heightSBox = QSpinBox(Dialog)
        self.heightSBox.setObjectName(u"heightSBox")
        self.heightSBox.setWrapping(False)
        self.heightSBox.setMinimum(1)
        self.heightSBox.setMaximum(600)
        self.heightSBox.setSingleStep(10)
        self.heightSBox.setValue(15)

        self.horizontalLayout_2.addWidget(self.heightSBox)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.timerSBox = QSpinBox(Dialog)
        self.timerSBox.setObjectName(u"timerSBox")
        self.timerSBox.setMaximum(5000)
        self.timerSBox.setSingleStep(50)
        self.timerSBox.setValue(200)

        self.gridLayout.addWidget(self.timerSBox, 0, 0, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)

        self.cleanSimulationCBox = QCheckBox(Dialog)
        self.cleanSimulationCBox.setObjectName(u"cleanSimulationCBox")

        self.gridLayout.addWidget(self.cleanSimulationCBox, 3, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0438\u043c\u0443\u043b\u044f\u0446\u0438\u0438", None))
        self.closePBtn.setText("")
        self.timerLbl.setText(QCoreApplication.translate("Dialog", u"\u043f\u0435\u0440\u0438\u043e\u0434 \u0441\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u043d\u0438\u044f \u0442\u0430\u0439\u043c\u0435\u0440\u0430", None))
        self.fieldSizeLbl.setText(QCoreApplication.translate("Dialog", u"\u0440\u0430\u0437\u043c\u0435\u0440 \u043f\u043e\u043b\u044f \u0432 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430\u0445 (\u043d\u0435 \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u0442\u0441\u044f \u043f\u0440\u0435\u0432\u044b\u0448\u0430\u0442\u044c 20 \u0442\u044b\u0441.)", None))
        self.cellSBox.setSuffix(QCoreApplication.translate("Dialog", u" px", None))
        self.cellSBox.setPrefix("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0445", None))
        self.timerSBox.setSuffix(QCoreApplication.translate("Dialog", u" \u043c\u0441", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u043f\u0440\u0438\u043c\u0435\u0440\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430", None))
        self.cleanSimulationCBox.setText(QCoreApplication.translate("Dialog", u"\u0427\u0438\u0441\u0442\u0430\u044f \u0441\u0438\u043c\u0443\u043b\u044f\u0446\u0438\u044f", None))
#if QT_CONFIG(accessibility)
        self.buttonBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.buttonBox.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
    # retranslateUi

