#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron

"""
Compute the inertia matrix of a box and print it as URDF.

Source:
    https://en.wikipedia.org/wiki/List_of_moments_of_inertia#List_of_3D_inertia_tensors
"""

import argparse
import sys


def parse_command_line_arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mass", type=float, help="total mass in [kg]")
    parser.add_argument(
        "l_x", type=float, help="box length in [m] along the x-axis"
    )
    parser.add_argument(
        "l_y", type=float, help="box length in [m] along the y-axis"
    )
    parser.add_argument(
        "l_z", type=float, help="box length in [m] along the z-axis"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_command_line_arguments()
    mass, l_x, l_y, l_z = args.mass, args.l_x, args.l_y, args.l_z
    ixx = mass / 12.0 * (l_y ** 2 + l_z ** 2)
    iyy = mass / 12.0 * (l_x ** 2 + l_z ** 2)
    izz = mass / 12.0 * (l_x ** 2 + l_y ** 2)
    print(f'<box size="{l_x} {l_y} {l_z}" />')
    print(f'<mass value="{mass}" />')
    print(f"\n<!-- {' '.join(sys.argv)} -->")
    print(
        f'<inertia ixx="{ixx}" ixy="0" ixz="0" '
        f'iyx="0" iyy="{iyy}" iyz="0" '
        f'izx="0" izy="0" izz="{izz}" />'
    )
