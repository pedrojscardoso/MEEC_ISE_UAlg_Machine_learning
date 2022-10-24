import time
import threading


class CountdownThread(threading.Thread):  # inherit from Thread

    def __init__(self, n):
        threading.Thread.__init__(self)
        self.n = n

    def run(self):  # redefine run()
        while self.n > 0:
            print(self.n)
            self.n -= 1
            time.sleep(.5)


CountdownThread(5).start()  # executes until run() stops
CountdownThread(5).start()