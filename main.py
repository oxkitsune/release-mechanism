import argparse
from typing import Literal

from controller import ReleaseController, MOTOR_MODEL, MOTOR_SERIAL_NUMBER
import time


def main():
    args = parse_args()

    print(f"Connecting to motor with serial: {args.serial}, model: {args.model}")
    controller = ReleaseController(tic_product_type=args.model, serial_no=args.serial)
    print("Enabling motor...")
    controller.enable_motor()

    print("Executing command:", args.command)
    if args.command == "open":
        controller.move_with_speed(30)
        time.sleep(2)
    elif args.command == "close":
        controller.move_with_speed(-30)
        time.sleep(2)
    else:
        print("Unknown command:", args.command)


def parse_args():
    parser = argparse.ArgumentParser(description="Open or close the release mechanism")
    parser.add_argument(
        "command", type=str, help="Command to run"
    )
    parser.add_argument(
        "--serial",
        type=str,
        help="Serial number of the motor",
        default=MOTOR_SERIAL_NUMBER,
    )
    parser.add_argument(
        "--model", type=str, help="Model number of the motor", default=MOTOR_MODEL
    )

    return parser.parse_args()


if __name__ == "__main__":
    main()
