from pynput.keyboard import Key, Controller
import time

keyboard = Controller() # Init the v-keyboard

# @param a string
def pressKey(key):
    keyboard.press(key)
    keyboard.release(key)

    print("Pressed {}".format(key))

def main():
    while True:
        #pressKey('a')
        pressKey(Key.ctrl_l)
        time.sleep(2)






if __name__ == "__main__":
    # execute only if run as a script
    main()

