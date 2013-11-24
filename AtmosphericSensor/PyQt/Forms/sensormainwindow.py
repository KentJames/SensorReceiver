# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensormainwindow.ui'
#
# Created: Sun Apr 28 11:38:44 2013
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
        SensorMainWindow.resize(221, 231)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SensorMainWindow.sizePolicy().hasHeightForWidth())
        SensorMainWindow.setSizePolicy(sizePolicy)
        SensorMainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralWidget = QtGui.QWidget(SensorMainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.detectedsensors = QtGui.QComboBox(self.centralWidget)
        self.detectedsensors.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.detectedsensors.setObjectName(_fromUtf8("detectedsensors"))
        self.tempNumber = QtGui.QLCDNumber(self.centralWidget)
        self.tempNumber.setGeometry(QtCore.QRect(120, 90, 91, 51))
        self.tempNumber.setDigitCount(3)
        self.tempNumber.setProperty("value", 0.0)
        self.tempNumber.setObjectName(_fromUtf8("tempNumber"))
        self.humidityNumber = QtGui.QLCDNumber(self.centralWidget)
        self.humidityNumber.setGeometry(QtCore.QRect(120, 150, 91, 51))
        self.humidityNumber.setDigitCount(3)
        self.humidityNumber.setObjectName(_fromUtf8("humidityNumber"))
        self.temperaturelabel = QtGui.QLabel(self.centralWidget)
        self.temperaturelabel.setGeometry(QtCore.QRect(10, 100, 101, 31))
        self.temperaturelabel.setScaledContents(False)
        self.temperaturelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.temperaturelabel.setWordWrap(False)
        self.temperaturelabel.setObjectName(_fromUtf8("temperaturelabel"))
        self.humiditylabel = QtGui.QLabel(self.centralWidget)
        self.humiditylabel.setGeometry(QtCore.QRect(10, 150, 101, 51))
        self.humiditylabel.setAlignment(QtCore.Qt.AlignCenter)
        self.humiditylabel.setObjectName(_fromUtf8("humiditylabel"))
        self.serialports = QtGui.QComboBox(self.centralWidget)
        self.serialports.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.serialports.setObjectName(_fromUtf8("serialports"))
        self.connectbutton = QtGui.QPushButton(self.centralWidget)
        self.connectbutton.setGeometry(QtCore.QRect(110, 10, 51, 31))
        self.connectbutton.setObjectName(_fromUtf8("connectbutton"))
        self.scanbutton = QtGui.QPushButton(self.centralWidget)
        self.scanbutton.setGeometry(QtCore.QRect(160, 10, 51, 31))
        self.scanbutton.setObjectName(_fromUtf8("scanbutton"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 50, 81, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        SensorMainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(SensorMainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 221, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuSensor = QtGui.QMenu(self.menuBar)
        self.menuSensor.setObjectName(_fromUtf8("menuSensor"))
        SensorMainWindow.setMenuBar(self.menuBar)
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
        self.menuSensor.addAction(self.actionAbout)
        self.menuSensor.addAction(self.actionExit)
        self.menuBar.addAction(self.menuSensor.menuAction())

        self.retranslateUi(SensorMainWindow)
        QtCore.QMetaObject.connectSlotsByName(SensorMainWindow)

    def retranslateUi(self, SensorMainWindow):
        SensorMainWindow.setWindowTitle(_translate("SensorMainWindow", "SensorMainWindow", None))
        self.temperaturelabel.setText(_translate("SensorMainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Temperature</span></p></body></html>", None))
        self.humiditylabel.setText(_translate("SensorMainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Humidity</span></p></body></html>", None))
        self.connectbutton.setText(_translate("SensorMainWindow", "Connect", None))
        self.scanbutton.setText(_translate("SensorMainWindow", "Rescan", None))
        self.pushButton.setText(_translate("SensorMainWindow", "Refresh", None))
        self.menuSensor.setTitle(_translate("SensorMainWindow", "Sensor", None))
        self.actionTerminal_View.setText(_translate("SensorMainWindow", "Terminal View", None))
        self.actionExit.setText(_translate("SensorMainWindow", "Exit", None))
        self.actionAbout.setText(_translate("SensorMainWindow", "About", None))
        self.actionSerial_Port.setText(_translate("SensorMainWindow", "Serial Port", None))
        self.actionTest.setText(_translate("SensorMainWindow", "Test", None))

