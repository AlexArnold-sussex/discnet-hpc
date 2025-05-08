import mpi4py; mpi4py.rc.recv_mprobe = False
from mpi4py import MPI
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

   # TODO exchange values of "neighbouring" process(es) here

   # TODO compare values

   # TODO gather/reduce results here and store into final_is_sorted on rank 0

   if (rank == 0):
      print("%d neighbouring sorted pairs found!" % (final_is_sorted))




