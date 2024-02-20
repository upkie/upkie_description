#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron
# Copyright 2024 Inria

"""
URDF description for the Upkie wheeled biped.
"""

from .load_in_pinocchio import load_in_pinocchio
from .paths import meshes_path, path, urdf_path

__version__ = "1.4.0"

__all__ = [
    "load_in_pinocchio",
    "meshes_path",
    "path",
    "urdf_path",
]
