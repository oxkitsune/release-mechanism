from ticlib import TicUSB
from tic import tic_constants, tic_setting_current_limit


from typing import Literal

MOTOR_SERIAL_NUMBER = "00362129"
MOTOR_MODEL = "T825"


class ReleaseController:
    # microstepping can be 1, 2, 4, 8, 16 or 32
    # max current in ampere
    # acceleration in mm/s/s
    def __init__(
        self,
        tic_product_type,
        acceleration: int = 100,
        microstepping: Literal[1, 2, 4, 8, 16, 32] = 32,
        current_limit: float = 1.5,
        serial_no: str = MOTOR_SERIAL_NUMBER,
    ):
        self.tic_product_type = tic_product_type
        self.tic = TicUSB(serial_number=serial_no)
        self.microstepping = microstepping

        self.tic.set_step_mode(
            tic_constants[f"TIC_STEP_MODE_MICROSTEP{self.microstepping}"]
        )
        self.tic.set_current_limit(
            tic_setting_current_limit(tic_product_type, current_limit)
        )

        tic_accel = self.__acceleration_convert(acceleration * 1000)
        self.tic.set_max_acceleration(tic_accel)
        self.tic.set_max_deceleration(tic_accel)

        self.tic.deenergize()
        self.tic.halt_and_set_position(0)

    def __speed_convert(self, micron_ps):
        return int(self.microstepping * micron_ps * 10000 / 4)

    def __acceleration_convert(self, micron_ps_ps):
        return int(self.microstepping * micron_ps_ps * 100 / 4)

    def enable_motor(self):
        self.tic.energize()
        self.tic.exit_safe_start()

    # speed in mm/s
    def move_with_speed(self, speed):
        tic_speed = self.__speed_convert(speed * 1000)
        # bug: direction of motor reverses above a speed of 100 for unknown reasons
        if abs(speed) >= 100:
            return False
        else:
            self.tic.set_max_speed(abs(tic_speed))
            self.tic.set_target_velocity(tic_speed)

    def stop(self):
        self.tic.deenergize()
