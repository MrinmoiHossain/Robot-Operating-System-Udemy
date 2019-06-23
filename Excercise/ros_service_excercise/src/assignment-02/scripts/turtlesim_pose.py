#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
import std_srvs.srv import Empty

x = 0
y = 0
z = 0
yaw = 0

def poseCallback(pose_message):
    #print("Pose Callback")
    #print("x = {}".format(pose_message.x))
    #print("y = %f" % pose_message.y)
    #print("yaw =", pose_message.theta)
    global x, y, z, yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta

def move(speed, distance):
    velocity_message = Twist()

    x0 = x
    y0 = y
    velocity_message.linear.x = speed
    distance_moved = 0.0
    loop_rate = rospy.Rate(10)

    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    while True:
        rospy.loginfo('Turtlesim moves forwards')
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()

        distance_moved = distance_moved + abs(0.5 * math.sqrt((x - x0)**2 + (y - y0)**2))
        print(distance_moved)

        if not(distance_moved < distance):
            rospy.loginfo('reached')
            break

    velocity_message.linear.x = 0
    velocity_publisher.publish(velocity_message)


if __name__ == '__main__':
    try:
        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        cmd_vel_topic = '/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        position_topic = '/turtle1/pose'
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)

        time.sleep(2)
        print('move')
        move(1.0, 5.0)
        time.sleep(2)
        print('start reset: ')
        rospy.wait_for_service('reset')
        reset_turtle = rospy.SeviceProxy('reset', Empty)
        reset_turtle()
        print('end reset')
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo('node terminated')