#!/usr/bin/env python
import rospy
import math
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_srvs.srv import Empty

global turtle_pose
turtle_pose = Pose()

def poseCallback(pose_message):
    global turtle_pose
    turtle_pose.x = pose_message.x
    turtle_pose.y = pose_message.y
    turtle_pose.theta = pose_message.theta

def degree2radian(angle):
    return angle * math.pi / 180.0

def getDistance(x1, y1, x2, y2):
    return math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

def move(speed, distance, isForward):
    vel_msg = Twist()

    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)

    vel_msg.linear.y = 0
    vel_msg.linear.z = 0

    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    # current time
    t0 = time.time()
    current_distance = 0.0

    loop_rate = rospy.Rate(10)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    while current_distance < distance:
        rospy.loginfo('Moving Forward')
        velocity_publisher.publish(vel_msg)

        t1 = time.time()
        current_distance = speed * (t1 - t0)
        loop_rate.sleep()

    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)    

def rotate(angular_speed, angle, clockwise):
    vel_msg = Twist()

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    # clockwise -> negative
    if(clockwise):
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)

    current_angle = 0.0
    t0 = time.time()
    loop_rate = rospy.Rate(10)

    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    while True:
        rospy.loginfo("Rotating Rover")
        velocity_publisher.publish(vel_msg)

        t1 = time.time()
        current_angle = angular_speed * (t1 - t0)
        loop_rate.sleep()

        if current_angle > angle:
            rospy.loginfo("Rotating Complete")
            break

    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

def setDesireOrientation(desired_angle_radian):
    relative_angle_radian = desired_angle_radian - turtle_pose.theta
    clockwise = relative_angle_radian < 0
    rotate(abs(relative_angle_radian), abs(relative_angle_radian), clockwise)

def moveGoal(goal_pose, distance_tolerance):
    vel_msg = Twist()

    loop_rate = rospy.Rate(10)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    while getDistance(turtle_pose.x, turtle_pose.y, goal_pose.x, goal_pose.y) > distance_tolerance:
        vel_msg.linear.x = 0.5 * getDistance(turtle_pose.x, turtle_pose.y, goal_pose.x, goal_pose.y)
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0

        # angular velocity
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 4 * (math.atan2(goal_pose.y - turtle_pose.y, goal_pose.x - turtle_pose.x) - turtle_pose.theta)

        velocity_publisher.publish(vel_msg)
        loop_rate.sleep()


    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

def gridClean():
    loop_rate = rospy.Rate(0.5)
    pose = Pose()
    pose.x = 1
    pose.y = 1
    pose.theta = 0
    moveGoal(pose, 0.01)
    loop_rate.sleep()

    rospy.loginfo("Set Desired Orientation")
    setDesireOrientation(0)
    loop_rate.sleep()

    rospy.loginfo("3rd Point")
    move(2.0, 9.0, True)
    loop_rate.sleep()
    rospy.loginfo("4th rotate")
    rotate(degree2radian(10), degree2radian(90), False)
    loop_rate.sleep()

    rospy.loginfo("5th Point")
    move(2.0, 9.0, True)
    rospy.loginfo("6th rotate")
    rotate(degree2radian(10), degree2radian(90), False)
    rospy.loginfo("7th Point")
    move(2.0, 1.0, True)
    rospy.loginfo("8th rotate")
    rotate(degree2radian(10), degree2radian(90), False)
    loop_rate.sleep()

    rospy.loginfo("9th Point")
    move(2.0, 9.0, True)
    rospy.loginfo("10th rotate")
    rotate(degree2radian(10), degree2radian(90), True)
    loop_rate.sleep()
    

def spiralClean():
    vel_msg = Twist()

    count = 0
    constant_speed = 4
    vk = 1
    wk = 2
    rk = 0.5

    loop_rate = rospy.Rate(1)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    while(turtle_pose.x < 10.5 and turtle_pose.y < 10.5):
        rk += 0.5
        vel_msg.linear.x = rk
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0

        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = constant_speed

        rospy.loginfo("vel_msg.linear.x = " + str(vel_msg.linear.x))
        rospy.loginfo("vel_msg.angular.z = " + str(vel_msg.angular.z))

        velocity_publisher.publish(vel_msg)
        loop_rate.sleep()

    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        rospy.init_node('turtlesim_motion', anonymous=True)

        publisher_topic = '/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(publisher_topic, Twist, queue_size = 10)

        pose_topic = '/turtle1/pose'
        pose_subscriber = rospy.Subscriber(pose_topic, Pose, poseCallback)

        # move(1.0, 3.5, True)
        # rotate(30, 90, False)
        # setDesireOrientation(degree2radian(90))

        '''
        goal_pose = Pose()
        goal_pose.x = 1
        goal_pose.y = 1
        goal_pose.theta = 0
        moveGoal(goal_pose, 0.01)
        '''

        # gridClean()
        spiralClean()

        time.sleep(2)

    except rospy.ROSInterruptException:
        rospy.loginfo('Node terminated')