from pydub.playback import _play_with_simpleaudio as play
from pynput import keyboard

from switch import Switch, Switch_Type

sound = None

# keyboard listener functions
def on_press(key):
    global sound
    play(sound)


def on_press_debug(key):
    try:
        print("alphanumeric key {0} pressed".format(key.char))
    except AttributeError:
        print("special key {0} pressed".format(key))


def on_release(key):
    if key == keyboard.Key.esc:  # stop listener
        return False

def main():
    global sound
    switch = Switch(switch_type=Switch_Type.GX_BLUE)  # I'm about to end my girlfriend ears
    sound = switch.getsound()
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()



if __name__ == "__main__":
    main()
