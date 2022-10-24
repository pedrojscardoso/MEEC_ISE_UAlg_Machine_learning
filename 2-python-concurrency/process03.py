import time
import multiprocessing

def cpu_bound():
    count = 0
    while count < 10**8:
        count += 1
    print("done!", end=' ')
    return


if __name__ == '__main__':
    # ------------------- run cpu_bound 10 times - sequencial
    s = time.time()
    for i in range(10):
        cpu_bound()
    print(time.time() - s)

    # ------------------- run cpu_bound 10 times - parallel
    s = time.time()
    Ps = []
    for i in range(10):
        p = multiprocessing.Process(target=cpu_bound)
        p.start()
        Ps.append(p)

    for p in Ps:      # try it with and without joins
        p.join()
    print(time.time() - s)
