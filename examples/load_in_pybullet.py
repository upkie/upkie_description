#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Inria
#
# /// script
# dependencies = ["pin", "upkie_description"]
# ///

"""Load Upkie in PyBullet."""

import argparse

import pybullet

import upkie_description

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--variant",
        help="variant of the robot description to load",
    )
    args = parser.parse_args()

    gui = True
    pybullet_mode = pybullet.GUI if gui else pybullet.DIRECT
    pybullet.connect(pybullet.GUI)

    if gui:  # Disable scene during initialization
        pybullet.configureDebugVisualizer(pybullet.COV_ENABLE_GUI, 0)
        pybullet.configureDebugVisualizer(pybullet.COV_ENABLE_RENDERING, 0)
        pybullet.configureDebugVisualizer(pybullet.COV_ENABLE_SHADOWS, 0)

    label = "robot"
    if args.variant:
        label = f"'{args.variant}' variant of the robot"
    print(f"Loading {label} in PyBullet...")
    robot = upkie_description.load_in_pybullet(variant=args.variant)
    print(f"Robot loaded with ID {robot}")
    print("Run this example with ``python -i`` to interact with it")

    if gui:  # Enable GUI if it is requested
        pybullet.configureDebugVisualizer(pybullet.COV_ENABLE_RENDERING, 1)
        pybullet.configureDebugVisualizer(pybullet.COV_ENABLE_SHADOWS, 0)
        pybullet.resetDebugVisualizerCamera(
            cameraDistance=1.0,
            cameraYaw=45,
            cameraPitch=-30,
            cameraTargetPosition=[0, 0, 0.3],
        )

    pybullet.setRealTimeSimulation(True)
    for _ in range(100000):
        pybullet.stepSimulation()

    pybullet.disconnect()
