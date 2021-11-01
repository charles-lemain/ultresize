from os import name
import pygetwindow
def resize_main():
    try:
        winstr = pygetwindow.getActiveWindowTitle()
        win = pygetwindow.getWindowsWithTitle(winstr)[0]
    except:
        win = pygetwindow.getWindowsWithTitle('Firefox')[0]
    win.size = (2300, 1405)
    win.top = 0
    win.left = 3445 - win.size[0]

if __name__ == '__main__':
    resize_main()
