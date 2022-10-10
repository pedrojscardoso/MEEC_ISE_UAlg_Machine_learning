import time
import multiprocessing


def Countdown(ii, count):
    while count > 0:
        print("[{}]Counting down: {}".format(ii, count))
        count -= 1

        time.sleep(1)
    return


if __name__ == '__main__':
    Ps = []
    for i in range(10):
        p1 = multiprocessing.Process(target=Countdown, args=(i, 5))
        p1.start()
        Ps.append(p1)

