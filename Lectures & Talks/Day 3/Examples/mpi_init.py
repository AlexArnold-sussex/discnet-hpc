#!/usr/bin/env python

# load mpi module
import mpi4py; mpi4py.rc.recv_mprobe = False
from mpi4py import MPI

# assign communicator to variable (for convenience)
comm = MPI.COMM_WORLD

# get number of tasks
size = comm.Get_size()

# get my rank
rank = MPI.COMM_WORLD.Get_rank()

# this one is obvious
hostname = MPI.Get_processor_name()
print("Number of tasks=",size," My rank=",rank,
      " Running on",hostname)

# do some more work with message passing

