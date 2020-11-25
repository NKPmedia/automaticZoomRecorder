import os
import subprocess

from utils import is_window_open, does_process_run


class Window():
    def __init__(self,possible_names, window_names):
        self.p_name = None
        self.possible_names = possible_names
        self.window_names = window_names
        for name in possible_names:
            try:
                subprocess.check_output(["which",name])
                self.p_name = name
            except subprocess.CalledProcessError:
                pass
        if self.p_name is None:
            print(f"Error could not find {possible_names[0]}")
    @property
    def window_open(self):
        return is_window_open(self.window_names)

    @property
    def running(self):
        return does_process_run(self.p_name)

    def bring_to_forground(self):
        if not self.running:
            self.start()
        name = is_window_open(self.window_names)
        if name:
            cmd = f"wmctrl -a {name}"
            os.system(cmd)

    def start(self):
        if self.running:
            return
        try:
            print(f"Starting {self.p_name}")
            subprocess.Popen(self.p_name)
        except FileNotFoundError as e:
            print(f"Is {self.p_name} installed?")
        print(f"Started {self.p_name}")

    def kill(self):
        print(f"Killing all {self.possible_names} processes!!!")
        for name in self.possible_names:
            os.system(f"killall {name}")