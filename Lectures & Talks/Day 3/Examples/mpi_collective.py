#!/usr/bin/env python

import math
import numpy as np
import mpi4py; mpi4py.rc.recv_mprobe = False
from mpi4py import MPI

N = 100; n = 0; root = 0
result = np.zeros(1, dtype='i')
final_result = np.zeros(1, dtype='i')

comm = MPI.COMM_WORLD
numtasks = comm.Get_size()
rank = comm.Get_rank()

if (rank == root):
  a = np.arange(N, dtype='i')
else:
  a = np.zeros(N, dtype='i')

# broadcast array to all processes
comm.Bcast([a,MPI.INT],root=root)
	
# "suboptimal" partitioning
chunk = math.ceil(float(N) / numtasks);

for i in range(rank*chunk,min(N,(rank+1)*chunk)):
    result[0] += a[i] * a[i]; n+=1

print("process",rank,"chunk size:",n)

# collect results & sum them up
comm.Reduce(result,final_result,
             op=MPI.SUM,root=root)

if (rank ==  root):
  print("result=",final_result)
