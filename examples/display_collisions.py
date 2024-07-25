#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Inria

"""
Display all frames from the robot description.

This example relies on the following dependencies:

- `MeshCat <https://github.com/rdeits/meshcat-python>`_
- `meshcat-shapes <https://github.com/stephane-caron/meshcat-shapes>`_
- `Pinocchio <https://github.com/stack-of-tasks/pinocchio>`_
"""

import time

import upkie_description
from pinocchio.visualize import MeshcatVisualizer

FRAME_SCALE = 1.0

if __name__ == "__main__":
    robot = upkie_description.load_in_pinocchio(with_camera=True)
    robot.setVisualizer(MeshcatVisualizer())
    robot.initViewer(open=True)
    robot.loadViewerModel(collision_color=(1.0, 0.0, 0.0, 0.3))
    robot.viz.displayCollisions(True)
    robot.display(robot.q0)
    time.sleep(1.0)  # avoid terminating too fast
