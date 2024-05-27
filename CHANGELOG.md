# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added

- Example to display the center of mass
- Filter frame names in frame display example

### Changed

- Increase velocity and torque limits to motor specs

## [1.5.0] - 2024-02-20

### Changed

- Shorten source headers using SPDX license identifiers
- Update project links

### Fixed

- Make Pinocchio an optional dependency

## [1.4.0] - 2023-07-19

### Added

- Summary of joint limits in the README

### Changed

- Hip position and velocity limits
- IMU orientation to be consistent with assembly instructions
- Knee position and velocity limits
- Wheel velocity limits

## [1.3.0] - 2023-04-05

### Added

- Example: display joint frames from the URDF description
- Example: load Upkie in Pinocchio

### Changed

- Update velocity limits to more reasonable values

## [1.2.0] - 2023-03-14

### Added

- Example: display frames from the URDF description
- Function to load the description directly in Pinocchio

### Fixed

- Orientation of the IMU frame (thanks to @G-Levine)

## [1.1.1] - 2023-02-13

### Changed

- Rename "chassis" to "torso"

## [1.1.0] - 2022-05-23

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

## [1.0.0] - 2022-03-17

Initial robot description.

### Added

- Mesh files for the legs, wheel tire and mjbots parts
- ROS build and package files
- Robot description (kinematics, inertias, collisions) in URDF
- Scripts to compute box and cylinder inertias

[unreleased]: https://github.com/upkie/upkie_description/compare/v1.5.0...HEAD
[1.5.0]: https://github.com/upkie/upkie_description/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/upkie/upkie_description/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/upkie/upkie_description/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/upkie/upkie_description/compare/v1.1.1...v1.2.0
[1.1.1]: https://github.com/upkie/upkie_description/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/upkie/upkie_description/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/upkie/upkie_description/releases/tag/v1.0.0
