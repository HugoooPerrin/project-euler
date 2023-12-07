from utils import monitor
from time import sleep

@monitor
def test():
    sleep(2)

test()