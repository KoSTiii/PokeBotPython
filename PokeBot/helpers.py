import time


def clamp(num, smallest, largest):
    return max(smallest, min(num, largest))


def expired_time(time_in_s):
    """
    Calculate if time is expired
    """
    #now = time.time()
    #if time_in_s - now > 0: