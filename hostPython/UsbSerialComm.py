import serial
import os 
import sys

from protobuf import messagesPrueba_pb2
from time import sleep



def SerialConn():
    port = '/dev/ttyACM1'
    baudrate = 9600
    try:
        ser = serial.Serial(port,baudrate)
        print('Conexión establecida')
    except serial.SerialException:
        ser.close()
        ser.open()
        print('Conexión establecida')
    
    return ser

def ConsoleFill(messages):
    
    messages.digitalPin = int(input('Introduce un entero: (Digital Input)'))
    messages.analogPin = int(input('Introduce otro entero (Analog Input): '))
    messages.codigo = int(input('Introduce un codigo entero(Codigo): '))
    value = input('Selecciona un valor... house, web, number, video: ')

    if value == 'house':
        messages.new_values = messagesPrueba_pb2.MensajePruebasPySTM.NewValues.HOUSE
    elif value == 'web':
        messages.new_values = messagesPrueba_pb2.MensajePruebasPySTM.NewValues.WEB
    elif value == 'number':
        messages.new_values = messagesPrueba_pb2.MensajePruebasPySTM.NewValues.NUMBER
    elif value == 'video':
        messages.new_values = messagesPrueba_pb2.MensajePruebasPySTM.NewValues.VIDEO
    else:
        messages.new_values = messagesPrueba_pb2.MensajePruebasPySTM.NewValues.DEFAULT

    
#port= '/dev/ttyACM1'

messages = messagesPrueba_pb2.MensajePruebasPySTM()

messages.digitalPin=564
messages.analogPin = 987
messages.codigo=125
messages.new_values = messagesPrueba_pb2.MensajePruebasPySTM.NewValues.WEB

#ConsoleFill(messages)
flag = 0xaa
final= 0xba

message_bytes = messages.SerializeToString()
flag_bytes=bytes([flag])
final_flag_bytes=bytes([final])
length_bytes=bytes([len(message_bytes)])

conn = SerialConn()

buf=bytearray()
while True:
    i = 0;
    if conn.readable():
        if conn.read() == b'\xaa':
            if conn.read() == b'\xaa':
                length_message = conn.read()
                temp = conn.read()
                while temp!= b'\xba' and i<length_message[0] :
                    buf+=temp
                    i = i + 1
                    temp = conn.read()                    
                array = bytearray(buf)
                messages.ParseFromString(array)
                print(messages.codigo)
    else:
        print("Enviamos mensajes")
        print("Mandamos cabeceras")
        conn.write(flag_bytes)
        print("Mandamos cabeceras 2")
        conn.write(flag_bytes)
        print("Mandamos longitud")
        conn.write(length_bytes)
        print("Mandamos mensaje")
        conn.write(message_bytes)
        print("Mandamos cabecera final")
        conn.write(final_flag_bytes)