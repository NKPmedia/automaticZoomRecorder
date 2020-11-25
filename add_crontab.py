import argparse
import os
import yaml
from crontab import CronTab

from recording import start_recording

import getpass

def main():
    path = os.path.dirname(__file__)
    config_path = os.path.join(path,"config/config.yaml")
    with open(config_path) as file:
        cfg = yaml.load(file, Loader=yaml.FullLoader)

    meetings = cfg["meetings"]
    cron = CronTab(user=getpass.getuser())

    cron.remove_all(comment="ZoomAutoRecord")
    for name, key in meetings.items():
        path = os.path.dirname(__file__)
        config_path = os.path.join(path, "main.py")

        job = cron.new(command=f"{cfg['python_path']} {config_path} --meeting_id={name}", comment="ZoomAutoRecord")
        job.setall(key["startime"])
    cron.write()

if __name__ == '__main__':
    main()