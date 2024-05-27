#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

import time

import meshcat_shapes
import pinocchio as pin
from meshcat import transformations
from pinocchio.visualize import MeshcatVisualizer

import upkie_description

RADIUS_PER_KG = 0.01  # [m] / [kg]

if __name__ == "__main__":
    robot = upkie_description.load_in_pinocchio(
        # NB: we want a free-flyer in this example, otherwise the torso will be
        # attached to the "universe" frame and its mass will not be counted in
        # pin.computeTotalMass and pin.centerOfMass calculations
        root_joint=pin.JointModelFreeFlyer()
    )

    robot.setVisualizer(MeshcatVisualizer())
    robot.initViewer(open=True)
    robot.loadViewerModel(color=[1.0, 1.0, 1.0, 0.3])
    robot.display(robot.q0)
    viewer = robot.viz.viewer

    com = pin.centerOfMass(robot.model, robot.data, robot.q0)
    meshcat_shapes.point(viewer["com"], radius=0.05, color=0xFF0000)
    viewer["com"].set_transform(transformations.translation_matrix(com))

    time.sleep(1.0)  # avoid terminating too fast
