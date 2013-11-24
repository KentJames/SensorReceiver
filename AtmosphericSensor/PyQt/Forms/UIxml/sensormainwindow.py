# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensormainwindow.ui'
#
# Created: Mon Feb 11 17:23:18 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SensorMainWindow(object):
    def setupUi(self, SensorMainWindow):
        SensorMainWindow.setObjectName(_fromUtf8("SensorMainWindow"))
        SensorMainWindow.resize(221, 297)
        self.centralWidget = QtGui.QWidget(SensorMainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.comboBox = QtGui.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.pressureNumber = QtGui.QLCDNumber(self.centralWidget)
        self.pressureNumber.setGeometry(QtCore.QRect(120, 120, 91, 51))
        self.pressureNumber.setDigitCount(3)
        self.pressureNumber.setObjectName(_fromUtf8("pressureNumber"))
        self.tempNumber = QtGui.QLCDNumber(self.centralWidget)
        self.tempNumber.setGeometry(QtCore.QRect(120, 60, 91, 51))
        self.tempNumber.setDigitCount(3)
        self.tempNumber.setProperty("value", 0.0)
        self.tempNumber.setObjectName(_fromUtf8("tempNumber"))
        self.humidityNumber = QtGui.QLCDNumber(self.centralWidget)
        self.humidityNumber.setGeometry(QtCore.QRect(120, 180, 91, 51))
        self.humidityNumber.setDigitCount(3)
        self.humidityNumber.setObjectName(_fromUtf8("humidityNumber"))
        self.templabel = QtGui.QLabel(self.centralWidget)
        self.templabel.setGeometry(QtCore.QRect(10, 60, 101, 31))
        self.templabel.setScaledContents(False)
        self.templabel.setAlignment(QtCore.Qt.AlignCenter)
        self.templabel.setWordWrap(False)
        self.templabel.setObjectName(_fromUtf8("templabel"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 120, 101, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 101, 51))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        SensorMainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(SensorMainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 221, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuSensor = QtGui.QMenu(self.menuBar)
        self.menuSensor.setObjectName(_fromUtf8("menuSensor"))
        self.menuDebug = QtGui.QMenu(self.menuSensor)
        self.menuDebug.setObjectName(_fromUtf8("menuDebug"))
        self.menuConnect = QtGui.QMenu(self.menuSensor)
        self.menuConnect.setObjectName(_fromUtf8("menuConnect"))
        SensorMainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(SensorMainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        SensorMainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(SensorMainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        SensorMainWindow.setStatusBar(self.statusBar)
        self.actionTerminal_View = QtGui.QAction(SensorMainWindow)
        self.actionTerminal_View.setObjectName(_fromUtf8("actionTerminal_View"))
        self.actionExit = QtGui.QAction(SensorMainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(SensorMainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionSerial_Port = QtGui.QAction(SensorMainWindow)
        self.actionSerial_Port.setObjectName(_fromUtf8("actionSerial_Port"))
        self.actionTest = QtGui.QAction(SensorMainWindow)
        self.actionTest.setObjectName(_fromUtf8("actionTest"))
        self.menuDebug.addAction(self.actionTerminal_View)
        self.menuConnect.addAction(self.actionTest)
        self.menuSensor.addAction(self.menuConnect.menuAction())
        self.menuSensor.addAction(self.menuDebug.menuAction())
        self.menuSensor.addSeparator()
        self.menuSensor.addAction(self.actionAbout)
        self.menuSensor.addAction(self.actionExit)
        self.menuBar.addAction(self.menuSensor.menuAction())

        self.retranslateUi(SensorMainWindow)
        QtCore.QMetaObject.connectSlotsByName(SensorMainWindow)

    def retranslateUi(self, SensorMainWindow):
        SensorMainWindow.setWindowTitle(_translate("SensorMainWindow", "SensorMainWindow", None))
        self.templabel.setText(_translate("SensorMainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Temperature</span></p></body></html>", None))
        self.label.setText(_translate("SensorMainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Pressure</span></p></body></html>", None))
        self.label_2.setText(_translate("SensorMainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Humidity</span></p></body></html>", None))
        self.menuSensor.setTitle(_translate("SensorMainWindow", "Sensor", None))
        self.menuDebug.setTitle(_translate("SensorMainWindow", "Debug", None))
        self.menuConnect.setTitle(_translate("SensorMainWindow", "Connect", None))
        self.actionTerminal_View.setText(_translate("SensorMainWindow", "Terminal View", None))
        self.actionExit.setText(_translate("SensorMainWindow", "Exit", None))
        self.actionAbout.setText(_translate("SensorMainWindow", "About", None))
        self.actionSerial_Port.setText(_translate("SensorMainWindow", "Serial Port", None))
        self.actionTest.setText(_translate("SensorMainWindow", "Test", None))

