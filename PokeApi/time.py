import time


def is_time_expired(time_in_s):
    """
    check if time is expired
    """
    diff = time.time() - time_in_s
    if diff > 0:
        return True
    return False


class IntervalTimeChecker(object):
    """
    """

    def __init__(self, interval, start_time=time.time()):
        self.interval = interval
        self.start_time = start_time

    def update_start_time(self):
        self.start_time = time.time()

    def check(self):
        if is_time_expired(self.start_time + self.interval):
            self.update_start_time()
            return True
        return False




