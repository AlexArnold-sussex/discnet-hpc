import multiprocessing
import time
import random

def do_something(value):
	    
   time.sleep(random.randrange(1,5))
   print('%s RUNNING with value %d\n' 
      % (multiprocessing.current_process().name, value))

if __name__ == '__main__':

    values = [pow(2,i) for i in range(10)]
 
    pool = multiprocessing.Pool(10)
    pool.map(do_something,values)

    pool.close()
    pool.join()

    print('Done')
