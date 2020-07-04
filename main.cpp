#include "USBSerial.h"
#include "drivers/USBHID.h"
#include "mbed.h"
#include "nanopb_library/TransmissionMessages.pb.h"
#include "nanopb_library/pb_common.h"
#include "nanopb_library/pb_decode.h"
#include "nanopb_library/pb_encode.h"
#include "platform/mbed_assert.h"
#include "platform/mbed_debug.h"
#include "platform/mbed_error.h"
#include "platform/mbed_stats.h"

// Functions
int state_machine();
int pb_decode_machine(int c);
int pb_encode_machine(int c);

// Interfaces
Serial serialConn(USBTX, USBRX);
USBSerial usbSerial;

//Protobuffers messages
IOControl ioControl;
Stats statsMessage;

//Variables
mbed_stats_sys_t statsSys;
pb_istream_t streamIn;
pb_ostream_t streamOut;
uint8_t buf[256];
size_t message_length;
DigitalOut digitalLed(LED1);
int version_os;
char temp;
bool statusPb;
char SOH = 0xaa;
char initialFlag = 0xab;
char finalEOF = 0xac;
int messageType;
int countMess = 0;
int state = 0;
int counter;
// main() runs in its own thread in the OS
int main() {

  while (1) {
    state_machine();
  }
}

int state_machine() {

  switch (state) {
  case 0:
    if (usbSerial.readable())
      state = 1;
    else
      state = 0;
    break;
  case 1:
    if (usbSerial.getc() == SOH) {
      state = 2;
    } else
      state = 0;
    break;
  case 2:
    if (usbSerial.getc() == initialFlag) {
      state = 3;
    } else
      state = 0;
    break;
  case 3:
    state = 4;
    message_length = usbSerial.getc();
    break;
  case 4:
    state = 5;
    messageType = int(usbSerial.getc());
    break;

  case 5:
    while (((temp = usbSerial.getc()) != finalEOF) and
           countMess < message_length) {
      buf[countMess] = temp;
      countMess++;
    }
    countMess = 0;
    state = 6;
    break;
  case 6:
    pb_decode_machine(messageType);
    state = 7;
    break;
  case 7:
    pb_encode_machine(messageType);
    state = 0;
    break;
  }
  return 1;
}

int pb_decode_machine(int c) { // deserialize
  switch (c) {
  case 1:
    streamIn = pb_istream_from_buffer(buf, message_length);
    statusPb = pb_decode(&streamIn, IOControl_fields, &ioControl);

    if (!statusPb) {
      serialConn.printf("Decoding failed %s\n", PB_GET_ERROR(&streamIn));
      ioControl.checkResponse = IOControl_CheckResponse_NONSUCCESSFULLY;
    }


    if (ioControl.typeOfControl == 1) {
      ioControl.checkResponse = IOControl_CheckResponse_SUCCESSFULLY;
    } else if (ioControl.typeOfControl == 2) {
      serialConn.printf("Enciendo Led/Apago Led");
      if (digitalLed.read() == 0)
        digitalLed.write(1);
      else
        digitalLed.write(0);
      ioControl.checkResponse = IOControl_CheckResponse_SUCCESSFULLY;
    } else if (ioControl.typeOfControl == 3) {
      serialConn.printf("Lectura entrada analógica");
      ioControl.checkResponse = IOControl_CheckResponse_SUCCESSFULLY;
    } else if (ioControl.typeOfControl == 4) {
      serialConn.printf("Lectura entrada digital");
      ioControl.digitalPin= digitalLed.read();
      ioControl.checkResponse = IOControl_CheckResponse_SUCCESSFULLY;
    }
    

    break;

  case 2:
    streamIn = pb_istream_from_buffer(buf, message_length);
    statusPb = pb_decode(&streamIn, Stats_fields, &statsMessage);

    if (!statusPb) {
      serialConn.printf("Decoding failed %s\n", PB_GET_ERROR(&streamIn));
    }
    
    mbed_stats_sys_get(&statsSys);
    
    statsMessage.cpuId = statsSys.compiler_id;
    statsMessage.mbedVersion=statsSys.os_version;
    break;
  }
  return 1;
}

int pb_encode_machine(int c) { // serialize
  switch (c) {
  case 1:
    message_length = sizeof(ioControl);
    streamOut = pb_ostream_from_buffer(buf, message_length);

    statusPb =
        pb_encode(&streamOut, IOControl_fields, &ioControl);
    message_length = streamOut.bytes_written;

    if (!statusPb) {
      serialConn.printf("Encoding failed %s\n", PB_GET_ERROR(&streamOut));
    } else {
      usbSerial.putc(SOH);
      usbSerial.putc(initialFlag);
      usbSerial.putc(message_length);
      for (countMess = 0; countMess < message_length; countMess++) {
        usbSerial.putc(buf[countMess]);
      }
      usbSerial.putc(finalEOF);
    }

    countMess = 0;
    break;
  
  case 2:
    message_length = sizeof(statsMessage);
    streamOut = pb_ostream_from_buffer(buf, message_length);

    statusPb =
        pb_encode(&streamOut, Stats_fields, &statsMessage);
    message_length = streamOut.bytes_written;

    if (!statusPb) {
      serialConn.printf("Encoding failed %s\n", PB_GET_ERROR(&streamOut));
    } else {
      usbSerial.putc(SOH);
      usbSerial.putc(initialFlag);
      usbSerial.putc(message_length);
      for (countMess = 0; countMess < message_length; countMess++) {
        usbSerial.putc(buf[countMess]);
      }
      usbSerial.putc(finalEOF);
    }

    countMess = 0;
    break;
  }
  return 1;
}
