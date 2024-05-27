#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

import time

import meshcat_shapes
import numpy as np
import pinocchio as pin
from meshcat import transformations
from pinocchio.visualize import MeshcatVisualizer

import upkie_description


def com_model_inertias(robot: pin.RobotWrapper, visualize: bool = True):
    total_mass = 0.0
    total_com = np.zeros(3)
    for joint_id, inertia in enumerate(robot.model.inertias):
        total_mass += inertia.mass
        transform_com_to_joint = pin.SE3(
            rotation=np.eye(3), translation=inertia.lever
        )
        transform_joint_to_world = robot.data.oMi[joint_id]
        transform_com_to_world = (
            transform_joint_to_world * transform_com_to_joint
        )
        total_com += inertia.mass * transform_com_to_world.translation
        if visualize:
            name = robot.model.names[joint_id]
            handle = viewer["pinocchio"]["joint_inertias"][name]
            meshcat_shapes.point(handle["com_mi"], radius=0.01, color=0x0000FF)
            handle["com_mi"].set_transform(transform_com_to_world.np)
    return total_com / total_mass


def com_manual(robot: pin.RobotWrapper, visualize: bool = True):
    total_mass = 0.0
    total_com = np.zeros(3)
    for frame_id, frame in enumerate(robot.model.frames):
        total_mass += frame.inertia.mass
        transform_com_to_frame = pin.SE3(
            rotation=np.eye(3), translation=frame.inertia.lever
        )
        transform_frame_to_world = robot.data.oMf[frame_id]
        transform_com_to_world = (
            transform_frame_to_world * transform_com_to_frame
        )
        total_com += frame.inertia.mass * transform_com_to_world.translation
        if visualize:
            handle = viewer["pinocchio"]["visuals"][f"{frame.name}_0"]
            meshcat_shapes.point(handle["com"], radius=0.01, color=0x00FF00)
            handle["com"].set_transform(transform_com_to_frame.np)
    return total_com / total_mass


if __name__ == "__main__":
    robot = upkie_description.load_in_pinocchio()

    robot.setVisualizer(MeshcatVisualizer())
    robot.initViewer(open=True)
    robot.loadViewerModel(color=[1.0, 1.0, 1.0, 0.3])
    robot.display(robot.q0)
    viewer = robot.viz.viewer

    pin.forwardKinematics(robot.model, robot.data, robot.q0)
    pin.updateFramePlacements(robot.model, robot.data)

    # com_1 = robot.com(robot.q0)
    com_1 = pin.centerOfMass(robot.model, robot.data, robot.q0)
    com_2 = com_manual(robot, visualize=True)
    com_3 = com_model_inertias(robot, visualize=True)
    meshcat_shapes.point(viewer["com_1"], radius=0.05, color=0xFF0000)
    meshcat_shapes.point(viewer["com_2"], radius=0.05, color=0x00FF00)
    meshcat_shapes.point(viewer["com_3"], radius=0.05, color=0x0000FF)
    viewer["com_1"].set_transform(transformations.translation_matrix(com_1))
    viewer["com_2"].set_transform(transformations.translation_matrix(com_2))
    viewer["com_3"].set_transform(transformations.translation_matrix(com_3))

    time.sleep(1.0)  # avoid terminating too fast
