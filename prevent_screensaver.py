import argparse
import time
from pynput.mouse import Controller, Button

def move_mouse(interval):
    mouse = Controller()
    try:
        while True:
            # Get the current mouse position
            pos = mouse.position
            # Move the mouse to a slightly different position
            mouse.move(50, 0)
            time.sleep(0.1)  # Small delay to ensure the move is registered
            mouse.move(-50, 0)
            # Sleep for the specified interval
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Script terminated by user.")

def main():
    parser = argparse.ArgumentParser(description="Prevent screensaver by moving the mouse.")
    parser.add_argument("interval", type=float, help="Interval in seconds between mouse movements.")
    args = parser.parse_args()

    move_mouse(args.interval)

if __name__ == "__main__":
    main()

