from pynput import keyboard

pressed_keys = set()

def on_press(key):
    pressed_keys.add(key)

def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

def is_pressed(key_name):
    # Convert string like "space" to pynput Key or character
    from pynput.keyboard import Key
    try:
        key = getattr(Key, key_name)
    except AttributeError:
        # Not a special key, check char key
        key = key_name

    return key in pressed_keys

