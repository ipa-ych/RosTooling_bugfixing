import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression, PathJoinSubstitution, TextSubstitution

def generate_launch_description():
  ld = LaunchDescription()
  
  # *** ROS 1 to ROS 2 bridges ***
  cob_teleop_robot_ros1_bridge_config = os.path.join(
    get_package_share_directory('cob_teleop_robot'),
    'config',
    'ros1_bridges.yaml'
  )

  load_bridge_params = ExecuteProcess(
      cmd=['rosparam', load, cob_teleop_robot_ros1_bridge_config]
  )

  ros1_topic_bridge_parameter_bridge = ExecuteProcess(
      cmd=['ros2', 'run', 'ros1_bridge', 'parameter_bridge', '__ns:=bridge_cob_teleop_robot_topics', '__name:=ros1_topic_bridge_parameter_bridge']


  return LaunchDescription([
    RegisterEventHandler(
      event_handler=OnExecutionComplete(
        target_action=load_bridge_params,
        on_completion=[
          LogInfo(msg='Load bridge parameter finished'),
          LogInfo(msg='launching bridge for topics'),
          ros1_topic_bridge_parameter_bridge,
          LogInfo(msg='Start loading bridge parameters'),
          load_bridge_params]
      )
    ),
    load_bridge_params
  ])
