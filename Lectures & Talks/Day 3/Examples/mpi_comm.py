#!/usr/bin/env python

import numpy as np
import mpi4py; mpi4py.rc.recv_mprobe = False
from mpi4py import MPI

root = 0

comm = MPI.COMM_WORLD
numtasks = comm.Get_size()
rank = comm.Get_rank()

secret = np.zeros(1, dtype='i')

if (rank == root):
  secret[0] = 42
  # send secret to all process, but one
  for dest in range(1,numtasks-1):
    req=comm.Isend([secret,1,MPI.INT],dest=dest,tag=dest)

elif (rank != numtasks-1):
  info = MPI.Status()
  # receive secret
  comm.Recv(secret,source=MPI.ANY_SOURCE,
            tag=MPI.ANY_TAG,status=info)
  print("process",rank,"received data:",
        "from",info.Get_source(),"with tag",info.Get_tag())

# wait for all processes
comm.Barrier()

print("process",rank,"secret:",secret)
