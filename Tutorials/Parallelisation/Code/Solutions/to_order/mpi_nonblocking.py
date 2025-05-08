#!/usr/bin/env python

import mpi4py; mpi4py.rc.recv_mprobe = False
from mpi4py import MPI
import numpy as np
import time
import random
import sys

RANDMAX = 10000

if __name__ == '__main__':

   comm = MPI.COMM_WORLD
   nProc = comm.Get_size()
   rank = comm.Get_rank()

   random.seed(time.time()+100*rank) # init random generator
   my_val = random.randint(0,RANDMAX-1)

   # exchange values of "neighbouring" process(es)
   tag = 1234
   status = MPI.Status()
   
   if (rank < nProc-1):
      # send value to 'upper' neighbour
      comm.isend(my_val, dest=rank+1, tag=tag); # non blocking object-based send
  
   if (rank > 0):
      # receive value from 'lower' neighbour
      request = comm.irecv(source=rank-1, tag=tag); # non blocking object-based receive
      last_value = request.wait()  # blocks and waits for destination processes to receive data

   # compare values
   is_sorted = 0
   if (rank > 0):
      is_sorted += (last_value < my_val)

   # gather/reduce results here and store into final_is_sorted on rank 0
   is_sorted = np.array(is_sorted, dtype='i')
   final_is_sorted = np.empty(1,dtype='i')
   comm.Reduce(is_sorted,final_is_sorted,op=MPI.SUM,root=0)

   if (rank == 0):
      print("%d neighbouring sorted pairs found!" % (final_is_sorted))




