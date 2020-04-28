#include "mbed.h"
#include "USBSerial.h"
#include "drivers/USBHID.h"


//Declare Serial Uart
Serial pcDebug(USBTX,USBRX);
//Declare USBSerial Device
//USBSerial usbSerial;
//Declare USBHID device con el tamaño de input y output 8 bytes 

USBHID hid(8, 8);

//Declaro estructuras de entrada y salida
HID_REPORT output_report ={
    .length = 8,
    .data={0}
};
HID_REPORT input_report ={
    .length = 0,
    .data = {0}
};





// main() runs in its own thread in the OS
int main()
{
    while (true) {
     //pcDebug.printf("Im SPLink Serial Console \r\n");
     //usbSerial.printf("Im virtual usb Serial port \r\n");
    //Filling report 

    for(int i = 0; i<output_report.length;i++){
        output_report.data[i] = rand();
    }

    //SendReport 

    hid.send(&output_report);
      
    

    //Read a message

    if(hid.read_nb(&input_report)){
        for(int i=0;i<input_report.length;i++){
            printf("%d\r",input_report.data[i]);
        }
    }

    }
}


