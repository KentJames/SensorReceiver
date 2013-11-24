import sys
from AtmosphericSensor.PyQt import sensorgui




def main():
    app = sensorgui.QtGui.QApplication(sys.argv)
    myapp = sensorgui.StartQT4()
    myapp.show()
    sys.exit(app.exec_())
    

if __name__=="__main__":
    main()



