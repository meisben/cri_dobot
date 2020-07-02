# -*- coding: utf-8 -*-
"""Simple test script for Dobot Magician Robot class using Dobot Magician Controller.
"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Program Purpose: Test script demonstrating use of cri_dobot wrapper for cri library on the dobot magican robot arm

# Author: Ben Money-Coomes (ben.money@gmail.com)

# **Version control**  (Feb 2020)

# v0.0.1    Non commented code is fully functional
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# ------------------------------------------#
# Imports                                   #
# ------------------------------------------#

import time
import numpy as np

from cri.robot import AsyncRobot
from cri_dobot.robot import SyncDobot
from cri_dobot.controller import dobotMagicianController

# ------------------------------------------#
# Start of main program                     #
# ------------------------------------------#

np.set_printoptions(precision=2, suppress=True)


def main():
    base_frame = (0, 0, 0, 0, 0, 0)
    # base frame: x->front, y->right, z->up
    work_frame = (220, 0, 80, 0, 0, 0)

    with AsyncRobot(SyncDobot(dobotMagicianController())) as robot:

        speed_test1 = robot.linear_speed
        print("speed_test1 (mm/s)", speed_test1)

        angular_speed_test1 = robot.angular_speed
        print("angular_speed_test1 (deg/s)", angular_speed_test1)

        # Set TCP, linear speed,  angular speed and coordinate frame
        # note that it is advisable not to use a Tool Center Point due to the dobot magician bug explained in the readme
        robot.tcp = (0, 0, 0, 0, 0, 0)
        robot.linear_speed = 100
        robot.angular_speed = 100

        speed_test2 = robot.linear_speed
        print("speed_test2 (mm/s)", speed_test2)

        angular_speed_test2 = robot.angular_speed
        print("angular_speed_test2 (deg/s)", angular_speed_test2)

        # ----- TCP section
        print("Please note there is a dobot magician bug with the tcp, tcp is not used !")
        print("For a description of this bug see the cri_dobot readme...")
        # tcp_test2 = robot.tcp
        # print("tcp_test2", tcp_test2)

        # print("do something")

        # tcp_test3 = robot.tcp
        # print("tcp_test3", tcp_test3)

        # ---- Start from below here !

        # Display robot info
        # print("Robot info: {}".format(robot.info)) #Currently not used

        # Example of displaying current command index on dobot magician
        currentIndex = robot.sync_robot.controller.current_index()
        print("Current Command Index: {}".format(currentIndex))

        # Set base frame for storing home position
        robot.coord_frame = base_frame

        # Set home position
        print("Setting home position")
        robot.sync_robot.set_home_params((200, 0, 80, 0, 0, 0))

        # Perform homing
        print("Starting homing")
        robot.sync_robot.perform_homing()
        print("Homing finished...")

        # Return to work frame
        robot.coord_frame = work_frame

        # Display initial joint angles
        print("Initial joint angles: {}".format(robot.joint_angles))

        # Display initial pose in work frame
        print("Initial pose in work frame: {}".format(robot.pose))

        # Move to origin of work frame
        print("Moving to origin of work frame ...")
        robot.move_linear((0, 0, 0, 0, 0, 0))

        # Increase and decrease all joint angles
        print("Increasing and decreasing all joint angles ...")

        newJointAngles = tuple(np.add(robot.joint_angles, (5, 5, 5, 5)))
        robot.move_joints(newJointAngles)
        print("Joint angles after increase: {}".format(robot.joint_angles))

        newJointAngles = tuple(np.subtract(robot.joint_angles, (5, 5, 5, 5)))
        robot.move_joints(newJointAngles)
        print("Joint angles after decrease: {}".format(robot.joint_angles))

        # # Move backward and forward
        print("Moving backward and forward ...")
        robot.move_linear((-20, 0, 0, 0, 0, 0))
        robot.move_linear((0, 0, 0, 0, 0, 0))

        # Move right and left
        print("Moving right and left ...")
        robot.move_linear((0, -20, 0, 0, 0, 0))
        robot.move_linear((0, 0, 0, 0, 0, 0))

        # Move down and up
        print("Moving down and up ...")
        robot.move_linear((0, 0, -20, 0, 0, 0))
        robot.move_linear((0, 0, 0, 0, 0, 0))

        # ---- Note that rolling is not possible on a 4dof robot and will return an error
        # Roll right and left
        # print("Rolling right and left ...")
        # robot.move_linear((0, 0, 0, 20, 0, 0))
        # robot.move_linear((0, 0, 0, 0, 0, 0))

        # # Roll forward and backward
        # print("Rolling forward and backward ...")
        # robot.move_linear((0, 0, 0, 0, 20, 0))
        # robot.move_linear((0, 0, 0, 0, 0, 0))
        # ----

        # # Turn clockwise and anticlockwise around work frame z-axis
        print("Turning clockwise and anticlockwise around work frame z-axis ...")
        robot.move_linear((0, 0, 0, 0, 0, -100))
        robot.move_linear((0, 0, 0, 0, 0, 0))

        # Print Pose in this position
        print("pose in work frame: {}".format(robot.pose))
        # Print joint angles in this position
        print("joint angles: {}".format(robot.joint_angles))

        # ---- Note that circular trajectories are not yet implemented
        # # Make a circular move down/up, via a point on the right/left
        # print("Making a circular move down and up, via a point on the right/left ...")
        # robot.blend_radius = 10
        # robot.move_circular((0, 20, 20, 0, 0, 0), (0, 0, 40, 0, 0, 0))
        # robot.blend_radius = 0
        # robot.move_circular((0, -20, 20, 0, 0, 0), (0, 0, 0, 0, 0, 0))
        # ----

        # Move to offset pose then tap down and up in sensor frame
        print("Moving to 20 mm/deg offset in all pose dimensions ...")
        robot.move_linear((-20, -20, -20, 0, 0, -20))
        print("Pose after offset move: {}".format(robot.pose))
        # THIS MOVEMENT ON THE DOBOT ARM IS UP THEN DOWN ->> CHECK WITH JOHN IF IMPORTANT :) !
        print("Tapping down and up ...")
        robot.coord_frame = base_frame
        robot.coord_frame = robot.pose
        robot.move_linear((0, 0, -20, 0, 0, 0))
        robot.move_linear((0, 0, 0, 0, 0, 0))
        robot.coord_frame = work_frame
        print("Moving to origin of work frame ...")
        robot.move_linear((0, 0, 0, 0, 0, 0))

        # ---- Note that blend radii are not yet implemented
        # # Increase blend radius and move through a sequence of waypoints
        # print("Increasing blend radius and moving through a sequence of waypoints ...")
        # robot.blend_radius = 20
        # print("Moving to first waypoint ...")
        # robot.move_linear((100, 0, 0, 0, 0, 0))
        # print("Moving to second waypoint ...")
        # robot.move_linear((100, 100, 0, 0, 0, 0))
        # robot.blend_radius = 0
        # print("Moving to final destination ...")
        # robot.move_linear((100, 100, 100, 0, 0, 0))
        # print("Moving to origin of work frame ...")
        # robot.move_linear((0, 0, 0, 0, 0, 0))
        # print("Final pose in work frame: {}".format(robot.pose))
        # ----

        # Pause before commencing asynchronous tests
        print("Waiting for 5 secs ...")
        time.sleep(5)
        print("Repeating test sequence for asynchronous moves ...")

        # Increase and decrease all joint angles (async)
        print("Increasing and decreasing all joint angles ...")

        newJointAngles = tuple(np.add(robot.joint_angles, (5, 5, 5, 5)))
        robot.async_move_joints(newJointAngles)
        print("Getting on with something else while command completes ...")
        robot.async_result()
        print("Joint angles after increase: {}".format(robot.joint_angles))

        newJointAngles = tuple(np.subtract(robot.joint_angles, (5, 5, 5, 5)))
        robot.async_move_joints(newJointAngles)
        print("Getting on with something else while command completes ...")
        robot.async_result()
        print("Joint angles after decrease: {}".format(robot.joint_angles))

        # Move backward and forward (async)
        print("Moving backward and forward (async) ...")
        robot.async_move_linear((-20, 0, 0, 0, 0, 0))
        print("Getting on with something else while command completes ...")
        robot.async_result()
        robot.async_move_linear((0, 0, 0, 0, 0, 0))
        print("Getting on with something else while command completes ...")
        robot.async_result()

        # Move right and left
        print("Moving right and left (async) ...")
        robot.async_move_linear((0, -20, 0, 0, 0, 0))
        print("Getting on with something else while command completes ...")
        robot.async_result()
        robot.async_move_linear((0, 0, 0, 0, 0, 0))
        print("Getting on with something else while command completes ...")
        robot.async_result()

        # Move down and up (async)
        print("Moving down and up (async) ...")
        robot.async_move_linear((0, 0, -20, 0, 0, 0))
        print("Getting on with something else while command completes ...")
        robot.async_result()
        robot.async_move_linear((0, 0, 0, 0, 0, 0))
        print("Getting on with something else while command completes ...")
        robot.async_result()

        # ---- Note that rolling is not possible on a 4dof robot and will return an error
        # # Roll right and left (async)
        # print("Rolling right and left (async) ...")
        # robot.async_move_linear((0, 0, 0, 20, 0, 0))
        # print("Getting on with something else while command completes ...")
        # robot.async_result()
        # robot.async_move_linear((0, 0, 0, 0, 0, 0))
        # print("Getting on with something else while command completes ...")
        # robot.async_result()

        # # Roll forward and backward (async)
        # print("Rolling forward and backward (async) ...")
        # robot.async_move_linear((0, 0, 0, 0, 20, 0))
        # print("Getting on with something else while command completes ...")
        # robot.async_result()
        # robot.async_move_linear((0, 0, 0, 0, 0, 0))
        # print("Getting on with something else while command completes ...")
        # robot.async_result()
        # ----

        # Turn clockwise and anticlockwise around work frame z-axis (async)
        print("Turning clockwise and anticlockwise around work frame z-axis (async) ...")
        robot.async_move_linear((0, 0, 0, 0, 0, -20))
        print("Getting on with something else while command completes ...")
        robot.async_result()
        robot.async_move_linear((0, 0, 0, 0, 0, 0))
        print("Getting on with something else while command completes ...")
        robot.async_result()

        # ---- Note that circular trajectories are not yet implemented
        # # Make a circular move down/up, via a point on the right/left
        # print("Making a circular move down and up, via a point on the right/left (async) ...")
        # robot.blend_radius = 10
        # robot.async_move_circular((0, 20, 20, 0, 0, 0), (0, 0, 40, 0, 0, 0))
        # print("Getting on with something else while command completes ...")
        # robot.async_result()
        # robot.blend_radius = 0
        # robot.async_move_circular((0, -20, 20, 0, 0, 0), (0, 0, 0, 0, 0, 0))
        # print("Getting on with something else while command completes ...")
        # robot.async_result()
        # ----

        # Move to offset pose then tap down and up in sensor frame (async)
        print("Moving to 20 mm/deg offset in all pose dimensions (async) ...")
        robot.async_move_linear((20, 20, 20, 0, 0, 20))
        print("Getting on with something else while command completes ...")
        robot.async_result()
        print("Pose after offset move: {}".format(robot.pose))
        print("Tapping down and up (async) ...")
        robot.coord_frame = base_frame
        robot.coord_frame = robot.pose
        robot.async_move_linear((0, 0, -20, 0, 0, 0))
        print("Getting on with something else while command completes ...")
        robot.async_result()
        robot.async_move_linear((0, 0, 0, 0, 0, 0))
        print("Getting on with something else while command completes ...")
        robot.async_result()
        robot.coord_frame = work_frame
        print("Moving to origin of work frame ...")
        robot.async_move_linear((0, 0, 0, 0, 0, 0))
        print("Getting on with something else while command completes ...")
        robot.async_result()

        # ---- Note that blend radii are not yet implemented
        # # Increase blend radius and move through a sequence of waypoints (async)
        # print("Increasing blend radius and moving through a sequence of waypoints ...")
        # robot.blend_radius = 20
        # print("Moving to first waypoint ...")
        # robot.async_move_linear((100, 0, 0, 0, 0, 0))
        # print("Getting on with something else while command completes ...")
        # robot.async_result()
        # print("Moving to second waypoint ...")
        # robot.async_move_linear((100, 100, 0, 0, 0, 0))
        # print("Getting on with something else while command completes ...")
        # robot.async_result()
        # robot.blend_radius = 0
        # print("Moving to final destination ...")
        # robot.async_move_linear((100, 100, 100, 0, 0, 0))
        # print("Getting on with something else while command completes ...")
        # robot.async_result()
        # print("Moving to origin of work frame ...")
        # robot.async_move_linear((0, 0, 0, 0, 0, 0))
        # print("Getting on with something else while command completes ...")
        # robot.async_result()
        # ----

        print("Final pose in work frame: {}".format(robot.pose))


if __name__ == '__main__':
    main()
