import obd

connection = obd.OBD() #connects to port automatically
while true
	cmd = obd.commands.FUEL_LEVEL #outputs as percent

response =  connection.query(cmd) # send command, parse response

print(response.value)


#to slow down the numbers:
#connection = obd.OBD(baudrate=)
#
#import obd, time
#connection = obd.OBD(baudrate=38400, fast=False)
#while True:
#	for i in commands_list:
#		cmd1 = obd.commands.RPM       # select an OBD command (sensor)
#        response1 = connection.query(cmd1) # send the command, and parse the response
#        print(response1.value) # returns unit-bearing values thanks to Pint
#        # connection.close()
#
#        cmd2 = obd.commands.COOLANT_TEMP # select an OBD command (sensor)
#        response2 = connection.query(cmd2) # send the command, and parse the response
#        print(response2.value)
#        # connection.close()
#        time.sleep(0.5)
