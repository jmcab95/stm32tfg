import serial
import os
import sys

from protobuf import TransmissionMessages_pb2
from time import sleep


def MessageTypeControl():
    inputTypeControl = input(
        "Choose the kind of message you want to generate ( IOCOntrol , Stats )\n")
    messageType = 0
    if inputTypeControl.lower() == "iocontrol":
        messageType = 1
    elif inputTypeControl.lower() == "stats":
        messageType = 2

    return messageType


def SerialConn():
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = '/dev/ttyACM1'

    try:
        ser.open()
        print("Connected to serial port :",ser.port)
        return ser
    except serial.SerialException:
        print("Trying to reconnect")
        sleep(1)
        SerialConn()


def GenerateProtobufferMessage(messageTypeControl):

    message = TransmissionMessages_pb2
    if messageTypeControl == 1:
        message = message.IOControl()
        election = int(input(
            "Choose an option:\n 1 - Analog write \n 2 - Digital write \n 3 - Analog read \n 4 - Digital read \n"))
        if election == 1:
            message.typeOfControl = message.TypeOfControl.ANALOGWRITE
            message.analogPin = 1
        elif election == 2:
            message.typeOfControl = message.TypeOfControl.DIGITALWRITE
            message.digitalPin = 1
        elif election == 3:
            message.typeOfControl = message.TypeOfControl.ANALOGREAD
            message.analogPin = 1
        elif election == 4:
            message.typeOfControl = message.TypeOfControl.DIGITALREAD
            message.digitalPin = 1

    elif messageTypeControl == 2:
        message = message.Stats()
        message.value = int(input("Insert a numeric ID: \n"))
        message.mbedVersion =51510
        message.cpuId=584
    return message

def PrintProtobufferMessage(messageTypeControl,generatedMessage):
    if messageTypeControl == 1:
        print("-IOControl-")
        print("Digital Pin: ", generatedMessage.digitalPin)
        print("Analog Pin: ",generatedMessage.analogPin)
        enumValue = ""
        if(generatedMessage.typeOfControl == 1):
            enumValue ="Message type : Analog Write"
        elif(generatedMessage.typeOfControl == 2):
            enumValue ="Message type : Digital Write"
        elif(generatedMessage.typeOfControl == 3):
            enumValue ="Message type : Analog Read"
        elif(generatedMessage.typeOfControl == 4):
            enumValue ="Message type : Digital Read"
        print(enumValue)
        successValue=""
        if(generatedMessage.checkResponse == 0):
            successValue="Response from mbed: NON SUCCESS"
        elif(generatedMessage.checkResponse == 1):
            successValue="Response from mbed: SUCCESS"
        print(successValue)
        
    elif messageTypeControl == 2:
        print("-Mbed Stats-")
        print("Value: ",generatedMessage.value)
        print("Mbed Version: ",generatedMessage.mbedVersion)
        print("CPU ID: ",generatedMessage.cpuId)


conn = SerialConn()
flag = True
while flag:

    messageTypeControl = MessageTypeControl()
    generatedMessage = GenerateProtobufferMessage(messageTypeControl)
    flagSOH = 0xaa
    initFlag = 0xab
    flagEOF = 0xac

    messageBytes = generatedMessage.SerializeToString()
    flagSOHBytes = bytes([flagSOH])
    initFlagBytes = bytes([initFlag])
    flagEOFBytes = bytes([flagEOF])
    lengthBytes = bytes([len(messageBytes)])
    messageTypeControlBytes = bytes([messageTypeControl])
    # print(len(messageBytes))
    '''
    print(messageTypeControlBytes)
    print(generatedMessage.typeOfControl)
    print(generatedMessage.digitalPin)
    print(generatedMessage.analogPin)
    '''

    # print(generatedMessage.streamBytes)

    continueConn = 1
    buf = bytearray()

    i = 0

    print("Sending message...")
    conn.write(flagSOHBytes)
    conn.write(initFlagBytes)
    conn.write(lengthBytes)
    conn.write(messageTypeControlBytes)
    conn.write(messageBytes)
    conn.write(flagEOFBytes)
    sleep(1)
    print("\nMessage sent\n")

    if conn.readable():
        if conn.read() == b'\xaa':
            if conn.read() == b'\xab':
                lengthMessage = conn.read()
                temp = conn.read()
                while temp != b'\xac' and i < lengthMessage[0]:
                    buf += temp
                    i = i + 1
                    temp = conn.read()
                array = bytearray(buf)
                generatedMessage.ParseFromString(array)
                PrintProtobufferMessage(messageTypeControl,generatedMessage)

    whileContinue = input("\nDo you want to send another instruction: yes / no : \n").lower()
    if whileContinue == "yes":
        flag = True
    else:
        flag = False

print("\n---Cerrando consola---\n")
