#include "mbed.h"
#include "USBSerial.h"


Serial pcDebug(USBTX,USBRX);
USBSerial usbSerial;


// main() runs in its own thread in the OS
int main()
{
    while (true) {
     pcDebug.printf("Im SPLink Serial Console \r\n");
     usbSerial.printf("Im virtual usb Serial port \r\n");
    
    }
}


