#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron

"""
Paths to the URDF description for the Upkie wheeled biped.
"""

import os

# Path to upkie_description
path = os.path.dirname(os.path.realpath(__file__))

# Path to the meshes folder
meshes_path = os.path.join(path, "meshes")

# Path to the robot's URDF
urdf_path = os.path.join(path, "urdf", "upkie.urdf")

__all__ = [
    "meshes_path",
    "path",
    "urdf_path",
]
