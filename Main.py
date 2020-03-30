import Drone
import sys
import time

# Live drone
#drone_1 = drone.Drone("128.1.1.1", 8889)

# Test drone
# drone start up
drone_1 = Drone.Drone('192.168.10.1', 8889)
drone_1.printInfo(1)
drone_1.connect(1)

