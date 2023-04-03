#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2023 Inria
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Display joint frames from the robot description.

This example relies on the following dependencies:

- `MeshCat <https://github.com/rdeits/meshcat-python>`_
- `meshcat-shapes <https://github.com/stephane-caron/meshcat-shapes>`_
- `Pinocchio <https://github.com/stack-of-tasks/pinocchio>`_
"""

import argparse
import time

import meshcat_shapes
import numpy as np
import pinocchio as pin
import upkie_description
from meshcat import transformations
from pinocchio.visualize import MeshcatVisualizer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--only",
        help="only display the frame with this name",
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

    model = robot.model
    data = robot.data
    q = pin.neutral(model)
    pin.forwardKinematics(model, data, q)

    for index, name in enumerate(model.names):
        joint_id = model.getJointId(name)
        joint = model.joints[joint_id]
        joint_placement = model.jointPlacements[joint_id]
        handle = viewer["pinocchio"]["joints"][name]
        handle.set_transform(data.oMi[joint_id].np)
        meshcat_shapes.frame(
            handle["frame"],
            axis_length=0.05 * args.frame_scale,
            axis_thickness=0.002 * args.frame_scale,
            opacity=0.8,
            origin_radius=0.005,
        )
        meshcat_shapes.textarea(
            handle["text"],
            text=name,
            width=0.05,
            height=0.05,
            font_size=150,
        )
        Rx = transformations.rotation_matrix(0.5 * np.pi, [1.0, 0.0, 0.0])
        Rz = transformations.rotation_matrix(0.5 * np.pi, [0.0, 0.0, 1.0])
        trans = transformations.translation_matrix(
            [0.0, 0.0, 0.005 * args.frame_scale]
        )
        handle["text"].set_transform(trans @ Rz @ Rx)

    time.sleep(1.0)  # avoid terminating too fast
