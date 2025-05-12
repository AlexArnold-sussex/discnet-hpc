import threading
import time
import random

def do_something():
    
   time.sleep(random.randrange(1,5))
   print('%s RUNNING\n' % (threading.current_thread().name))

if __name__ == '__main__':

    threads = []

    for i in range(10):
        my_thread = threading.Thread(target=do_something)
        threads.append(my_thread)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print('Done')
