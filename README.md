# Upkie wheeled biped robot

<img src="https://user-images.githubusercontent.com/1189580/169594012-2d685579-2b66-4470-9def-57bd0656b420.png" align="right" width="300">

[![Documentation](https://img.shields.io/badge/docs-read-brightgreen?logo=read-the-docs&style=flat)](https://github.com/upkie/upkie_description/wiki)
[![Conda version](https://anaconda.org/conda-forge/upkie_description/badges/version.svg)](https://anaconda.org/conda-forge/upkie_description)
[![PyPI version](https://img.shields.io/pypi/v/upkie_description)](https://pypi.org/project/upkie_description/)
[![Chat](https://img.shields.io/badge/matrix-chat-%234eb899)](https://app.element.io/#/room/#tasts-robots:matrix.org)

URDF description for the [Upkie](https://hackaday.io/project/185729-upkie-wheeled-biped-robot) wheeled biped. 

## Python module

The description can be loaded directly in various Python robotics frameworks, for instance:

```python
import upkie_description

robot = upkie_description.load_in_pinocchio()
```

Check out the [Python readme](dist/python/README.md) for more details.

## Joint limits

| Joint | Limit    | Value (±) | Unit  | Why? |
|-------|----------|-----------|-------|------|
| Hip   | Position | 1.26      | rad   | Geometry: cables fully stretched |
| Hip   | Velocity | 28.8      | rad/s | Derived from the [qdd100 spec](https://mjbots.com/products/qdd100-beta-3), see [below](#maximum-velocity-for-a-qdd100-at-18v) |
| Hip   | Torque   | 16.0      | Nm    | Peak torque (< 1 s) from the [qdd100 spec](https://mjbots.com/products/qdd100-beta-3) |
| Knee  | Position | 2.51      | rad   | Geometry: wheels touching hip actuators. |
| Knee  | Velocity | 28.8      | rad/s | Derived from the [qdd100 spec](https://mjbots.com/products/qdd100-beta-3), see [below](#maximum-velocity-for-a-qdd100-at-18v) |
| Knee  | Torque   | 16        | Nm    | Peak torque (< 1 s) from the [qdd100 spec](https://mjbots.com/products/qdd100-beta-3) |
| Wheel | Position | -         | -     | - |
| Wheel | Velocity | 785       | rad/s | Maximum velocity from the [mj5208 spec](https://mjbots.com/products/mj5208) |
| Wheel | Torque   | 1.7       | Nm    | Peak torque from the [mj5208 spec](https://mjbots.com/products/mj5208) |

### Maximum velocity for a qdd100 at 18 V

Peak velocities for the qdd100 are rated as 3,600 dps at 36 V and 2,300 dps at 24 V. Assuming a linear velocity-voltage relationship (which is a big assumption) leads to 1,650 dps at the 18 V of the [RYOBI batteries used on Upkie](https://github.com/upkie/upkie/wiki/Bill-of-materials), or equivalently 28.8 rad/s after conversion and rounding.

## See also

- [Upkie](https://github.com/upkie/upkie): main repository for the robot's hardware and software
- [3D printed parts](https://github.com/upkie/parts): CAD files and add-ons for the robot

## License

Upkie's torso derives from the chassis of the [mjbots quad](https://github.com/mjbots/quad). The Apache 2.0 license applies to all files in this repository, to the exception of the [wheel\_tire](meshes/wheel_tire) mesh which is under the CC BY 4.0 license. Meshes from [mjbots](meshes/mjbots) are also Apache 2.0. See the files in their respective folders for more details.
