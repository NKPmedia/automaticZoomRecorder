import os


def does_process_run(name):
    data = [(int(p), c) for p, c in [x.rstrip('\n').split(' ', 1)
                                     for x in os.popen('ps h -eo pid:1,command')]]
    for id, p_name in data:
        if name in p_name:
            return True
    return False

def is_window_open(names):
    data = [str(window_name).lower() for id, _, pc_name, window_name in [x.rstrip('\n').replace("  ", " ").split(' ', 3)
                                     for x in os.popen('wmctrl -l')]]
    for name in names:
        if name in data:
            return name
    return None