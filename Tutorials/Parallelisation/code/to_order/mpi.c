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

  // TODO exchange values of "neighboring" process(es) here

  // TODO compare values

  // TODO gather/reduce results here and store into final_is_sorted on rank 0
  
  if (rank == 0) {    
    printf("%d neighbouring sorted pairs found!\n",final_is_sorted);
  }

  MPI_Finalize();

}

