from time import sleep
from pynput import keyboard
from datetime import datetime
import keyboard as kboard

keylog = []
words = {}
current_word = ''
prev_word = ''
line_position = 0

def log():
    global line_position

    with open('log.txt', 'a') as log:
        log.write(''.join(keylog))
        line_position += len(keylog)

        # new line if we're past 70 chars after the append
        if line_position >= 70:
            log.write('\n')
            line_position = 0

def on_press(key):
    global current_word
    global prev_word
    global words

    try:
        # print(str(key.char))

        if str(key.char) != 'None':
            keylog.append(str(key.char))

            if str(key.char).isalpha():
                current_word += str(key.char)
    except AttributeError:
        if(str(key)[4:] == 'space'):
            keylog.append(' ')
            # print(' ')

            if prev_word not in words:
                words[prev_word] = [current_word, '', '']
            else:
                words[prev_word].insert(0, current_word)
                words[prev_word].pop()

            print('Current word: ' + current_word)
            print('Word pair: ' + prev_word + ' ' + current_word)

            if current_word in words:
                print('Current pairings: ' + str(words[current_word]))
            else:
                print('No current pairings.')

            prev_word = current_word
            current_word = ''
        else:
            keylog.append('<' + str(key)[4:] + '>')
            # print('<' + str(key)[4:] + '>')
        
listener = keyboard.Listener(on_press=on_press)
listener.start()

def on_activate_1():
    global words
    global prev_word
    global current_word
    print('<ctrl>+<alt>+1 pressed')

    if prev_word in words:
        kboard.write(words[prev_word][0] + ' ')
        prev_word = current_word
        current_word = ''
    else:
        print('No word in 1 spot')
        print(prev_word)

def on_activate_2():
    global words
    global prev_word
    global current_word
    print('<ctrl>+<alt>+2 pressed')

    if prev_word in words and words[prev_word][1] != '':
        kboard.write(words[prev_word][1] + ' ')
        prev_word = current_word
        current_word = ''
    else:
        print('No word in 2 spot')
        print(prev_word)

def on_activate_3():
    global words
    global prev_word
    global current_word
    print('<ctrl>+<alt>+3 pressed')

    if prev_word in words and words[prev_word][2] != '':
        kboard.write(words[prev_word][2] + ' ')
        prev_word = current_word
        current_word = ''
    else:
        print('No word in 3 spot')
        print(prev_word)

hotkeys = keyboard.GlobalHotKeys({
         '<ctrl>+<alt>+1': on_activate_1,
         '<ctrl>+<alt>+2': on_activate_2,
         '<ctrl>+<alt>+3': on_activate_3})
hotkeys.start()


while '<esc>' not in keylog:
    log()
    keylog = []
    # print('keylog cleared')
    # print('collecting for 10 seconds')
    sleep(10)


    
