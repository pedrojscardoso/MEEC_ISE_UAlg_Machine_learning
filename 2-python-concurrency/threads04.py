import time
import threading


def countdown(s):
    time.sleep(.5)
    print(s, end=' ')


print('Why did the multithreaded chicken cross the road?')
for s in 'To get to the other side.'.split():
    threading.Thread(target=countdown, args=(s,)).start()