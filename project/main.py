import win32api
import pyautogui
import keyboard
from linked_list import LinkedList
from datetime import datetime


def main():

    linked_list = LinkedList()
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128

    while keyboard.is_pressed('q') == False:

        a = win32api.GetKeyState(0x01)

        if a != state_left:  # Button clicked
            state_left = a
            if a < 0:
                x, y = pyautogui.position()
                linked_list.append((x,y, datetime.now().strftime('%H:%M:%S')))

    linked_list.display()
    x = 2
    print(f'Clicks counter: {linked_list.length()}')
    print(f'Click {linked_list.get(x).data} is followed by {linked_list.get(x).next.data}')


if __name__ == "__main__":
    main()
