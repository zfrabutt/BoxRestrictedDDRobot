#!/bin/bash

rosrun gazebo_ros spawn_model -file models/box_make.urdf -urdf -model $1 -y $3 -x $2 -z 5.0