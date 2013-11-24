import platform, os, serial


class detectports(object):

    def __init__(self):

        self.operatingsystem = platform.system()
        self.serialtest = None

        self.i = None
        

        self.availableports = self.detectserialports()

    def __str__(self):

        try:

            return repr(self.availableports)

        except TypeError:

            return 'No COM ports detected'

           



    def detectserialports(self):

        self.available= []

            #Manually scan all serial ports.
        if self.operatingsystem == 'Windows': 

            # Brute force detection, thanks gates.


            for self.i in range(256):
                try:

                    self.serialtest = serial.Serial(self.i)
                    self.available.append((self.serialtest.portstr))
                    self.serialtest.close()

                except serial.SerialException:
                    pass

            return self.available
        else:
            #Assume linux/etc
            pass
    def returnavailableserialports(self):

        self.availableports = tuple(self.availableports)

        return self.availableports
       