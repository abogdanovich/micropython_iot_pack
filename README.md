# micropython_iot_pack
micropython_iot_mini_pack wifi \ mqtt 

erase esp8266 > esptool.py --port COM7 erase_flash
burn firmware > esptool.py --port COM7 --baud 115200 write_flash --flash_size=detect -fm dio 0 esp8266-20190529-v1.11.bin

upload files using ampy -p COMx put filename/folder
run python file at microcontroller using ampy -p COMx run filename/folder

pull requests are welcome all time! enjoy and thanks for your contribution!
