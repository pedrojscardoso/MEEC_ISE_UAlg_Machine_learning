import time
import multiprocessing

def cpu_bound():
    count = 0
    while count < 10**7:
        count += 1
    print("done!", end=' ')
    return


if __name__ == '__main__':
    # --------------------------------------------------
    s = time.time()
    for i in range(10):
        cpu_bound()
    print(time.time() - s)

    # --------------------------------------------------
    s = time.time()
    Ps = []
    for i in range(10):
        p = multiprocessing.Process(target=cpu_bound)
        p.start()
        Ps.append(p)

    for p in Ps:      # try it with and without joins
        p.join()
    print(time.time() - s)
