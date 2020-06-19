import serial
import os 

ser = serial.Serial('/dev/ttyACM1')

sof = '\n'
eof= '\t'
while True:
    ser.write(b'HelloWorld')

    if(ser.readable):
        #print(ser.read())
