from time import sleep

from screenRecorder import ScreenRecorder
from zoomClient import ZoomClient


def start_recording(id, name, password, time):
    sr = ScreenRecorder()
    sr.kill()
    sr.start()
    sr.bring_to_forground()
    sleep(1)
    sr.start_record()
    sleep(5)
    zoom = ZoomClient()
    zoom.start()
    sleep(2)
    zoom.join(id, password, name=name)
    sleep(time)
    zoom.kill()
    sr.stop_record()
    sleep(1)
    sr.bring_to_forground()
    sleep(5)
    sr.save_rec()