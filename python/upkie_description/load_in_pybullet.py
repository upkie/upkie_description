#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron
# Copyright 2023 Inria

"""Load Upkie description in PyBullet."""

import os

import pybullet

from .paths import PATH


def load_in_pybullet(variant: str = "", **kwargs) -> int:
    """Load a robot description in PyBullet.

    Args:
        variant (optional): Variant of the robot description to load,
            corresponding to the suffix of the URDF file. For example, set to
            "camera" to load ``upkie_camera.urdf``.
        kwargs: arguments passed to pybullet.loadURDF function, including:
            basePosition: 3D position of the base of the robot in world
                coordinates.
            baseOrientation: orientation in quaternion (xyzw) of the base of
                the robot in world coordinates.
            flags: int flags for the URDF loading in pybullet.
            useFixedBase: boolean indicating use a fix joint between world and
                robot base.
            physicsClientId: int indicating the pybullet client id.

    Returns:
        Integer identifier of the robot in PyBullet.
    """
    filename = f"upkie_{variant}.urdf" if variant else "upkie.urdf"
    urdf_path = os.path.join(PATH, "urdf", filename)
    pybullet.setAdditionalSearchPath(PATH)
    robot = pybullet.loadURDF(urdf_path, **kwargs)
    return robot
