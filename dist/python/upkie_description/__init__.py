#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
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
