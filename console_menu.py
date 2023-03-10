#!/usr/bin/env python3

from time import sleep
from ev3dev2.button import Button
from ev3dev2.console import Console
from ev3dev2.led import Leds
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sound import Sound
from Movement.drive import drive, turn_degree
from Movement.sounds import welcome, beep



#ALL VARIABLES THAT YOU CAN CHANGE/ADD/DELETE
distance_cm = 10   # \
speed = 20         #  |=> YOU CAN CHANGE THESE VARIABLES
laps = 4           # /
degrees = 90       #/



'''
THIS CONSOLE IS ONLY FOR THE FIRST TASK (1a and 1b), EACH FUTURE TASK WILL HAVE A DIFFERENT CONSOLE
ONLY THE FINAL DEMO THAT WILL HAVE ALL FUNCTIONS INCLUDED
'''

# Function to reset console
def reset_console():
    console = Console()
    console.reset_console()
    print("")  # add a blank line for spacing


# Main function for printing instructions
def instructions():
    console = Console()
    console.reset_console()

    # Printing menu options
    print("Enter:Gyro \nReset")
    print("Up: Test1")
    print("Down: Test2")


#....#####.....######.........#....#....######....######.........######....######....#....#....######....#....#..
#....#....#....#....#.........##...#....#....#......##.............##......#....#....#....#....#.........#....#..
#....#....#....#....#.........#.#..#....#....#......##.............##......#....#....#....#....#.........######..
#....#....#....#....#.........#..#.#....#....#......##.............##......#....#....#....#....#.........#....#..
#....#####.....######.........#...##....######......##.............##......######....######....######....#....#..

"""
Used to create a console menu for switching between programs quickly
without having to return to Brickman to find and launch a program.
Demonstrates the EV3DEV2 Console(), Led(), and Button() classes.
"""


def get_positions(console):
    """
    Compute a dictionary keyed by button names with horizontal alignment,
    and column/row location to show each choice on the EV3 LCD console.
    Parameter:
    - `console` (Console): an instance of the EV3 Console() class
    returns a dictionary keyed by button names with column/row location
    """

    midrow = 1 + console.rows // 2
    midcol = 1 + console.columns // 2
    # horiz_alignment, col, row
    return {
        "up": ("C", midcol, 1),
        "right": ("R", console.columns, midrow),
        "down": ("C", midcol, console.rows),
        "left": ("L", 1, midrow),
        "enter": ("C", midcol, midrow)
    }

def wait_for_button_press(button):
    """
    Wait for a button to be pressed and released.
    Parameter:
    - `button` (Button): an instance of the EV3 Button() class
    return the Button name that was pressed.
    """
    pressed = None
    while True:
        allpressed = button.buttons_pressed
        if bool(allpressed):
            pressed = allpressed[0]  # just get the first one
            while not button.wait_for_released(pressed):
                pass
            break
    return pressed

