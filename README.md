
# Crazyflie Drone Keyboard Control

This Python script allows you to control a Crazyflie drone using your keyboard. It is designed to provide basic movement controls such as forward, backward, left, right, up, down, and rotation.

## Prerequisites

Before you start, ensure that you have the following requirements met:

- Crazyflie drone set up and ready to connect
- The Crazyflie Python library `cflib` installed
- The `pynput` library installed to capture keyboard inputs

You can install the required Python libraries using pip:

```bash
pip install cflib pynput
```

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/magnaprog/crazyflie-keyboard-controller.git
```

2. Navigate to the cloned repository:

```bash
cd crazyflie-keyboard-controller
```

## Usage

1. Make sure the Crazyflie drone is turned on and the Crazyradio PA USB dongle is inserted into your computer.

2. Run the script:

```bash
python keyboard_control.py
```

3. Once the script is running, use the following keys to control the drone:

- `w`: Move forward
- `s`: Move backward
- `a`: Move left
- `d`: Move right
- `q`: Rotate left
- `e`: Rotate right
- `r`: Move up
- `f`: Move down
- `ESC`: Exit the script

## Safety and Disclaimer

Ensure you have enough space to safely fly the Crazyflie drone. It's recommended to use a large, open area free from obstacles. The author is not responsible for any damage caused by using this script. Always prioritize safety and use at your own risk.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to the Bitcraze team for the fantastic Crazyflie drone and the comprehensive API.
- Thanks to the developers of the `pynput` library for providing a straightforward way to capture keyboard events.
