from InquirerPy import inquirer, prompt
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


def get_switch_type():
    switch_type = Switch_Type.GX_BLUE
    input_options = prompt([
        {
            "type": "list",
            "name": "type",
            "message": "Pick your favourite switch",
            "choices": [switch.name for switch in list(Switch_Type)]
        }
    ])

    switch_type = Switch_Type[input_options.get("type")]
    return switch_type


def main():
    global sound
    switch_type = get_switch_type()
    switch = Switch(switch_type=switch_type)  # I'm about to end my girlfriend ears
    sound = switch.getsound()
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()
