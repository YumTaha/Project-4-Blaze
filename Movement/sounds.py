from ev3dev2.sound import Sound

def beep():
    beep = Sound()
    beep.beep()

def welcome():
    sound = Sound()
    sound.speak("Hey, this is Blaze", volume=100)