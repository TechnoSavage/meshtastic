""" text """


import meshtastic
import meshtastic.serial_interface

class meshtasticConn(object):
    """Object class for communication channel on a Meshtastic mesh.

    :param port: A string, serial interface connected to meshtastic radio."""

    def __init__(self, port):
        self._port = meshtastic.serial_interface.SerialInterface(port)
        self.config = self.localConfig()

    def changePort(self, port):
        """Change the port serial interface used to connect to meshastic radio.
        
        :param port: A string, serial interface connected to meshtastic radio."""

        self._port = meshtastic.serial_interface.SerialInterface(port)

    def localConfig(self):
        """Fetch local configuration of Meshtastic radio.
        
        :returns: A string, configuration of radio."""

        conf = self._port.getNode('^local')
        self.config = conf.localConfig
        return conf.localConfig
    
    def sendMessage(self, message):
        """Send provided message to Mesh.
        
        :param message: A string, message to send to mesh."""

        self._port.sendText(message)
