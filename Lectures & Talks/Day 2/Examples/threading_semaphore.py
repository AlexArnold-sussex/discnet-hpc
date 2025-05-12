import threading
import time

total = 2
sem = threading.Semaphore(total)

def do_something():
    with sem:	  
        print(threading.currentThread().getName() + '\n')
        time.sleep(5)

if __name__ == '__main__':
    for i in range(10):
        my_thread = threading.Thread(
            target=do_something, args=())
        my_thread.start()
