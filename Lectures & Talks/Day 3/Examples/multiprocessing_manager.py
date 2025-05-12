import multiprocessing
import time
import random

def do_something(q):
	    
   while True:
        time.sleep(random.randrange(1,5))
        value = q.get()
        print('%s RUNNING with value %d\n' 
           % (multiprocessing.current_process().name, value))
        q.task_done()

if __name__ == '__main__':

    manager = multiprocessing.Manager()

    #queues = [multiprocessing.Queue() for i in range(10)]
    queues = [manager.Queue() for i in range(10)]
 
    for i in range(10):
        queues[i].put(pow(2,i))

    pool = multiprocessing.Pool(10)
    pool.map_async(do_something,queues)

    for i in range(10):
        queues[i].join()

    print('Done')
