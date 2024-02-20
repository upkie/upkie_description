#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Inria

"""Load Upkie in Pinocchio."""

import upkie_description

if __name__ == "__main__":
    print("Loading robot in Pinocchio...")
    robot = upkie_description.load_in_pinocchio()
    print(f"{robot=}")
    print("Run this example with ``python -i`` to interact with it")
