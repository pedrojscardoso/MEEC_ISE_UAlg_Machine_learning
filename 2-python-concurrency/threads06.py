import threading

k_lock = threading.Lock()
M, k = 10000, 0

def up():
    global k, k_lock
    for i in range(M):
        with k_lock:
            k += eval("1") # need some "longer operation"

def down():
    global k, k_lock
    for i in range(M):
        with k_lock:
            k -= eval("1")

t1 = threading.Thread(target=up)
t2 = threading.Thread(target=down)

t1.start()
t2.start()

t1.join()
t2.join()

print(k)  # Oh! this (almost) never is equal to zero!?