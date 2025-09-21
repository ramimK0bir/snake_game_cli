from pynput import keyboard

def wait_for_key_press():
    pressed_key = None

    def on_press(key):
        nonlocal pressed_key
        pressed_key = key
        # Stop listener after first key press
        return False

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # This blocks until listener stops

    return pressed_key

def is_pressed(key) :
    key="Key."+key
    pressed_key = wait_for_key_press()
    print(f"pressed_key {str(pressed_key)}")
    if key==pressed_key :
        print("true")
        return True
