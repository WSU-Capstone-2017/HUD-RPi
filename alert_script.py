# Nasser alert script


import obd

connection = obd.OBD()

cmd = obd.commands.GET_DTC

while 1:
    response = connection.query(cmd).value
    
    print response

    
