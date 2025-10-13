#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron
# Copyright 2024 Inria

"""URDF description for the Upkie wheeled biped."""

from .paths import MESHES_PATH, PATH, URDF_PATH

__version__ = "2.2.0"

__all__ = [
    "MESHES_PATH",
    "PATH",
    "URDF_PATH",
]

try:
    from .load_in_pinocchio import load_in_pinocchio  # noqa

    __all__.append("load_in_pinocchio")
except ImportError:
    pass


try:
    from .load_in_pybullet import load_in_pybullet  # noqa

    __all__.append("load_in_pybullet")
except ImportError:
    pass
