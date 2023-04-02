from ev3dev2.sound import Sound

def play_sound(filename):
    sound = Sound()
    sound.play('sounds/{}'.format(filename))
