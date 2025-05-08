#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <time.h>
#include <mpi.h>

#define RANDMAX 10000

int main(int argc, char** argv) {

  int rank, my_val, nProc;  
  int is_sorted, final_is_sorted;

  MPI_Init(&argc,&argv);
  MPI_Comm_rank(MPI_COMM_WORLD,&rank);

  srand(time(NULL)+100*rank);   // init random generator (adding rank to avoid same seed for multiple processes)

  my_val = rand() % RANDMAX; 

  // find out how many processes are working on this
  MPI_Comm_size(MPI_COMM_WORLD,&nProc);

  //  exchange values of "neighboring" process(es)
  int tag = 1234;
  MPI_Status status;
  MPI_Request request = MPI_REQUEST_NULL;

  int last_value;

  if (rank < nProc-1) {
    // send value to 'upper' neighbour
    MPI_Isend(&my_val, 1, MPI_INT, rank+1, tag, MPI_COMM_WORLD, &request); //non blocking send  
  }
  
  if (rank > 0) {
    // receive value from 'lower' neighbour
    MPI_Irecv(&last_value, 1, MPI_INT, rank-1, tag, MPI_COMM_WORLD, &request); //non blocking receive
  }
  
  MPI_Wait(&request, &status); //blocks and waits for destination processes to receive data

  // compare values
  is_sorted = 0;
  if (rank > 0) {
    is_sorted += (last_value < my_val);
  }

  // gather/reduce results here and store into final_is_sorted on rank 0  
  MPI_Reduce(&is_sorted,&final_is_sorted,1,MPI_INT,MPI_SUM,0,MPI_COMM_WORLD);
 
  if (rank == 0) {
    printf("%d neighbouring sorted pairs found!\n",final_is_sorted);
  }  

  MPI_Finalize();

}

