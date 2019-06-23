#!/usr/bin/env python
import rospy
from ros_essential_cpp.msg import IoTSensor

def iot_sensor_callback(iot_sensor_message):
    rospy.loginfo("New IoT data received: (%d, %s, %.2f, %.2f)",
                    iot_sensor_message.id, iot_sensor_message.name,
                    iot_sensor_message.temperature, iot_sensor_message.humidity)

def listener():
    rospy.init_node('iot_sensor_subcriber_node', anonymous=True)
    rospy.Subscriber('iot_sensor_topic', IoTSensor, iot_sensor_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()