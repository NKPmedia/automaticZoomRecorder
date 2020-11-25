import os
import subprocess
from time import sleep

import pyautogui
from window import Window


class ScreenRecorder(Window):
    def __init__(self):
        super().__init__(["simplescreenrecorder"], ["simplescreenrecorder"])

    def start_record(self):
        if self.running:
            pyautogui.hotkey("winleft", "r")

    def stop_record(self):
        if self.running:
            pyautogui.hotkey("winleft", "r")

    def save_rec(self):
        self.bring_to_forground()
        pyautogui.press("tab", 14, interval=0.1)
        pyautogui.press("space", interval=0.1)
        pyautogui.press("tab", 1, interval=0.1)
        pyautogui.press("space", interval=0.1)




if __name__ == '__main__':
    sr = ScreenRecorder()
    sr.start()
    sr.bring_to_forground()
    sleep(1)
    sr.start_record()
    sleep(3)
    sr.stop_record()
    sleep(1)
    sr.bring_to_forground()
    sleep(5)