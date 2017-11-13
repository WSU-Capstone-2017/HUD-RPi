import serial

serNum = serial.Serial {"/dev/ttyUSB0")
serNum.baudrate = 9600

result = ""

while True:

    dataResult = serNum.read(1)
    result+= dataResult

    if dataResult == '\n':

        if result[:6] == '$GPGLL' :
            print (result[7:33])

            result = ""
            break
        result = ""
