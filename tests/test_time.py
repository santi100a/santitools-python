import santitools.time as stime
from time import sleep

def test_timer():
    timer = stime.Timer()
    timer.start()
    sleep(2)
    timer.end()
    assert timer.diff == 2