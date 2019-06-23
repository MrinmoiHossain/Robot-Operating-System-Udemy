#!/usr/bin/env python
import rospy
from ros_essential_cpp.msg import IoTSensor
import random

def talker():
    publisher = rospy.Publisher('iot_sensor_topic', IoTSensor, queue_size=10)
    rospy.init_node('iot_sensor_topic', anonymous=True)
    rate = rospy.Rate(7)

    cn = 1
    while not rospy.is_shutdown():
        iot_sensor = IoTSensor()
        iot_sensor.id = cn
        iot_sensor.name = 'IoT_Sensor '
        iot_sensor.temperature = 24.33 + (random.random() * 2)
        iot_sensor.humidity = 33.41 + (random.random() * 2)

        rospy.loginfo('I publish: ')
        rospy.loginfo(iot_sensor)
        publisher.publish(iot_sensor)
        rate.sleep()
        cn += 1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass