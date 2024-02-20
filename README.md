# Upkie wheeled biped robot

<img src="https://user-images.githubusercontent.com/1189580/169594012-2d685579-2b66-4470-9def-57bd0656b420.png" align="right" width="300">

URDF description for the [Upkie](https://hackaday.io/project/185729-upkie-wheeled-biped-robot) wheeled biped. 

## Python module

The description can be loaded directly in various Python robotics frameworks, for instance:

```python
import upkie_description

robot = upkie_description.load_in_pinocchio()
```

Check out the [Python readme](dist/python/README.md) for more details.

## Joint limits

| Joint | Limit    | Value (±) | Unit | Why? |
|-------|----------|-----------|------|------|
| Hip   | Position | 0.2       | rev  | Cables fully stretched |
| Hip   | Velocity | 2         | rps  | Conservative, maximum rated velocity would be around 6 rps |
| Hip   | Torque   | 10        | Nm   | From the [qdd100 spec](https://mjbots.com/products/qdd100-beta-3) |
| Knee  | Position | 0.4       | rev  | Wheels touching hip actuators. |
| Knee  | Velocity | 2         | rps  | Conservative, maximum rated velocity would be around 6 rps |
| Knee  | Torque   | 10        | Nm   | From the [qdd100 spec](https://mjbots.com/products/qdd100-beta-3) |
| Wheel | Position | -         | -    | - |
| Wheel | Velocity | 8         | rps  | Conservative, maximum rated velocity [is 125 rps](https://mjbots.com/products/mj5208) |
| Wheel | Torque   | 1         | Nm   | Conservative, 60% of [peak torque](https://mjbots.com/products/mj5208) |

## See also

- [Upkie](https://github.com/upkie/upkie): main repository for the robot's hardware and software
- [3D printed parts](https://github.com/upkie/parts): CAD files and add-ons for the robot

## License

Upkie's torso derives from the chassis of the [mjbots quad](https://github.com/mjbots/quad). The Apache 2.0 license applies to all files in this repository, to the exception of the [wheel\_tire](meshes/wheel_tire) mesh which is under the CC BY 4.0 license. Meshes from [mjbots](meshes/mjbots) are also Apache 2.0. See the files in their respective folders for more details.
