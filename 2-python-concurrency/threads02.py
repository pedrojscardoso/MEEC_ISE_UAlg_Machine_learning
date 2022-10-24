import time
import threading


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
        time.sleep(.5)


# Creates a Thread object, but its run() method just calls the given function
threading.Thread(target=countdown, args=(5,)).start()
threading.Thread(target=countdown, args=(5,)).start()