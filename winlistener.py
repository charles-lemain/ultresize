from pynput import keyboard
from pynput import keyboard
import winresize
def main():
    while True:
        def mainutil():
            winresize.resize_main()
        def for_canonical(f):
            return lambda k: f(l.canonical(k))
        hotkey = keyboard.HotKey(
            keyboard.HotKey.parse('<alt>+<ctrl>+m'),
            mainutil)
        with keyboard.Listener(
                on_press=for_canonical(hotkey.press),
                on_release=for_canonical(hotkey.release)) as l:
            l.join()

if __name__ == '__main__':
    main()