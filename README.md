# Upkie wheeled biped robot

<img src="https://user-images.githubusercontent.com/1189580/169594012-2d685579-2b66-4470-9def-57bd0656b420.png" align="right" width="300">

URDF description for the [Upkie](https://hackaday.io/project/185729-upkie-wheeled-biped-robot) wheeled biped. 

## Python module

The description can be loaded directly in various Python robotics frameworks, for instance:

```python
import upkie_description

robot = upkie_description.load_in_pinocchio()
```

Check out the [Python README](dist/python/README.md) for more details.

## Joint limits

| Joint | Limit    | Value (±) | Unit |
|-------|----------|-----------|------|
| Hip   | Position | 0.2       | rev  |
| Hip   | Velocity | 2         | rps  |
| Hip   | Torque   | 10        | Nm   |
| Knee  | Position | 0.4       | rev  |
| Knee  | Velocity | 2         | rps  |
| Knee  | Torque   | 10        | Nm   |
| Wheel | Position | -         | -    |
| Wheel | Velocity | 8         | rps  |
| Wheel | Torque   | 1         | Nm   |

## See also

- [3D printed parts](https://github.com/tasts-robots/upkie_parts)
- [Upkie's software](https://github.com/tasts-robots/upkie)

## License

Upkie's torso derives from the chassis of the [mjbots quad](https://github.com/mjbots/quad). The Apache 2.0 license applies to all files in this repository, to the exception of the [wheel\_tire](meshes/wheel_tire) mesh which is under the CC BY 4.0 license. Meshes from [mjbots](meshes/mjbots) are also Apache 2.0. See the files in their respective folders for more details.
