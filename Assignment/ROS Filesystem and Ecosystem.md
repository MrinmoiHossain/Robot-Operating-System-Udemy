1. What is the first command you must run in ROS?
```bash
roscore
```
2. What is the command to run the Turtlesim simulator?
```bash
rosrun turtlesim turtlesim_node
```
3. What is the command to find the list of all ROS nodes?
```bash
rosnode list
```
4. What is the command to find the list of all ROS topics?
```bash
rostopic list
```
5. What is the topic that tells about the position of the turtle?
```bash
/turtle1/pose
```
6. What is the topic that sends command to the turtle to make it move?
```bash
turtle1/cmd_vel
```
7. What is the command that tells you information about the topic about velocity?
```bash
rostopic info /turtle1/cmd_vel
```
8. What is the node used to publish velocity commands to the turtle?
```bash
turtle_teleop_key
```
9. What is the node used to subscribe to velocity commands to the turtle?
```bash
turtlesim
```
10. What is the command that allows to see the type of message for velocity topic?
```bash
rostopic info /turtle1/cmd_vel 
``` 
11. What is the content of the velocity message? Explain its content.
```bash
rosmsg show geometry_msgs/Twist
``` 
```
    linear:
      float32 x
      float32 y
      float32 z
    angular:
      float32 x
      float32 y
      float32 z
```
- Two types of velocity: linear and angular velocity. Here, x and y are linear velocity and z is angular velocity.
12. What is the content of the position message? Explain its content
```bash
rosmsg show turtlesim/Pose
```
```
    float32 x  
    float32 y  
    float32 theta
     
    float32 linear_velocity
    float32 angular_velocity
```
- Here, x and y are coordinates position and theta angular position