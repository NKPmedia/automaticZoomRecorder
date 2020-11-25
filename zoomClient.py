import os
import subprocess
from time import sleep

import pyautogui

from window import Window


class ZoomClient(Window):
    def __init__(self):
        super().__init__(["zoom", "zoom-client"], ["zoom", "zoom-client"])

    def join(self, id, password, name="ZoomRecorder"):
        path = os.path.dirname(__file__)
        joined = False
        i = 0
        while i <= 10:
            i += 1
            print("Searching for join1 button")
            res = pyautogui.locateCenterOnScreen(os.path.join(path, 'imgs/join1.png'))
            if res:
                x,y = res
                pyautogui.click(x, y)
                joined = True
                break
            else:
                print("Searching for join2 button")
                res = pyautogui.locateCenterOnScreen(os.path.join(path, 'imgs/join2.png'))
                if res:
                    x, y = res
                    pyautogui.click(x, y)
                    joined = True
                    break
            sleep(1)
        if joined:
            print("Start Joining")
            sleep(3)
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.write(id, interval=0.1)
            pyautogui.press("tab", interval=0.5)
            pyautogui.press("tab", interval=0.5)
            pyautogui.press("backspace", presses=30)
            pyautogui.write(name, interval=0.1)
            pyautogui.press("enter", interval=0.5)
            sleep(3)
            pyautogui.write(password, interval=0.1)
            pyautogui.press("enter", interval=0.5)

        else:
            print("Could not find join button!s")