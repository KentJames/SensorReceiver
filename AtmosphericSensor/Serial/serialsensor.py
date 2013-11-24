import sys
import serial
import queue
import threading
import time
from . import interface
from .. import base_exception







class serialiface(interface.iface):

    def __init__(self,PORT, BAUD = 9600, timeout = 5):

        

        self.PORT = PORT
        print(self.PORT)
        self.BAUD = BAUD
        self.timeout = 1

        self.serialinterface = None

        

        self.openinterface()





    def openinterface(self):

        try:

            print("Attempting to connect to serial port: ",self.PORT)
            self.serialinterface = serial.Serial(self.PORT, self.BAUD, 8, timeout = self.timeout)
            print("Interface opened successfully!")

        except serial.SerialException:

            raise interface.InterfaceNotConnected("serialiface.open")
    

    def closeport(self):
        
        if self.serialinterface is not None:

            self.serialinterface.close()

        self.serialinterface = None
        return True

        

    def writetoport(self):
        #Should probably implement this.
        pass

    def readlinefromport(self):
        
        self.line = self.serialinterface.readline()
        return self.line

    def readtestline(self):

        self.line = "011 20 80 \n"
        return self.line

    def readfromport(self, size):

        self.line = self.serialinterface.read(size)
        return self.line