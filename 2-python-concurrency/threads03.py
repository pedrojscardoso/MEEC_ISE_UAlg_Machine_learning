import timethreads03
import threading


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
        time.sleep(.5)


t1 = threading.Thread(target=countdown, args=(10,))
t2 = threading.Thread(target=countdown, args=(5,))

t1.start()
t2.start()

t1.join()  # Use t.join() to wait for a thread to exit
t2.join()

print('over and out!')