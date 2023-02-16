from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveDifferential, SpeedRPM
from ev3dev2.wheel import EV3Tire, Wheel
from math import pi
class MyWheel(Wheel):
    def __init__(self):
        super(MyWheel, self).__init__(68.8, 36)

def coordinator():    
    STUD_MM = 8
    # test with a robot that:
    # - uses the custom wheel MyWheel
    # - wheels are 18 studs apart
    mdiff = MoveDifferential(OUTPUT_A, OUTPUT_D, MyWheel, 18 * STUD_MM)

    # Rotate 90 degrees clockwise
    mdiff.turn_right(SpeedRPM(40), 90)

    # Drive forward 500 mm
    #mdiff.on_for_distance(SpeedRPM(40), 500)

    # Drive in arc to the right along an imaginary circle of radius 150 mm.
    # Drive for 700 mm around this imaginary circle.
    mdiff.on_arc_right(SpeedRPM(80), 300, 700)
'''
    # Enable odometry
    mdiff.odometry_start()

    # Use odometry to drive to specific coordinates
    mdiff.on_to_coordinates(SpeedRPM(40), 300, 300)

    # Use odometry to go back to where we started
    mdiff.on_to_coordinates(SpeedRPM(40), 0, 0)

    # Use odometry to rotate in place to 90 degrees
    mdiff.turn_to_angle(SpeedRPM(40), 90)

    # Disable odometry
    mdiff.odometry_stop()
'''