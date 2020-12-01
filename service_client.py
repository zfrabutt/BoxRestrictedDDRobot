#! /usr/bin/env python

import rospy
import time as t
from std_srvs.srv import Trigger, TriggerRequest

rospy.init_node('service_client')

rospy.wait_for_service('/box')

sos_service = rospy.ServiceProxy('/box', Trigger)

sos = TriggerRequest()

while True:

    tick = t.time()
    result = sos_service(sos)
    tock = t.time()

    #print(tock - tick)
    t.sleep(0.2)

#print(result)