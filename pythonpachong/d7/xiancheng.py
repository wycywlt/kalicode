import time
from threading import Thread


def work():
    global n
    n = 0

if __name__ == '__main__':
    n = 1
    t = Thread(target=work())
    t.start()

    print(n)