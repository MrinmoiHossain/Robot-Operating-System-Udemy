#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "turtlesim/Pose.h"
using namespace std;

ros::Publisher velocity_publisher;
ros::Subscriber pose_subscriber;
turtlesim::Pose turtlesim_pose;

const double PI = 3.14159265359;

//move the robot straight
void move(double speed, double distance, bool isForward);
void rotate(double angular_speed, double angle, bool clockwise);
double degree2radian(double deg);
void setDesireOrientation(double desired_angle_radian);
void poseCallback(const turtlesim::Pose::ConstPtr &pose_message);
void moveGoal(turtlesim::Pose goal_pose, double distance_tolerance);
double getDistance(double x1, double y1, double x2, double y2);

int main(int argc, char **argv)
{
    ros::init(argc, argv, "robot_cleaner");
    ros::NodeHandle n;

    double speed, distance;
    bool isForward;

    velocity_publisher = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 10);
    pose_subscriber = n.subscribe("/turtle1/pose", 10, poseCallback);
    /* 
    cout << "Enter Speed: ";
    cin >> speed;
    cout << "Enter Distance: ";
    cin >> distance;
    cout << "Forward?: ";
    cin >> isForward;
    move(speed, distance, isForward);

    double angular_speed, angle;
    bool clockwise;

    cout << "Enter angular velocity (deg/sec): ";
    cin >> angular_speed;
    cout << "Enter desired angle (deg): ";
    cin >> angle;
    cout << "Clockwise?: ";
    cin >> clockwise;
    rotate(degree2radian(angular_speed), degree2radian(angle), clockwise);
    */

    /* 
    setDesireOrientation(degree2radian(120));
    ros::Rate loop_rate(0.5);
    loop_rate.sleep();
    setDesireOrientation(degree2radian(-60));
    loop_rate.sleep();
    setDesireOrientation(degree2radian(0));
    */

    ros::Rate loop_rate(0.5);
    turtlesim::Pose goal_pose;
    goal_pose.x = 1;
    goal_pose.y = 1;
    goal_pose.theta = 0;
    moveGoal(goal_pose, 0.01);
    loop_rate.sleep();

    ros::spin();

    return 0;
}

void move(double speed, double distance, bool isForward)
{
    geometry_msgs::Twist vel_msg;

    //distance = speed * time

    //set a random linear velocity in the x-axis
    if(isForward)
        vel_msg.linear.x = abs(speed);
    else
        vel_msg.linear.x = -abs(speed);
    vel_msg.linear.y = 0;
    vel_msg.linear.z = 0;

    //set a random angular velocity in the y-axis
    vel_msg.angular.x = 0;
    vel_msg.angular.y = 0;
    vel_msg.angular.z = 0;

    //current time: t0
    double t0 = ros::Time::now().toSec();
    double current_distance = 0;
    ros::Rate loop_rate(100);
    do{
        //publish the velocity
        velocity_publisher.publish(vel_msg);
        double t1 = ros::Time::now().toSec();

        //current distance = speed * (t1 - t0)
        current_distance = speed * (t1 - t0);
        ros::spinOnce();
        loop_rate.sleep();
    }while(current_distance < distance);
    vel_msg.linear.x = 0;
    velocity_publisher.publish(vel_msg);
}

void rotate(double angular_speed, double angle, bool clockwise)
{
    geometry_msgs::Twist vel_msg;

    vel_msg.linear.x = 0;
    vel_msg.linear.y = 0;
    vel_msg.linear.z = 0;
    vel_msg.angular.x = 0;
    vel_msg.angular.y = 0;

    //clockwise -> negative
    if(clockwise)
        vel_msg.angular.z = -abs(angular_speed);
    else
        vel_msg.angular.z = abs(angular_speed);
    
    double current_angle = 0.0;
    double t0 = ros::Time::now().toSec();
    ros::Rate loop_rate(100);
    do{
        velocity_publisher.publish(vel_msg);
        double t1 = ros::Time::now().toSec();
        current_angle = angular_speed * (t1 - t0);
        ros::spinOnce();
        loop_rate.sleep();
    }while(current_angle < angle);

    vel_msg.angular.z = 0;
    velocity_publisher.publish(vel_msg);
}

double degree2radian(double deg)
{
    return (deg * PI) / 180.0;
}

void setDesireOrientation(double desired_angle_radian)
{
    double relative_angle_radian = desired_angle_radian - turtlesim_pose.theta;
    bool clockwise = ((relative_angle_radian < 0)? true : false);
    rotate(abs(relative_angle_radian) / 4, abs(relative_angle_radian), clockwise);
}

void poseCallback(const turtlesim::Pose::ConstPtr &pose_message)
{
    turtlesim_pose.x = pose_message->x;
    turtlesim_pose.y = pose_message->y;
    turtlesim_pose.theta = pose_message->theta;
}

double getDistance(double x1, double y1, double x2, double y2)
{
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
}

void moveGoal(turtlesim::Pose goal_pose, double distance_tolerance)
{
    geometry_msgs::Twist vel_msg;

    ros::Rate loop_rate(10);
    do{
        //linear velocity in the x-axis
        vel_msg.linear.x = 1.5 * getDistance(turtlesim_pose.x, turtlesim_pose.y, goal_pose.x, goal_pose.y);
        vel_msg.linear.y = 0;
        vel_msg.linear.z = 0;
        //angular velocity in the z-axis
        vel_msg.angular.x = 0;
        vel_msg.angular.y = 0;
        vel_msg.angular.z = 4 * (atan2(goal_pose.y - turtlesim_pose.y, goal_pose.x - turtlesim_pose.x) - turtlesim_pose.theta);

        velocity_publisher.publish(vel_msg);
        ros::spinOnce();
        loop_rate.sleep();
    }while(getDistance(turtlesim_pose.x, turtlesim_pose.y, goal_pose.x, goal_pose.y) > distance_tolerance);
    cout<< "End Move Goal" << endl;
    vel_msg.linear.x = 0;
    vel_msg.angular.z = 0;
    velocity_publisher.publish(vel_msg);
}