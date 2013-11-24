import sys, os


from PyQt4 import QtCore, QtGui
from .. import base_exception
from .Forms import sensormainwindow
from ..Serial import detectserialports, serialsensor, interface

import queue, threading, time


 

class PyQtException(base_exception.SensorException):

    pass


class StartQT4(QtGui.QMainWindow):

    def __init__(self, parent = None):

        QtGui.QWidget.__init__(self, parent)

        self.mainwindow = sensormainwindow.Ui_SensorMainWindow()
        self.mainwindow.setupUi(self)

        self.serialiface = None


        self.datareceived = None
        

        self.serialdetect()



        ######## Connect slots #########

        # Pushbuttons:

        QtCore.QObject.connect(self.mainwindow.connectbutton,QtCore.SIGNAL("clicked()"),self.connectserialinterface)
        QtCore.QObject.connect(self.mainwindow.scanbutton,QtCore.SIGNAL("clicked()"),self.serialdetect)
        QtCore.QObject.connect(self.mainwindow.pushButton,QtCore.SIGNAL("clicked()"),self.refreshdisplay)

        # Combobox:

        QtCore.QObject.connect(self.mainwindow.detectedsensors,QtCore.SIGNAL("currentIndexChanged()"),self.setsensor)

        # Menus:

        QtCore.QObject.connect(self.mainwindow.actionExit,QtCore.SIGNAL("triggered()"), self.exit)
        QtCore.QObject.connect(self.mainwindow.actionAbout,QtCore.SIGNAL("triggered()"),self.showabout)


        ##Test stuff:

        self.writehumidity(0)
        self.writetemperature(0)

        self.testdata()

        

    def serialdetect(self):

        self.serialiface = None

        self.mainwindow.detectedsensors.clear()

        self.mainwindow.serialports.clear()

        self.availableserialports = None
        self.ports = None

        self.availableserialports = detectserialports.detectports()
        self.ports = self.availableserialports.returnavailableserialports()

        

        for i in range(len(self.ports)):

            self.mainwindow.serialports.addItem(self.ports[i])
            
    def connectserialinterface(self):

        try:

            self.serialiface = serialsensor.serialiface(self.mainwindow.serialports.currentText(),9600,1) 
            self.mainwindow.detectedsensors.addItem(self.mainwindow.serialports.currentText())    

        except interface.InterfaceNotConnected:

            self.serialiface.closeport()
            self.serialiface = serialsensor.serialiface(self.mainwindow.serialports.currentText(),9600,1)
            


    def setsensor(self):

        pass

    def refreshdisplay(self):
    
        try:
            self.datareceived = self.serialiface.readlinefromport()
            self.sortdata(self.datareceived)

        except AttributeError:

            print("No Serial Port Connected.")


    def sortdata(self, datareceived):

        self.dataval = datareceived
        print(self.dataval)
        self.dataval = self.dataval.decode("utf-8")
        self.words = self.dataval.split()
        print(self.words)

        try:

            if (self.words[0] == "011"):

                self.writetemperature(self.words[1])
                self.writehumidity(self.words[2])
            
            else:
        
                self.refreshdisplay()

        except IndexError:

            #self.refreshdisplay()
            pass
            
        


    # Self test routine for interpreting ascii data

    def testdata(self):

        self.testdataval = "011 24 45 \\n"
        self.testwords = self.testdataval.split()
        
      #  for i in self.testwords:
      #      i.decode("utf-8")

        print(self.testwords)

        try:
            
            if (self.testwords[0] == "011") and (self.testwords[0] == "\\n"):

                self.writetemperature(self.testwords[1])
                self.writehumidity(self.testwords[2])

        except IndexError:

            pass

    def writetemperature(self, string):

        self.mainwindow.tempNumber.display(int(string))

    def writehumidity(self,string):
        
        self.mainwindow.humidityNumber.display(int(string))

    def showabout(self):

        pass

    def exit(self):

        sys.exit(0)






    

            

            

