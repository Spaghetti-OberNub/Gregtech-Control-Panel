# Form implementation generated from reading ui file 'c:\Users\Moritz\Desktop\Gregtech Control Panel\thorium_widget.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(245, 112)
        font = QtGui.QFont()
        font.setFamily("Arial")
        Form.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalWidget = QtWidgets.QWidget(parent=Form)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rod_name_label = QtWidgets.QLabel(parent=self.verticalWidget)
        self.rod_name_label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rod_name_label.setFont(font)
        self.rod_name_label.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.rod_name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.rod_name_label.setWordWrap(True)
        self.rod_name_label.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.rod_name_label.setObjectName("rod_name_label")
        self.verticalLayout.addWidget(self.rod_name_label)
        self.durability_label = QtWidgets.QLabel(parent=self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.durability_label.sizePolicy().hasHeightForWidth())
        self.durability_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.durability_label.setFont(font)
        self.durability_label.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.durability_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.durability_label.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.durability_label.setObjectName("durability_label")
        self.verticalLayout.addWidget(self.durability_label)
        self.damage_progress = QtWidgets.QProgressBar(parent=self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.damage_progress.sizePolicy().hasHeightForWidth())
        self.damage_progress.setSizePolicy(sizePolicy)
        self.damage_progress.setStyleSheet("QProgressBar {\n"
"    background-color: #1c1c1c;      /* dunkler Hintergrund, fast schwarz */\n"
"    border: 1px solid #000;\n"
"    height: 8px;\n"
"    text-align: center;\n"
"    color: transparent;             /* Text unsichtbar machen */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #00ff00;      /* Standard: grün */\n"
"    margin: 0px;\n"
"}")
        self.damage_progress.setProperty("value", 99)
        self.damage_progress.setTextVisible(False)
        self.damage_progress.setObjectName("damage_progress")
        self.verticalLayout.addWidget(self.damage_progress)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.gridLayout.addWidget(self.verticalWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.rod_name_label.setText(_translate("Form", "Fuel Rod #1"))
        self.durability_label.setText(_translate("Form", "Durability: 00%"))
