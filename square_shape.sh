#!/bin/bash

rosrun gazebo_ros spawn_model -file box.sdf -sdf -model $1 -y $3 -x $2 -z 1.0