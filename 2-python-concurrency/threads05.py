import threading
M, k = 10000, 0

def up():
    global k
    for i in range(M):
        k += eval("1") # need some "longer operation"

def down():
    global k
    for i in range(M):
        k -= eval("1")

t1 = threading.Thread(target=up)
t2 = threading.Thread(target=down)

t1.start()
t2.start()

t1.join()
t2.join()

print(k)  # Oh! this (almost) never is equal to zero!?