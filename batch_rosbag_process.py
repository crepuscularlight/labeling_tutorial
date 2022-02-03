#!/usr/bin/env python
# coding=utf-8

"""Extract images from a rosbag.
"""

import os
import argparse
import datetime
import cv2
from os import path
from time import gmtime,strftime

import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():
    """Extract a folder of images from a rosbag.
    """
    parser = argparse.ArgumentParser(description="Extract images from a ROS bag.")
    parser.add_argument("bag_file_dir", help="Input ROS bag.")
    parser.add_argument("output_dir", help="Output directory.")
    parser.add_argument("image_topic", help="Image topic.")

    args = parser.parse_args()

    file_names=os.listdir(args.bag_file_dir)

    bag_names=[]

    for name in file_names:
        if name.endswith(".bag"):
            bag_names.append(name)
    
    

    if(not path.exists(args.output_dir)):
        # args.output_dir='./img'+str(strftime("%Y-%m-%d-%H-%M-%S", gmtime()))
        # args.output_dir='./img_'+str(args.bag_file)
        os.mkdir(args.output_dir)

    
    for bag_name in bag_names:

        print ("Extract images from %s on topic %s into %s" % (bag_name,
                                                            args.image_topic, args.output_dir))

        bag = rosbag.Bag(bag_name, "r")
        bridge = CvBridge()
        count = 0
        images_dir=args.output_dir+"/img_"+bag_name
        if not os.path.exists(images_dir):
            os.mkdir(images_dir)

        for topic, msg, t in bag.read_messages(topics=[args.image_topic]):
            if count % 100 == 0:
                cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")

                cv2.imwrite(os.path.join(images_dir, f"{bag_name}frame%06i.png" % count), cv_img)
                print( "Wrote image %i" % count)

            count += 1

        bag.close()

    return

if __name__ == '__main__':
    main()

