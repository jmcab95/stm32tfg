# stm32tfg
Repositorio para TFG 

1 - Registrarse en https://os.mbed.com/ y seleccionar el tipo de placa que tenemos

2 - Descargar Mbed Studio

3 - Usar https://os.mbed.com/platforms/ST-Nucleo-F411RE/ como referencia. Al final aparece como instalar los drivers de STLink

--------------------------------------------------------------------------------------
Estructura del Repositorio
-------------------------------------------------------------------------------------
- ProtobufferSource: Contiene fichero .proto y .options

- hostPython: Contiene Programa de Control y las librerías protobuffers compiladas para Python

- Nanopb_library: Contiene los headers necesarios de nanopb para Mbed y los headers generados desde el .proto para mbed

- main.cpp: funcionalidad de la placa de desarrollo.

