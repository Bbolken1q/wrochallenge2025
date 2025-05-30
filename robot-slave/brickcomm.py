from console import debug_print
import rpyc # type: ignore
from time import sleep


conn = rpyc.classic.connect('192.168.0.2', port=42069)

ev3dev2_motor = conn.modules['ev3dev2.motor']

brick_sensors_motor = ev3dev2_motor.MediumMotor(ev3dev2_motor.OUTPUT_B)
brick_gate_motor = ev3dev2_motor.LargeMotor(ev3dev2_motor.OUTPUT_A)

brick_sensors_motor.run_timed(time_sp=1000, speed_sp=600)

# sensors_motor.turn_to_angle(speed=100, angle_target_degrees=60, error_margin=1)