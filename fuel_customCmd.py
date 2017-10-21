#Nasser custom command for fuel

from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int
import obd




def fuel(messages):
        d = messages[0].data
        v = bytes_to_int(d) / 4.0
        return v 
c = OBDCommand("FUEL_LEVEL", \
                "Fuel level", \
                "010F", \
                2, \
                fuel, \
                ECU.ENGINE, \
                True)
o = obd.OBD()
o.supported_commands.add(c)
o.query(c)
newfuel=o.supported_commands.add(c)
while 1:
        newfuelresp = o.query(c)
        print newfuelresp
       # newfuelstr = str(newfuelresp.value).split()
        #if newfuelstr[0] != "None":
              #  fuel = float(newfuelstr[0])
               # print fuel
