#!/usr/bin/python

"""Code for transmitting bytes from RPi to Arduino via i2c.
Used for motor controlling. Author: aijat"""

# **CONNECTIONS** SDA: RPi 3, Arduino A4. SCL: RPi 5, Arduino A5

import smbus
import time

def getchar():
    #Returns a single character from standard input
    import tty, termios, sys
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def write_motors(bus, address, hor_dir, ver_dir):
    """Write two bytes to the i2c for motors"""
    bus.write_i2c_block_data(address, hor_dir, [ver_dir])
    print("Sent to the first servo: " + str(hor_dir))
    print("Sent to the second servo: " + str(ver_dir))


def main():
    """Run the main program"""
    bus = smbus.SMBus(1)
    address = 0x09
    run = True

    while run:
        """0: smaller angle, 1: do nothing, 2: bigger angle"""
        hor_dir = 1
        ver_dir = 1

        ch = getchar()
        if ch == 'a':
            hor_dir = 0
        elif ch == 'd':
            hor_dir = 2
        else:
            hor_dir = 1

        if ch == 's':
            ver_dir = 2
        elif ch == 'w':
            ver_dir = 0
        else:
            ver_dir = 1
        if ch == 'p':
            run = False
        write_motors(bus, address, hor_dir, ver_dir)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
