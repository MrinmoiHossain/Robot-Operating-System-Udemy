### 1. What is the command used to create a ROS package called ros_service_assignment? Make sure to clarify the path where to create it. 
```bash
~$ cd catkin_ws/
~/catkin_ws$ cd src
~/catkin_ws/src$ catkin_create_pkg ros_service_assignment roscpp rospy std_msgs
~/catkin_ws/src$ cd ..
~/catkin_ws$ catkin_make
``` 
### 2. What is the name of the folder when to create the service file? Provide the absolute path to the file (from the root). 
The name of the folder is "srv" when to create the service file.
```bash
Absolute path: /home/mrinmoi/Udemy_ROS/catkin_ws/src/ros_service_assignment/srv
``` 
### 3. What is the content of the service file RectangleAreaService.srv?
```
float32 width
float32 height
---
float32 area
``` 
### 4. What are the changes you need to do in the CMakeLists.txt. Copy/paste the whole CMakeLists.txt. 
```
find_package(catkin REQUIRED COMPONENTS
    roscpp
    rospy
    std_msgs
    message_generation
)

add_service_files(
    FILES
    RectangleArea.srv
)

generate_message(
    DEPENDENCIES
    std_msgs
)
``` 
### 5. What are the changes you need to do the package.xml? Copy/paste the whole package.xml.
```
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend>
``` 
### 6. What is the command to build the new service and generate executable files?
```bash
~/caktin_ws$ catkin_make
``` 
### 7. How to make sure that service files are now created? 
```bash
rossrv list 
ros_service_assignment/RectangleArea 
``` 
### 8. Write the server application (C++ or Python)
```python
#!/usr/bin/env python

from ros_service_assignment.srv import RectangleArea
from ros_service_assignment.srv import RectangleAreaRequest
from ros_service_assignment.srv import RectangleAreaResponse

import rospy

def rectangle_area_callback(req):
    print("Returning area of a rectangle [%s * %s = %s]" % (req.width, req.height, req.width * req.height))
    return RectangleAreaResponse(req.width * req.height)

def rectangle_area_server():
    rospy.init_node('rectangle_area_server_node')
    s = rospy.Service('rectangle_area_service', RectangleArea, rectangle_area_callback)
    print("Ready to calculate the area of a rectangle.")
    rospy.spin()
    
if __name__ == "__main__":
    rectangle_area_server()
``` 
### 9. Write the client application (C++ or Python)
```python
#!/usr/bin/env python
import sys
import rospy
from ros_service_assignment.srv import RectangleArea
from ros_service_assignment.srv import RectangleAreaRequest
from ros_service_assignment.srv import RectangleAreaResponse

def request_rectangle_area(x, y):
    rospy.wait_for_service('rectangle_area_service')
    try:
        add_two_ints = rospy.ServiceProxy('rectangle_area_service', RectangleArea)
        server_response = add_two_ints(x, y)
        return server_response.area
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def usage():
    return "%s [x y]" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting the area of a rectangle of width %s and height %s" % (x, y))
    print("Area of the   a rectangle of width %s and height %s = %s" % (x, y, request_rectangle_area(x, y)))
``` 
### 10. What are the commands to test that the application works fine. 
```bash
~$ roscore
~$ rosrun ros_service_assignment rectangle_server.py
~$ rosrun ros_service_assignment rectangle_client.py 3.3 7.7
``` 
