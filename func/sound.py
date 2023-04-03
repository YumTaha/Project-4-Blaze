from ev3dev2.sound import Sound
def play_sound(string): sound = Sound(); sound.speak(string)
def beep(): sound = Sound(); sound.beep()