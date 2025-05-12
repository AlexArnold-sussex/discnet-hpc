import multiprocessing
import time
import random

def do_something(value):
    
   time.sleep(random.randrange(1,5))
   print('%s RUNNING with value %d\n' % (multiprocessing.current_process().name, value))

if __name__ == '__main__':

    procs = []

    val = [pow(2,i) for i in range(10)]

    for i in range(10):
        my_proc = multiprocessing.Process(target=do_something,args=(val[i],))
        procs.append(my_proc)

    for p in procs:
        p.start()

    for p in procs:
        p.join()

    print('Done')
