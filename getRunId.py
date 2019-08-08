#run this file to get a runId
#insert runID into scene%d.py
import firedrone.client as fdc
from firedrone.client.errors import FireDroneClientHttpError


workspace = fdc.Workspace('7#ogORpZ1j9CRAT$-AYVoG4SgVXnkjf&rC6Xg2kADk^ece-_gM9X5bp1HXA%%C!S' )
#workspace.directrun_end('390c00b6-4cf8-4e0d-8c75-a5b43e38a26e')

#Insert scene number
try:
    start_result = workspace.directrun_start(21)
    print(start_result)
except FireDroneClientHttpError as e:
    print(e)
