#include <ros/ros.h>
#include <cv_bridge/cv_bridge.h>
#include <opencv/cv.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/objdetect/objdetect.hpp>
#include <people_msgs/PositionMeasurementArray.h>
#include <sensor_msgs/PointCloud.h>
#include <sensor_msgs/image_encodings.h>

void face_cloud_Callback(sensor_msgs::PointCloud a)
{
  ROS_INFO("I received some point cloud info!");
}

void pos_meas_Callback(people_msgs::PositionMeasurementArray a)
{
  ROS_INFO("I received some position info!");
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "faces");
  ros::NodeHandle nh;

  ros::Subscriber sub = nh.subscribe("/face_detector/faces_cloud", 1000, face_cloud_Callback);
  ros::Subscriber sub2 = nh.subscribe("/face_detector/people_tracker_measurements_array", 1000, pos_meas_Callback);
  ros::spin();
}
