import sys
import abc
from .. import base_exception

class InterfaceException(base_exception.SensorException):
    pass


class InterfaceNotConnected(InterfaceException):
    pass



'''

Defines an abstract method, which allows people to build up an interface for a serial device.

'''


class iface(metaclass = abc.ABCMeta):

    

    @abc.abstractmethod
    def openinterface(self):
        pass

    @abc.abstractmethod
    def readfromport(self, size):
        pass
    
    @abc.abstractmethod 
    def readlinefromport(self):
        pass   

    @abc.abstractmethod
    def closeport(self):
        pass

    @abc.abstractmethod
    def writetoport(self,data):
        pass