def menu(choices, before_run_function=None, after_run_function=None):
    """
    Console Menu that accepts choices and corresponding functions to call.
    The user must press the same button twice: once to see their choice highlited,
    a second time to confirm and run the function. The EV3 LEDs show each state change:
    Green = Ready for button, Amber = Ready for second button, Red = Running
    Parameters:
    - `choices` a dictionary of tuples "button-name": ("mission-name", function-to-call)
        Example:
            choices = {
                # "button-name": ("mission-name", function-to-call)
                # or "button-name": ("mission-name", lambda: call(x, y, z))
                "enter": ("CAL", lambda: auto_calibrate(robot, 1.0)),
                "up": ("MI2", fmission2),
                "right": ("MI3", fmission3),
                "down": ("MI4", fmission4),
                "left": ("MI5", fmission5)
            }
        where fmission2, fmission3 are functions;
        note don't call them with parentheses, unless preceded by lambda: to defer the call
    - `before_run_function` when not None, call this function before each mission run, passed with mission-name
    - `after_run_function` when not None, call this function after each mission run, passed with mission-name
    """

    console = Console()
    leds = Leds()
    button = Button()

    leds.all_off()
    leds.set_color("LEFT", "GREEN")
    leds.set_color("RIGHT", "GREEN")
    menu_positions = get_positions(console)

    last = None  # the last choice--initialize to None

    while True:
        # display the menu of choices, but show the last choice in inverse
        console.reset_console()
        for btn, (name, _) in choices.items():
            align, col, row = menu_positions[btn]
            console.text_at(name, col, row, inverse=(btn == last), alignment=align)

        pressed = wait_for_button_press(button)

        # get the choice for the button pressed
        if pressed in choices:
            if last == pressed:   # was same button pressed?
                console.reset_console()
                leds.set_color("LEFT", "RED")
                leds.set_color("RIGHT", "RED")

                # call the user's subroutine to run the mission, but catch any errors
                try:
                    name, mission_function = choices[pressed]
                    if before_run_function is not None:
                        before_run_function(name)
                    mission_function()
                except Exception as ex:
                    print("**** Exception when running")
                    print(ex)
                finally:
                    if after_run_function is not None:
                        after_run_function(name)
                    last = None
                    leds.set_color("LEFT", "GREEN")
                    leds.set_color("RIGHT", "GREEN")
            else:   # different button pressed
                last = pressed
                leds.set_color("LEFT", "AMBER")
                leds.set_color("RIGHT", "AMBER")

if __name__ == "__main__":

    # This is the main program to demonstrate the console menu logic above.
    #
    # Define functions that represent different missions
    # Note: these can be imported from different modules (files)
    # and use lambda notation to defer the function call
    # i.e. lambda : call(a, b, c)

    welcome() # Speak welcome message
    instructions() # show menu options



    def reset_sensors():
        
        console = Console()
        console.reset_console()
        
        """ Reset values of any connected gyro sensor """
        for port in [INPUT_1, INPUT_2, INPUT_3, INPUT_4]:
            try:
                sensor = GyroSensor(port)
                sensor.reset()
                print("Gyro reset".format(port))
                sleep(1)
            except:
                pass
        
                
    def comingsoon():
        pass


    def testing():

        inch = 12 # The initial 12 inch the robot should move tp
        cm = inch * 2.54 # Converted to cm
        einch = 96 # The distance that varies between each test
        ecm = einch * 2.54 # Converted to cm

        # The movement
        drive(cm, speed, direction='forward')
        turn_degree(degrees, speed, direction='right')
        drive(ecm, speed, direction='forward')


    def testing2():

        inch = 12 # The distance that varies between each test
        cm = inch * 2.54 # Converted to cm

        # The movement
        drive(cm, speed, direction='forward')


    # Define the functions to be called before and after each run.
    # Functions will be called with the mission_name as the argument.
    # Useful for resetting motor positions between runs, etc.

    def before(mission_name):
        sound = Sound()
        sound.speak("starting " + mission_name)
        beep()
        reset_console()
    
    def after(mission_name):
        sound = Sound()
        sound.speak(mission_name + " complete")
        beep()
        instructions()

    # Define the buttons, mission names, functions for the console menu.
    # Key is the button assignment: one of "enter", "up", "right", "down", "left"
    # Note the "backspace" button interrupts the program and returns to Brickman
    # Example:
    # CHOICES = {
    #     # "button-name": ("mission-name", function-to-call)
    #     # or "button-name": ("mission-name", lambda: call(x, y, z))
    #     "up": ("MI1", mission1),
    #     "right": ("MI2", mission2),
    #     "left": ("MI3", mission3),
    #     "down": ("SHOW", lambda: show_sensors(5)),
    #     "enter": ("CAL", calibrate)
    # }
    # menu(CHOICES, before_run_function=before, after_run_function=after)

    CHOICES = {
        "up": ("test1", testing),
        "right": ("MI2", comingsoon),
        "left": ("MI3", comingsoon),
        "down": ("test2", testing2),
        "enter": ("Reset Gyroscope", reset_sensors)
    }

    

    instructions()
    menu(CHOICES, before_run_function=before, after_run_function=after)

#END OF CODE
    