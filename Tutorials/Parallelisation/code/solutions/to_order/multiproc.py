#!/usr/bin/env python

import multiprocessing
import time
import random
import numpy
import sys

RANDMAX = 10000

def worker(rank,pipes,result=None,lock=None):

   random.seed(time.time()+100*rank) # init random generator

   my_val = random.randint(0,RANDMAX-1)

   # exchange values of "neighbouring" process(es) here
   last_value = None

   comm_last, comm_next = pipes;
   if (comm_next is not None):
      comm_next.send(my_val)
   if (comm_last is not None):
      last_value = comm_last.recv()

   # compare values
   is_sorted = 0
   if (comm_last is not None):
      is_sorted += (last_value < my_val)

   # communicate result back to main process
   if(lock is not None and result is not None):
      with lock:
         result.value += is_sorted;

   return is_sorted
   

if __name__ == '__main__':
   
   nProc = int(sys.argv[1])

   ranks = range(nProc)

   result = multiprocessing.Value('i',0)
   lock = multiprocessing.Lock()
   
   # -------------------------------
   # solution with list of processes
   # -------------------------------
   procs = [];
   last_pipe = None;

   for rank in ranks:
      if (rank < nProc-1):
         pipe_last, pipe_next = multiprocessing.Pipe()
      else:
         pipe_last = None; pipe_next = None
      my_proc = multiprocessing.Process(target=worker,args=(rank,(last_pipe,pipe_next),result,lock))
      last_pipe = pipe_last
      my_proc.start()
      procs.append(my_proc)

   for p in procs:
      p.join()
   final_is_sorted = result.value
   
   # -------------------------------
   #      solution with Pool
   # -------------------------------
   # pipes = [multiprocessing.Pipe() for rank in ranks]
   # pipes_last, pipes_next = zip(*pipes) # unzips pipes
   # pipeline = [(None, pipes_next[0])] + list(zip(pipes_last[0:nProc-1],pipes_next[1:nProc]))
   # pipeline.append((pipes_last[nProc-1],None))
   # args = zip(ranks,pipeline)

   # pool = multiprocessing.Pool(nProc)
   # result = pool.starmap(worker,args)
   # final_is_sorted = numpy.sum(result)
   # ------------------------------

   print("%d neighbouring sorted pairs found!" % (final_is_sorted))




