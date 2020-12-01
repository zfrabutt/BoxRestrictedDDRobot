#!/usr/bin/env python3
#Modified Given Code
import rospy
import socket
from std_msgs.msg import String 
from gazebo_msgs.srv import ApplyJointEffort
from gazebo_msgs.srv import GetJointProperties
from std_msgs.msg import Header

lastInput = None

def setRot(pub, val, direction):
    buff = ApplyJointEffort()
    buff.effort = val

    start_time = rospy.Time(0,0)
    end_time = rospy.Time(0.01,0)
    if direction == "l":
        buff.joint_name = "dd_robot::left_wheel_hinge"
        pub(buff.joint_name,  buff.effort, start_time, end_time)
    if direction == "r":
        buff.joint_name = "dd_robot::right_wheel_hinge"
        pub(buff.joint_name, -buff.effort, start_time, end_time)

def callback(msg): 

    global lastInput


    pub = rospy.ServiceProxy('/gazebo/apply_joint_effort',ApplyJointEffort)

    d = msg.data
    print(lastInput)
    if lastInput != None:
        if lastInput == "w":
            setRot(pub, -100, "r")
            setRot(pub, 100, "l")
        elif lastInput == "s":
            setRot(pub, 100, "r")
            setRot(pub, -100, "l")
        elif lastInput == "a":
            setRot(pub, 100, "r")
            setRot(pub, 100, "l")
        elif lastInput == "d":
            setRot(pub, -100, "r")
            setRot(pub, -100, "l")
        else:
            pass
    
    lastInput = d

    if (d == "w"):
        setRot(pub, 100, "r")
        setRot(pub, -100, "l")
    elif (d == "s"):
        setRot(pub, -100, "r")
        setRot(pub, 100, "l")
        pass
    elif (d == "a"):
        setRot(pub, -100, "r")
        setRot(pub, -100, "l")
    elif (d == "d"):
        setRot(pub, 100, "r")
        setRot(pub, 100, "l")
    else:
        pass

    rate = rospy.Rate(10)
    rate.sleep()


rospy.init_node('dd_ctrl', anonymous=True)
sub = rospy.Subscriber('/key_press', String, callback)
rospy.spin()           