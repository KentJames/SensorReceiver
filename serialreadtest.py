import os, sys
from AtmosphericSensor.Serial import detectserialports, serialsensor



def main():

    serialports = detectserialports.detectports()
    availableports = serialports.returnavailableserialports()

    serialinterface = serialsensor.serialiface(availableports[0])

    line = serialinterface.readlinefromport()

    while line != b'':

        line = serialinterface.readlinefromport()
        print(line)


if __name__=="__main__":
    main()