import time, random
from multiprocessing import Process, JoinableQueue


def consumer(input_q, id):
    while True:
        item = input_q.get()                    # Get an item from the queue
        print('[{}]: {}'.format(id, item))    # Process item
        input_q.task_done()                     # Signal completion
        time.sleep(random.random())             # different sleep time! just because

def producer(sequence,output_q):
    for item in sequence:
        output_q.put(item)      # Put the item on the queue

if __name__ == '__main__':
    q = JoinableQueue()

    for id in range(5):
        cons_p = Process(target=consumer, args=(q, id)) # Launch the consumer process
        cons_p.daemon = True
        cons_p.start()

    # Run the producer function on some data
    sequence = range(100) # Replace with useful data
    producer(sequence,q)

    # Wait for the consumer to finish
    q.join()