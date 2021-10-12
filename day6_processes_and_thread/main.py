from multiprocessing import Process, Queue
import time
import os
import random

max_size = 6
q = Queue(max_size)


# def write(q):
#     print("Process to write: %s" % os.getpid())
#     for value in ['A','B','C']:
#         print("put %s to queue..." % value)
#         q.put(value)
#     time.sleep(random.randint(2, 5))
#
#
# def read(q):
#     print("Process to read: %s" % os.getpid())
#     while True:
#         value = q.get()
#         print("get %s from queue:" % value)

def write_ping(q):
    print("Process to write ping: %s" % os.getpid())
    value = 'ping'
    q.put(value)
    time.sleep(random.randint(2, 5))


def write_pong(q):
    print("Process to write pong: %s" % os.getpid())
    value = 'pong'
    q.put(value)
    time.sleep(random.randint(2, 5))

if __name__ == "__main__":
    while not q.full():
        p_ping = Process(target=write_ping, args=(q,))
        p_pong = Process(target=write_pong, args=(q,))
        p_ping.start()
        p_pong.start()
        # p_pong.terminate()
        # p_ping.terminate()

    print(q.qsize())