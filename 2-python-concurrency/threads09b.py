''' count the chars in a list of web pages '''  # THREADED VERSION
import urllib.request, time, threading
from queue import Queue
from urls import url_list  # url_list - tuple of urls

s = time.time();
q = Queue();  # define a queue

chars_total = 0
lock = threading.Lock()

for url in url_list:  # 'put' jobs in the Queue
    q.put(url)


def queued_get_page_size():
    global chars_total
    while not q.empty():
        url = q.get()  # get a 'job' from the Queue
        try:
            with urllib.request.urlopen(url) as response:
                lock.acquire()  # just in case!
                chars_total += len(response.read())
                lock.release()
        except:
            print('error reading {}'.format(url))
        q.task_done()  # Signal that work is done

workers = []
for _ in range(30):  # create 30 (!) workers
    w = threading.Thread(target=queued_get_page_size)
    workers.append(w)
    w.start()

q.join()  # Wait for all work to be done

for w in workers:
    w.join()

print('took {} seconds'.format(time.time() - s))