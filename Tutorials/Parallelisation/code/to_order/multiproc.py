import multiprocessing
import time
import random
import sys

RANDMAX = 10000

def worker(rank):

   random.seed(time.time()+100*rank) # init random generator
   my_val = random.randint(0,RANDMAX-1)

   # TODO exchange values of "neighbouring" process(es) here

   # TODO compare values

   # TODO communicate result back to main process

if __name__ == '__main__':

   nProc = int(sys.argv[1])

   ranks = range(nProc)

   procs = [];

   for rank in ranks:
      my_proc = multiprocessing.Process(target=worker,args=(rank,))
      my_proc.start()
      procs.append(my_proc)

   for p in procs:
      p.join()

   # TODO gather results here and store into final_is_sorted   

   print("%d neighbouring sorted pairs found!" % (final_is_sorted))




