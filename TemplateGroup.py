# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/tmp/tmpkfNtfM.ui'
#
# Created: Wed Jun 11 09:30:53 2014
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

# IMPORT WIDGETS
#import IonPumpWidget
#import TspPumpWidget
#import ValveWidget
#import LRValveWidget
#import GaugeWidget
#import PLCGaugeWidget
#import MovableAbsorberWidget
import TemplateWidget

import threading

class Ui_MainWindow(object):
    titleFont = QtGui.QFont("Arial")
    descriptions = None
    childWidgets = None

    setModelMap = None

    def setupUi(self, MainWindow, gui_groups, additional):
        self.setModelMap = []
        self.descriptions = []
        self.childWidgets = []
        self.allGroupWidgets = []
        self.allGroupNames = sorted(gui_groups.keys())
        self.allGroupButtons = []
        self.MainWindow = MainWindow

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 405)
        self.titleFont.setBold(True)

        # LAYOUTS
        #
        # ------------------------
        self.horizontalLayout = QtGui.QHBoxLayout(MainWindow)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.mainLayout.setSpacing(4)

        # 1. Layout for PREV button
        self.prevLayout = QtGui.QVBoxLayout()
        self.horizontalLayout.addLayout(self.prevLayout)

        # 2. VLINE
        vline = QtGui.QFrame()
        vline.setFrameStyle(QtGui.QFrame.VLine)
        vline.setLineWidth(2)
        self.horizontalLayout.addWidget(vline)
        self.horizontalLayout.addSpacing(3)

        # 3. MAIN LAYOUT
        self.horizontalLayout.addLayout(self.mainLayout)

        # 4. VLINE
        self.horizontalLayout.addSpacing(3)
        vline = QtGui.QFrame()
        vline.setFrameStyle(QtGui.QFrame.VLine)
        vline.setLineWidth(2)
        self.horizontalLayout.addWidget(vline)

        # 5. Layout for PREV button
        self.nextLayout = QtGui.QVBoxLayout()
        self.horizontalLayout.addLayout(self.nextLayout)



        # GUI GROUPS
        #
        ############################
        for group_name in sorted(gui_groups.keys()):
            groupButton = QtGui.QPushButton()
            groupButton.setText(group_name.upper())
            groupButton.setStyleSheet("font-weight: bold;")
            groupButton.setMinimumWidth(200)
            self.allGroupButtons.append(groupButton)

            self.mainLayout.addWidget(groupButton)

            allGroupWidget = QtGui.QWidget()
            self.allGroupWidgets.append(allGroupWidget)
            index = len(self.allGroupWidgets)-1
            groupButton.clicked.connect((lambda i: lambda: self.showHideNamedGroups(i))(index))

            groupLayout = QtGui.QGridLayout(allGroupWidget)
            groupLayout.setSpacing(3)
            self.mainLayout.addWidget(allGroupWidget)

            if(len(gui_groups[group_name]) > 1):
                vline = QtGui.QFrame()
                vline.setFrameStyle(QtGui.QFrame.VLine)
                groupLayout.addWidget(vline, 0, 1, -1, 1)
                vline = QtGui.QFrame()
                vline.setFrameStyle(QtGui.QFrame.VLine)
                groupLayout.addWidget(vline, 0, 3, -1, 1)


            hline = QtGui.QFrame()
            hline.setFrameStyle(QtGui.QFrame.HLine)
            hline.setMaximumHeight(1)
            groupLayout.addWidget(hline, 0, 0, 1, -1)

            i = 1
            j = 0
            for k in range(len(gui_groups[group_name])):
                element = gui_groups[group_name][k][1:]
                elementId = gui_groups[group_name][k][0]
                elementWidget = QtGui.QWidget()

                if "IPC" in elementId:
                    #elementUi = IonPumpWidget.Ui_Form()
                    elementUi = TemplateWidget.Ui_Form()
                elif "VGC" in elementId:
                    #elementUi = GaugeWidget.Ui_Form()
                    elementUi = TemplateWidget.Ui_Form()
                elif "VGM" in elementId:
                    #elementUi = ValveWidget.Ui_Form()
                    elementUi = TemplateWidget.Ui_Form()
                elif "PLC_GAUGE" in elementId:
                    #elementUi = PLCGaugeWidget.Ui_Form()
                    elementUi = TemplateWidget.Ui_Form()
                elif "ABS" in elementId:
                    #elementUi = MovableAbsorberWidget.Ui_Form()
                    elementUi = TemplateWidget.Ui_Form()
                else:
                    continue

                elementUi.setupUi(elementWidget, element)
                self.childWidgets.append(elementUi)
                groupLayout.addWidget(elementWidget, i,j,1,1)
                j = j+2
                if j >= 6 and len(gui_groups[group_name]) > k+1:
                    hline = QtGui.QFrame()
                    hline.setFrameStyle(QtGui.QFrame.HLine)
                    hline.setMaximumHeight(1)
                    groupLayout.addWidget(hline, i+1, 0, 1, -1)
                    j = 0
                    i = i+2
            hline = QtGui.QFrame()
            hline.setFrameStyle(QtGui.QFrame.HLine)
            groupLayout.addWidget(hline, i+1, 0, 1, -1)





        # HANDLE ADDITIONAL INFO






        self.mainLayout.addStretch()



        self.actionShowDescY = QtGui.QAction(MainWindow)
        self.actionShowDescN = QtGui.QAction(MainWindow)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionShowDescY.setText("Show descriptions")
        self.actionShowDescN.setText("Hide descriptions")
        self.actionExit.setText("Close")
        self.actionShowDescY.triggered.connect(self.showDescriptions)
        self.actionShowDescN.triggered.connect(self.hideDescriptions)
        self.actionExit.triggered.connect(self.close)
        MainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        MainWindow.customContextMenuRequested.connect(self.showContextMenu)


        MainWindow.addNext = self.addNext
        MainWindow.addPrev = self.addPrev
        MainWindow.setManagerInstance = self.setManagerInstance


        # Worker set-model Thread
        MainWindow.finished.connect(self.closeHandler)
        self.setModelStop = threading.Event()
        self.setModelThread = threading.Thread(target=self.setModelRun)
        self.setModelThread.start()


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        pass



    # Helper function, tell ControlProgram to open Device Panel for proxy
    def openEngineeringScreen(self, proxy):
        if self.manager:
            try:
                index = self.manager.getCsvDevice(proxy).runGUI()
                if index == 0:
                    QtGui.QMessageBox.information(None, 'Info', "GUI for device " + proxy.upper() + " already running")
                elif index == -1:
                    QtGui.QMessageBox.question(None, 'Warning', "Device " + proxy.upper() + " not accessible!", QtGui.QMessageBox.Ok)
                elif index == -2:
                    QtGui.QMessageBox.question(None, 'Warning', "GUI script for device " + proxy.upper() + " not found!", QtGui.QMessageBox.Ok)
                elif index == -3:
                    QtGui.QMessageBox.question(None, 'Warning', "Error occurred whilst running GUI script for device " + proxy.upper(), QtGui.QMessageBox.Ok)
            except:
                QtGui.QMessageBox.warning(None, 'Warning', "Cannot open GUI for device: " + proxy.upper(), QtGui.QMessageBox.Ok)
        else:
            QtGui.QMessageBox.warning(None, 'Warning', "Cannot open GUI for device: " + proxy.upper(), QtGui.QMessageBox.Ok)


    # Called by ControlProgram
    def setManagerInstance(self, manager):
        self.manager = manager

    # Called by ControlProgram
    def addNext(self, callable, index, desc):
        nextButton = QtGui.QPushButton()
        nextButton.setText(u'\u25B6')
        nextButton.setFixedWidth(20)
        nextButton.setMaximumHeight(999)
        nextButton.setToolTip("Open " + desc + " section")
        nextButton.clicked.connect((lambda i: lambda: callable(i))(index))
        self.nextLayout.addWidget(nextButton)

    # Called by ControlProgram
    def addPrev(self, callable, index, desc):
        prevButton = QtGui.QPushButton()
        prevButton.setText(u'\u25C0')
        prevButton.setFixedWidth(20)
        prevButton.setMaximumHeight(999)
        prevButton.setToolTip("Open " + desc + " section")
        prevButton.clicked.connect((lambda i: lambda: callable(i))(index))
        self.prevLayout.addWidget(prevButton)


    def closeHandler(self):
        self.setModelStop.set()

    def setModelRun(self):
        for setModelEl in self.setModelMap:
            if(self.setModelStop.isSet()):
                return
            setModelEl[0].setModel(setModelEl[1])
        for widget in self.childWidgets:
            if(self.setModelStop.isSet()):
                return
            widget.setModel()


    def close(self):
        self.MainWindow.close()

    def showDescriptions(self):
        for desc in self.descriptions:
            desc.show()
        for widget in self.childWidgets:
            widget.showDescription(True)

    def hideDescriptions(self):
        for desc in self.descriptions:
            desc.hide()
        for widget in self.childWidgets:
            widget.showDescription(False)


    def showContextMenu(self, pos):
        pos = self.MainWindow.mapToGlobal(pos)
        menu = QtGui.QMenu(None)
        menu.addAction(self.actionShowDescY)
        menu.addAction(self.actionShowDescN)
        menu.addAction(self.actionExit)
        menu.exec_(pos)


    def showHideNamedGroups(self, index):
        if self.allGroupWidgets[index].isHidden():
            self.allGroupWidgets[index].show()
            self.allGroupButtons[index].setText(self.allGroupNames[index])
        else:
            self.allGroupWidgets[index].hide()
            self.allGroupButtons[index].setText(u'\u25BC' + "  " + self.allGroupNames[index] + "  " + u'\u25BC')



