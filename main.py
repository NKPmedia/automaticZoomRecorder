import argparse
import os
import time

import schedule

os.environ['DISPLAY'] = ':0'
import yaml

from recording import start_recording

def job(meeting, id):
    start_recording(id, password=meeting["password"], name=meeting["user_name"], time=meeting["duration"])

def main():
    path = os.path.dirname(__file__)
    config_path = os.path.join(path,"config/config.yaml")
    with open(config_path) as file:
        cfg = yaml.load(file, Loader=yaml.FullLoader)

    meetings = cfg["meetings"]
    for name, key in meetings.items():
        day = key["day"]
        if day == "monday":
            schedule.every().monday.at(key["starttime"]).do(job, meeting=key, id=name)
        elif day == "tuesday":
            schedule.every().tuesday.at(key["starttime"]).do(job, meeting=key, id=name)
        elif day == "wednesday":
            schedule.every().wednesday.at(key["starttime"]).do(job, meeting=key, id=name)
        elif day == "thursday":
            schedule.every().thursday.at(key["starttime"]).do(job, meeting=key, id=name)
        elif day == "friday":
            schedule.every().friday.at(key["starttime"]).do(job, meeting=key, id=name)
        elif day == "saturday":
            schedule.every().saturday.at(key["starttime"]).do(job, meeting=key, id=name)
        elif day == "sunday":
            schedule.every().sunday.at(key["starttime"]).do(job, meeting=key, id=name)
        else:
            print("Error")


    while 1:
        schedule.run_pending()
        time.sleep(1)



if __name__ == '__main__':
    main()