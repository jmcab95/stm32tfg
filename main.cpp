#include "USBSerial.h"
#include "drivers/USBHID.h"
#include "mbed.h"
#include "nanopb_library/messagesPrueba.pb.h"
#include "nanopb_library/pb_common.h"
#include "nanopb_library/pb_decode.h"
#include "nanopb_library/pb_encode.h"

Serial pcDebug(USBTX, USBRX);
USBSerial usbSerial;
MensajePruebasPySTM mensajePrueba;
size_t message_length = 128;
bool status;
char flag_inicio = 0xaa;
char flag_final = 0xba;

// main() runs in its own thread in the OS
int main() {

  char temp;

  while (1) {

    int i = 0;
    if (usbSerial.readable()) {

      if ((temp = usbSerial.getc()) == 0xaa) {
        // pcDebug.printf("Entra en primer flag");
        if ((temp = usbSerial.getc()) == 0xaa) {
          // pcDebug.printf("Entra en segundo flag");
          // Segundo flag
          temp = usbSerial.getc();
          // pcDebug.printf("Valor lenght leido: %d",temp);
          message_length = temp;
          uint8_t buf[message_length];

          while (((temp = usbSerial.getc()) != 0xba) and (i < message_length)) {
            // pcDebug.printf("Valor actual %02X", temp);
            buf[i] = temp;
            i++;
          }

          pb_istream_t stream = pb_istream_from_buffer(buf, message_length);
          status =
              pb_decode(&stream, MensajePruebasPySTM_fields, &mensajePrueba);

          if (!status) {
            pcDebug.printf("Decoding failed %s\n", PB_GET_ERROR(&stream));
            return 1;
          }

          pcDebug.printf("el msg del parametro es %d",
                         mensajePrueba.digitalPin);
        }
      }
    } else {
      // Enviamos un mensaje protobuffer
      // Modificamos
      mensajePrueba.digitalPin = 564;
      mensajePrueba.analogPin = 987;
      mensajePrueba.codigo = 125;
      message_length = sizeof(mensajePrueba);
      uint8_t buf[message_length];
      pb_ostream_t stream = pb_ostream_from_buffer(buf, sizeof(buf));

      status = pb_encode(&stream, MensajePruebasPySTM_fields, &mensajePrueba);
      message_length = stream.bytes_written;

      if (!status) {
        pcDebug.printf("Encoding failed %s\n", PB_GET_ERROR(&stream));
        return 1;
      } else {
        // si esta bien encodeado mandamos cabeceras, longitud, mensaje y flag
        // de cierre

        usbSerial.putc(flag_inicio);
        usbSerial.putc(flag_inicio);
        usbSerial.putc(message_length);
        for (i = 0; i < message_length; i++) {
          pcDebug.printf("-- %d --", buf[i]);
          usbSerial.putc(buf[i]);
        }
        usbSerial.putc(flag_final);
      }
    }
  }
}
