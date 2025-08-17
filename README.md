# Dobot-Magician-Python-Control
This script connects to a Dobot robotic arm, configures its motion parameters, sends it to its home position, and then disconnects. Perfect for anyone who doesn't want to go through chinese electronics hell and their support.
Perfectly working py integration, feel free to do whatever you want in there!

run_dobot function:<br/>
-Loads the Dobot API from the DLL.<br/>
-Connects to the robot arm over serial (115200 baud).<br/>
-Prints the connection status.<br/>
-If connection is successful:<br/>
-Clears the robot’s command queue.<br/>
-Sets HOME parameters (where the arm returns to).<br/>
-Sets joint parameters and common PTP (point-to-point) motion parameters.<br/>
-Issues a HOMECmd (send the arm to its home position).<br/>
-Starts executing queued commands.<br/>
.Disconnects the Dobot.<br/>
