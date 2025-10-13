#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Inria
#
# /// script
# dependencies = ["pin", "upkie_description", "ipython"]
# ///

"""Load Upkie in Pinocchio."""

import argparse

import IPython
import pinocchio as pin

import upkie_description

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--variant",
        help="variant of the robot description to load",
    )
    args = parser.parse_args()

    label = "robot"
    if args.variant:
        label = f"'{args.variant}' variant of the robot"
    print(f"Loading {label} in Pinocchio...")
    robot = upkie_description.load_in_pinocchio(
        # NB: we add a free-flyer so that the torso mass is included
        root_joint=pin.JointModelFreeFlyer(),
        variant=args.variant,
    )
    print(f"Robot description loaded to {robot=}\n")

    # Make sure we have an interpreter
    if IPython.get_ipython() is None:
        IPython.embed()
