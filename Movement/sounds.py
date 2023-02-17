from ev3dev2.sound import Sound

def beep():
    beep = Sound()
    beep.beep()
def speaker():
    sound = Sound()
    sound.speak('I am BLAZE')
def finished():
    sound = Sound()
    sound.speak('Done')