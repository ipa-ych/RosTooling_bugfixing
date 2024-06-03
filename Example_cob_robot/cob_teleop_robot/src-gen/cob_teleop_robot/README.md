# cob_teleop_robot

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
- joy_node
- twist_mux
- teleop_twist_joy_node

The listed nodes offer the following connections:
- Publisher: joy_pub [sensor_msgs/Joy]
- Publisher: /base/twist_controller/command [geometry_msgs/Twist]
- Subscriber: cmd_vel_sub [geometry_msgs/Twist]
- Subscriber: joy_sub [sensor_msgs/Joy]
- Publisher: cmd_vel_pub [geometry_msgs/Twist]

## Installation

### Using release

This package can be copied to a valid ROS 2 workspace. To be sure that all the related dependencies are intalles the command **rosdep install** can be used.
Then the workspace must be compiled using the common ROS 2 build command:

```
mkdir -p ros2_ws/src
cd ros2_ws/
cp -r PATHtoTHISPackage/cob_teleop_robot src/.
rosdep install --from-path src/ -i -y
colcon build
source install/setup.bash
```



## Usage


To execute the launch file, the following command can be called:

```
ros2 launch cob_teleop_robot cob_teleop_robot.launch.py 
```

The generated launch files requires the xterm package, it can be installed by:

```
sudo apt install xterm
```



