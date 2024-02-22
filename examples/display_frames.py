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

import argparse
import time

import meshcat_shapes
import numpy as np
import upkie_description
from meshcat import transformations
from pinocchio.visualize import MeshcatVisualizer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--only",
        help="only display frames whose names contain a given string",
    )
    parser.add_argument(
        "--frame-scale",
        type=float,
        default=1.0,
        help="scaling factor applied to all frames",
    )
    args = parser.parse_args()

    robot = upkie_description.load_in_pinocchio()
    robot.setVisualizer(MeshcatVisualizer())
    robot.initViewer(open=True)
    robot.loadViewerModel(color=[1.0, 1.0, 1.0, 0.3])
    robot.display(robot.q0)
    viewer = robot.viz.viewer

    for frame in robot.model.frames:
        if frame.name == "universe" or (args.only and not args.only in frame.name):
            continue
        handle = viewer["pinocchio"]["visuals"][f"{frame.name}_0"]
        meshcat_shapes.frame(
            handle["frame"],
            axis_length=0.05 * args.frame_scale,
            axis_thickness=0.002 * args.frame_scale,
            opacity=0.8,
            origin_radius=0.005,
        )
        meshcat_shapes.textarea(
            handle["text"],
            text=frame.name,
            width=0.05,
            height=0.05,
            font_size=100,
        )
        Rx = transformations.rotation_matrix(0.5 * np.pi, [1.0, 0.0, 0.0])
        Rz = transformations.rotation_matrix(0.5 * np.pi, [0.0, 0.0, 1.0])
        trans = transformations.translation_matrix(
            [0.0, 0.0, 0.005 * args.frame_scale]
        )
        handle["text"].set_transform(trans @ Rz @ Rx)

    time.sleep(1.0)  # avoid terminating too fast
