#include "mbed.h"
#include "USBSerial.h"
#include "drivers/USBHID.h"
#include "nanopb_library/pb_common.h"
#include "nanopb_library/pb_decode.h"
#include "nanopb_library/pb_encode.h"
#include "nanopb_library/messages.pb.h"



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
            switch(usbSerial.getc()){


                // pcDebug.putc(usbSerial.getc());
        }
            //usbSerial.putc(name);
        
        
        


        }



     }
}