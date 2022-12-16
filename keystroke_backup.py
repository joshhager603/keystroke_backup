from time import sleep
from pynput import keyboard
import keyboard as kboard

keylog = []
words = {}
current_word = ''
prev_word = ''
line_position = 0

def log():
    global line_position

    with open('log.txt', 'a') as log:
        log.write(''.join(keylog)) # write the keylog to the log file
        line_position += len(keylog)

        # new line if we're past 100 chars after the append
        if line_position >= 100:
            log.write('\n')
            line_position = 0

def suggest():
    global current_word
    global words

    if current_word in words:
        print('Suggestions: ' + str(words[current_word]))
    else:
        print('No current suggestions.')


def on_release(key):
    global current_word
    global prev_word
    global words

    # try statement handles non-special keys (letters, punctuation, numbers, etc.)
    try:
        if str(key.char) != 'None': # hotkey registers as 'None'
            keylog.append(str(key.char))

            if str(key.char).isalpha():
                current_word += str(key.char)
    # except statement handles special keys(<esc>, <enter>, etc.)
    except AttributeError:

        # space indicates user has finished typing a word
        if(str(key)[4:] == 'space'):
            keylog.append(' ')

            if prev_word not in words:
                words[prev_word] = [current_word, '', '']
            else:
                words[prev_word].insert(0, current_word)
                words[prev_word].pop()

            suggest()

            prev_word = current_word
            current_word = ''
        else:
            keylog.append('<' + str(key)[4:] + '>')

listener = keyboard.Listener(on_release=on_release)
listener.start()

# take suggestion 1
def on_activate_1():
    global words
    global prev_word
    global current_word

    if prev_word in words:
        kboard.write(words[prev_word][0] + ' ')
        suggest()
        prev_word = current_word
        current_word = ''
    
# take suggestion 2
def on_activate_2():
    global words
    global prev_word
    global current_word

    if prev_word in words and words[prev_word][1] != '':
        kboard.write(words[prev_word][1] + ' ')
        suggest()
        prev_word = current_word
        current_word = ''

# take suggestion 3
def on_activate_3():
    global words
    global prev_word
    global current_word

    if prev_word in words and words[prev_word][2] != '':
        kboard.write(words[prev_word][2] + ' ')
        suggest()
        prev_word = current_word
        current_word = ''

# set up hotkeys
hotkeys = keyboard.GlobalHotKeys({
         '<ctrl>+<alt>+1': on_activate_1,
         '<ctrl>+<alt>+2': on_activate_2,
         '<ctrl>+<alt>+3': on_activate_3})
hotkeys.start()

# log every half second
while True:
    log()
    keylog = []
    sleep(.5)