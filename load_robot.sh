rosservice call gazebo/delete_model bb_8
rosservice call gazebo/delete_model dd_robot
rosrun gazebo_ros spawn_model -file models/model.sdf -sdf -model dd_robot -y 23 -x 24 -z 1.0
