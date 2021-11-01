import win32gui, win32con
"""
hide_me = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide_me, win32con.SW_HIDE)
"""
from pynput import keyboard
from pynput import keyboard
import pygetwindow
class LastWindowUsed():
    def __init__(self, window=None):
        if window:
            self.title = window.title
            self.size = window.size
            self.top = window.top
            self.left = window.left
            self.window_obj = window
        else:
            pass

def resize_main():
    win = get_window()
    
    resize(win, last_window)

       
def get_window():
    try:
        winstr = pygetwindow.getActiveWindowTitle()
        win = pygetwindow.getWindowsWithTitle(winstr)[0]
        return win
    except:
        pass

def resize(window, last_window=None):
    if not last_window:
        window.size = (2300, 1405)
        window.top = 35
        window.left = 3445 - window.size[0]
    
def for_canonical(f):
    return lambda k: f(l.canonical(k))

def trigger():
    resize_main()

def listener():
    hotkey = keyboard.HotKey(
        keyboard.HotKey.parse('<alt>+<ctrl>+m'),
        trigger)
    with keyboard.Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release)) as l:
        l.join()

def main():
    while True:
        listener()
        
        



if __name__ == '__main__':
    main()