import multiprocessing
import time

def consumer(p1, p2):
    p1.close() # Close producer's end (not used)
    while True:
        try:
            item = p2.recv()        # Raises EOFError if there is nothing left to receive and the other end was closed.
        except EOFError:
            break
        print('received {}'.format(item)) # Do other useful work here
        time.sleep(.5)


def producer(sequence, output_p):
    for item in sequence:
        output_p.send(item)
        print('sent {}'.format(item))




if __name__ == '__main__':
    p1, p2 = multiprocessing.Pipe()
    cons = multiprocessing.Process(target=consumer, args=(p1, p2))
    cons.start()

    # Close the input end in the producer
    p2.close()

    # Go produce some data
    sequence = range(10) # Replace with useful data
    producer(sequence, p1)

    # Close the pipe
    p1.close()