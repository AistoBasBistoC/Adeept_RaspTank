import time
import threading
import move
import Adafruit_PCA9685
import os
import info
import RPIservo

functionMode = 0
speed_set = 100
rad = 0.5
turnWiggle = 60

# move servo init
scGear = RPIservo.ServoCtrl()
scGear.moveInit()

# camera turn? init
P_sc = RPIservo.ServoCtrl()
P_sc.start()

# camera pitch? init
T_sc = RPIservo.ServoCtrl()
T_sc.start()

# arm servo init
H1_sc = RPIservo.ServoCtrl()
H1_sc.start()

# hand servo init
H2_sc = RPIservo.ServoCtrl()
H2_sc.start()

# grabber init
G_sc = RPIservo.ServoCtrl()
G_sc.start()

# modeSelect = 'none'
modeSelect = 'PT'

init_pwm0 = scGear.initPos[0]
init_pwm1 = scGear.initPos[1]
init_pwm2 = scGear.initPos[2]
init_pwm3 = scGear.initPos[3]
init_pwm4 = scGear.initPos[4]


# TEST ARM CODE
# move arm down, stop, grab, stop, arm up, stop, release, stop
H1_sc.singleServo(12, -1, 7) # arm down
time.sleep(1)
H1_sc.stopWiggle() # stop
time.sleep(1)
G_sc.singleServo(15, 1, 3) # grab
time.sleep(1)
G_sc.stopWiggle() # stop
time.sleep(1)
H1_sc.singleServo(12, 1, 7) # arm up
time.sleep(1)
H1_sc.stopWiggle() # stop
time.sleep(1)
G_sc.singleServo(15, -1, 3) # release
time.sleep(1)
G_sc.stopWiggle() # stop
time.sleep(1)

