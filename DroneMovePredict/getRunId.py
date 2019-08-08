#run this file to get a runId
#insert runID into scene%d.py
import firedrone.client as fdc
from firedrone.client.errors import FireDroneClientHttpError


workspace = fdc.Workspace('' )
#workspace.directrun_end('')

#Insert scene number
try:
    start_result = workspace.directrun_start(21)
    print(start_result)
except FireDroneClientHttpError as e:
    print(e)
