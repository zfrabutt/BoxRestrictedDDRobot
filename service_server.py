#! /usr/bin/env python

import os
import rospy
import math
import numpy as np
import time as t
from std_srvs.srv import Trigger, TriggerResponse
from gazebo_msgs.srv import GetModelState, GetModelStateRequest

name = 'box'
box_i = 0
robot_proxy = None 

def trigger_response(request):

    global box_i

    dropBool = False
    a = getRobotLocation()
    x = a[0]
    y = a[1]
    b = getBoxLocation(x,y)
    if (b != None):
        if not checkBoxLocation(b[0],b[1]):
            dropBox(b[0], b[1])
            dropBool = True
 

    return TriggerResponse(
        success = dropBool,
        message = "dt = "
    )

def delBox(bi):
    buff = "rosservice call gazebo/delete_model "+name+str(bi)+" &"
    print bi
    os.system(buff)

def delBoxAll(bi):
    for i in range(bi):
        delBox(i)
        t.sleep(0.1)


box_x = []
box_y = []

def saveBoxVal(x,y):
    global box_X, box_y
    box_x.append(x)
    box_y.append(y)
    return

def checkBoxLocation(x, y):
    global box_x, box_y
    for i in range(len(box_x)):
        xx = box_x[i]
        yy = box_y[i]
        d = np.sqrt((xx-x) * (xx - x) + (yy-y) * (yy-y))
        if d < .75:
            return True
    return False



def dropBox(x,y):
    global box_i

    print("test")
    saveBoxVal(x,y)

    b0 = ("./square_shape.sh ")
    b1 = name + str(box_i) + " "
    box_i += 1
    b2 = str(x) + " "
    b3 = str(y)
    b4 = "&"
    buff = b0 + b1 + b2 + b3 + b4
    os.system(buff)
    

def getBoxLocation(x,y):

    if (x < 24 and x > -24 and  y < 24 and y > -24):
        return None

    if (x >= 24):
        xn = 25
    elif (x <= -24):
        xn = -25
    else:
        if  x > -.5 and x < .5:
            xn = 0
        elif x > 0:
            xn = math.ceil(x)
        else:
            xn = math.floor(x)


    if (y <= -24):
        yn = -25
    elif (y >= 24) :
        yn = 25
    else:
        if y > -.5 and y < -.5:
            yn = 0
        elif y > 0:
            yn = math.ceil(y)
        else:
            yn = math.floor(y)

    return ((xn, yn))

def getRobotLocation():
    global robot_proxy

    a = GetModelStateRequest(model_name = 'dd_robot')
    a.model_name="dd_robot"
    s = robot_proxy(a)

    

    x = s.pose.position.x
    y = s.pose.position.y
    print(x,y)
    return ((x,y))

rospy.init_node('service_example')
#delBoxAll(255)
my_service = rospy.Service('/box', Trigger, trigger_response)

rospy.wait_for_service('gazebo/get_model_state')
robot_proxy = rospy.ServiceProxy('gazebo/get_model_state', GetModelState)

rospy.spin()