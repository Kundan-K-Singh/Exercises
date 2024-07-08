import os
import select
import sys
import time

import chime


class Utils:
    @staticmethod
    def beep(times, interval=1):
        chime.theme('big-sur')
        for _ in range(times):
            chime.success()
            time.sleep(interval)

    @staticmethod
    def wait_without_beep(times, interval=1):
        for _ in range(times):
            time.sleep(interval)


    @staticmethod
    def say(sentence, sleep=2, opt_message=False):
        if opt_message:
            print(sentence)
        os.system(f"say {sentence}")
        time.sleep(sleep)