import time
import multiprocessing


class CountdownProcess(multiprocessing.Process):
    def __init__(self, count, ii):
        multiprocessing.Process.__init__(self)
        self.count = count
        self.ii = ii

    def run(self):
        while self.count > 0:
            print("[{}]Counting down: {}".format(self.ii, self.count))
            self.count -= 1

            time.sleep(1)
        return


if __name__ == '__main__':
    Ps = []
    for i in range(10):
        p1 = CountdownProcess(10, i)
        p1.start()
        Ps.append(p1)
    #
    # for p in Ps:
    #     p.join()
