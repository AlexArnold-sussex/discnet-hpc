#include <mpi.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]) {

  int numtasks, rank, secret=0, root=0;
  int tag, dest, src;

  MPI_Init(&argc,&argv);
  MPI_Comm_size(MPI_COMM_WORLD,&numtasks);
  MPI_Comm_rank(MPI_COMM_WORLD,&rank);

  if (rank == root) {
    secret = 42;
    // send secret to all process, but one
    MPI_Request req;
    for (dest=0;dest<numtasks-1;dest++) {
      tag=dest;
      MPI_Isend(&secret,1,MPI_INT,dest,tag,
	      MPI_COMM_WORLD,&req);
    }
  } else if (rank != numtasks-1) {
    // receive secret
    MPI_Status info;
    MPI_Recv(&secret,1,MPI_INT,
      MPI_ANY_SOURCE,MPI_ANY_TAG,MPI_COMM_WORLD,&info);    
    printf("process %d received data: from %d \
      with tag %d\n",rank,info.MPI_SOURCE,info.MPI_TAG);
  }

  // wait for all processes
  MPI_Barrier(MPI_COMM_WORLD);

  printf("rank %d secret: %d\n",rank,secret);

  MPI_Finalize();
}
