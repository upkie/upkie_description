#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

import time

import meshcat_shapes
import numpy as np
import pinocchio as pin
import upkie_description
from meshcat import transformations
from pinocchio.visualize import MeshcatVisualizer


def com_manual(robot: pin.RobotWrapper, visualize: bool = True):
    total_mass = 0.0
    total_com = np.zeros(3)
    for frame_id, frame in enumerate(robot.model.frames):
        if frame.name == "universe":
            continue
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
            meshcat_shapes.point(handle["com"], radius=0.01, color=0xFF0000)
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
    com_2 = com_manual(robot, visualize=False)
    meshcat_shapes.point(viewer["com_1"], radius=0.05, color=0xFF0000)
    meshcat_shapes.point(viewer["com_2"], radius=0.05, color=0x00FF00)
    viewer["com_1"].set_transform(transformations.translation_matrix(com_1))
    viewer["com_2"].set_transform(transformations.translation_matrix(com_2))

    time.sleep(1.0)  # avoid terminating too fast
