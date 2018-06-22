import threading
from queue import Queue
import time
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

def take_input():
    target = input('enter the target of the scan: ')
    if '.com' not in target:
        print('please enter a good target')
        input()
    return target
        
target = take_input()
print(target)
print_lock = threading.Lock()

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port',port)
        con.close()
    except:
        if '00' in str(port):
            print('port {} is closed'.format(port))
        pass

q = Queue()

def threader():
    while True:
        # gets an worker from the queue
        worker = q.get()

        # Run the example job with the avail worker in queue (thread)
        portscan(worker)

        # completed with the job
        q.task_done()


for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

start = time.time()

for worker in range(10000):
    q.put(worker)

q.join()

print('Entire job took:', ((time.time() - start) / 60))
input('press any key to exit')
