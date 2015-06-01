# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/tmp/tmprZv_PC.ui'
#
# Created: Wed Jun 11 09:29:58 2014
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, Qt
import PyTango
from taurus.qt.qtgui.display import TaurusLabel, TaurusLed
from cosywidgets.input import OpenWidgetButton
from cosywidgets.input import CommandComboBox


class Ui_Form(object):
    def setupUi(self, Form, element):
        self.deviceProxy = element[0]
        description = element[1]

        Form.setObjectName("Form")
        Form.resize(260, 104)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setMargin(5)
        self.verticalLayout.setObjectName("verticalLayout")

        ########################
        # HORIZONTAL 1
        ########################
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Element Name -> OpenWidgetButton (Cosywidgets)
        self.ElementName = OpenWidgetButton(Form)
        self.ElementName.setText(self.deviceProxy.split("/")[2] + " ")
        self.horizontalLayout.addWidget(self.ElementName)

        # LED for state
        self.stateT = TaurusLed(Form)
        self.stateT.setFixedSize(QtCore.QSize(20, 20))
        self.stateT.setObjectName("stateT")
        self.horizontalLayout.addWidget(self.stateT)

        # Command combobox (Cosywidgets)
        self.comboBox = CommandComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setFixedHeight(20)
        self.horizontalLayout.addWidget(self.comboBox)
        self.comboBox.addItems(["Start", "Stop", "Init"])

        self.verticalLayout.addLayout(self.horizontalLayout)


        ########################
        # HORIZONTAL 2
        ########################
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # DESIRED ATTRIBUTE ...
        self.pressure = QtGui.QLabel(Form)
        self.pressure.setObjectName("pressure")
        self.horizontalLayout_2.addWidget(self.pressure)
        self.pressureT = TaurusLabel(Form)
        self.pressureT.setObjectName("pressureT")
        self.pressureT.setFixedWidth(180)
        self.horizontalLayout_2.addWidget(self.pressureT)
        self.pressureU = QtGui.QLabel(Form)
        self.pressureU.setText("mBar")
        self.horizontalLayout_2.addWidget(self.pressureU)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        ########################
        # HORIZONTAL 3
        ########################
        # ...


        ########################
        # DESCRIPTION
        ########################
        self.descLabel = QtGui.QLabel(u'\u2022' + " " + description)
        self.descLabel.setStyleSheet("background-color: lightblue; border: 1px solid grey;")
        self.descLabel.setToolTip(description)
        self.verticalLayout.addSpacing(2)
        self.verticalLayout.addWidget(self.descLabel)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pressure.setText(QtGui.QApplication.translate("Form", "Pressure:", None, QtGui.QApplication.UnicodeUTF8))

    # SHOW/HIDE DESCRIPTION
    def showDescription(self, show):
        if show:
            self.descLabel.show()
        else:
            self.descLabel.hide()

    # SEPARATE SET MODEL -> background thread
    def setModel(self):
        self.ElementName.setModel(self.deviceProxy)
        self.stateT.setModel(self.deviceProxy + "/State")
        self.comboBox.setModel(self.deviceProxy)
        self.pressureT.setModel(self.deviceProxy + "/pressure")
        try:
            self.pressureU.setText(PyTango.AttributeProxy(self.deviceProxy + "/pressure").get_config().unit)
        except PyTango.DevFailed:
            pass