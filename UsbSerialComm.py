import serial
import os 

ser = serial.Serial('/dev/ttyACM1')


while True:
    ser.write(b'HelloWorld')

    if(ser.readable):
        print(ser.read())
