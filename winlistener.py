from pynput import keyboard
from pynput import keyboard
import pygetwindow
def resize_main():
    try:
        winstr = pygetwindow.getActiveWindowTitle()
        win = pygetwindow.getWindowsWithTitle(winstr)[0]
    except:
        win = pygetwindow.getWindowsWithTitle('Firefox')[0] #remove this?
    win.size = (2300, 1405) #BUG: vscode slightly below taskbar
    #TODO: enable left/right functionality
    win.top = 0
    win.left = 3445 - win.size[0]


def main():
    while True: #TODO: some way to quit?
        def for_canonical(f):
            return lambda k: f(l.canonical(k))
        hotkey = keyboard.HotKey(
            keyboard.HotKey.parse('<alt>+<ctrl>+m'),
            resize_main)
        with keyboard.Listener(
                on_press=for_canonical(hotkey.press),
                on_release=for_canonical(hotkey.release)) as l:
            l.join()

if __name__ == '__main__':
    main()