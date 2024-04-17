import logging
from pynput import keyboard
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.console import Console
from cflib.crazyflie.mem import MemoryElement
from cflib.crazyflie.syncLogger import SyncLogger
from cflib.crazyflie.mem import LighthouseMemHelper
from cflib.positioning.motion_commander import MotionCommander
from cflib.positioning.position_hl_commander import PositionHlCommander

# URI to the Crazyflie
URI = 'radio://0/80/2M/E7E7E7E7E7'

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)

def on_press(key):
    try:
        if key.char == 'w':
            # Forward
            mc.forward(0.5, velocity=0.5)
        elif key.char == 's':
            # Backward
            mc.back(0.5, velocity=0.5)
        elif key.char == 'a':
            # Left
            mc.left(0.5, velocity=0.5)
        elif key.char == 'd':
            # Right
            mc.right(0.5, velocity=0.5)
        elif key.char == 'q':
            # Rotate left
            mc.turn_left(45, rate=90)
        elif key.char == 'e':
            # Rotate right
            mc.turn_right(45, rate=90)
        elif key.char == 'r':
            # Move up
            mc.up(0.5, velocity=0.5)
        elif key.char == 'f':
            # Move down
            mc.down(0.5, velocity=0.5)
    except AttributeError:
        if key == keyboard.Key.esc:
            # Stop listener
            return False

if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
        with MotionCommander(scf) as mc:
            # Start the keyboard listener
            with keyboard.Listener(on_press=on_press) as listener:
                listener.join()
