# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

### Added

- Summary of joint limits in the README

### Changed

- Hip position and velocity limits
- IMU orientation to be consistent with assembly instructions
- Knee position and velocity limits
- Wheel velocity limits

## [1.3.0] - 2023/04/05

### Added

- Example: display joint frames from the URDF description
- Example: load Upkie in Pinocchio

### Changed

- Update velocity limits to more reasonable values

## [1.2.0] - 2023/03/14

### Added

- Example: display frames from the URDF description
- Function to load the description directly in Pinocchio

### Fixed

- Orientation of the IMU frame (thanks to @G-Levine)

## [1.1.1] - 2023/02/13

### Changed

- Rename "chassis" to "torso"

## [1.1.0] - 2022/05/23

### Added

- Build file to use the model in Bazel projects
- Illustration to the README
- Link to the mjbots quad chassis
- Python distribution of the model

### Changed

- Relicense the project to Apache 2.0
- Turn IMU 180 degrees around the base yaw axis

### Fixed

- Cleaned dangling Bazel reference to ``//tools/lint``
- Links to Printables.com
- Project name for CMake

## [1.0.0] - 2022/03/17

Initial robot description.

### Added

- Mesh files for the legs, wheel tire and mjbots parts
- ROS build and package files
- Robot description (kinematics, inertias, collisions) in URDF
- Scripts to compute box and cylinder inertias
