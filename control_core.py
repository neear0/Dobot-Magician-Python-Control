import cv2
import numpy as np
import threading 
import DobotDllType as dobot_dll

status_mes = {
    dobot_dll.DobotConnect.DobotConnect_NoError:  "no error",
    dobot_dll.DobotConnect.DobotConnect_NotFound: "not found",
    dobot_dll.DobotConnect.DobotConnect_Occupied: "connection occupied"
}

def run_dobot():
    dobot_api = dobot_dll.load()
    dobot_state = dobot_dll.ConnectDobot(dobot_api, "", 115200)[0]
    print("Connection status:",status_mes[dobot_state])

    if (dobot_state == dobot_dll.DobotConnect.DobotConnect_NoError):
      
      dobot_dll.SetQueuedCmdClear(dobot_api)

      dobot_dll.SetHOMEParams(dobot_api, 206.7, 0, 135, 12.87, isQueued = 1)
      dobot_dll.SetPTPJointParams(dobot_api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
      dobot_dll.SetPTPCommonParams(dobot_api, 50, 50, isQueued = 1)

      dobot_dll.SetHOMECmd(dobot_api, temp = 0, isQueued = 1)
  
    dobot_dll.SetQueuedCmdStartExec(dobot_api)
    dobot_dll.DisconnectDobot(dobot_api)

if __name__ == "__main__":
  run_dobot.start()