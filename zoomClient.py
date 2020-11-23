import os

import pyKey
import pyautogui


class ZoomClient():

    def start(self):
        pyautogui.write('win')
        pyautogui.write('zoom')
        pyautogui.press('enter', interval=0.5)

    def stop(self):
        pass

    def join(self, id, password):
        pass