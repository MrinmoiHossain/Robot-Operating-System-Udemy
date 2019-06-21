### Check all correct answers for the CMakeLists.txt file. 
- CMakeLists.txt file describes how to build the code and where to install it to
- The file CMakeLists.txt is the input to the CMake build system for building software packages

### It is a good practice to source your overlay workspace in the .bashrc rather than sourcing it every time when you open a new terminal 
- True

### Image you have create a new workspace called catkin_ws in the path /home/user/ and you use a ROS Kinetic version. What is the command you must execute to enable the workspace that you have created?
- source /home/user/catkin_ws/devel/setup.bash

### `roscd` this command takes you to the last ROS workspace that you have sourced its `setup.bash`.
- True

### `roscd` this command takes you to the default ROS package
- False

### Check all correct answers
- A ROS workspace contains three main folders: a `source` folder, a `devel` folder and a `build` folder.
- A ROS workspace is a user directory that we will used to create the user ROS packages
- A ROS workspace is built using `catkin_make` command

### Check all correct answers for the file `package.xml`.
- `package.xml` is used to describe the package and set its dependencies
- `package.xml` is automatically generated when creating a new ROS package
- `package.xml` defines two types of dependencies: (1) dependencies needed to build a package, (2) dependencies needed to execute the package
- You can define a liencese of your package in `package.xml`.

### What is the command used to create a new ROS package called my_package
- cd ~/catkin_ws/src
- catkin_create_pkg my_package std_msgs rospy roscpp