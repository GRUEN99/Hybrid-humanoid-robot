import serial
import time

class SerialCommunication:
    def __init__(self):
        self.serial_port = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.serial_port.reset_input_buffer()
        #return self.serial_port
    def write(self , data):
        self.serial_port.write(data)
        
    