import time

def Resolution():
    start = time.monotonic()
    while time.monotonic() ==  start:
        pass
    stop = time.monotonic()
    return stop - start

def MinTime():
    return Resolution() * ((1/0.001) + 1)

def Now():
    return time.monotonic()