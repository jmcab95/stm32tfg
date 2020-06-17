#include "mbed.h"
#include "USBSerial.h"
#include "drivers/USBHID.h"


//Declare Serial Uart

Serial pcDebug(USBTX,USBRX);
//Declare USBSerial Device
USBSerial usbSerial;

char name = 'H';




// main() runs in its own thread in the OS
int main()
{
     while(1){
        if (usbSerial.readable()!=0){
                 pcDebug.putc(usbSerial.getc());
        }else{
            usbSerial.putc(name);
        }
     }
}