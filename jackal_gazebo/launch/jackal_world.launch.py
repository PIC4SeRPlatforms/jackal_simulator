from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration

from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    world = LaunchConfiguration('world')
    world_arg = DeclareLaunchArgument(
        'world',
        default_value='empty.world',
        description='Full path to world model file to load or a Gazebo world file name',
    )

    gazebo_launch = PathJoinSubstitution(
        [FindPackageShare('jackal_gazebo'),
         'launch',
         'gazebo.launch.py'],
    )

    gazebo_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([gazebo_launch]),
        launch_arguments={'world_path': world}.items(),
    )

    ld = LaunchDescription()
    ld.add_action(world_arg)
    ld.add_action(gazebo_sim)

    return ld
