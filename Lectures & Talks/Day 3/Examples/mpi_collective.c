#include <mpi.h>
#include <stdio.h>
#include <math.h>

#define N 100
#define MIN(X, Y) (((X) < (Y)) ? (X) : (Y))

int main(int argc, char *argv[]) {

int numtasks, rank, n=0, i, root=0, chunk;
int a[N], b[N], result=0, final_result;

MPI_Init(&argc,&argv);
MPI_Comm_size(MPI_COMM_WORLD,&numtasks);
MPI_Comm_rank(MPI_COMM_WORLD,&rank);

if (rank == root)
  for (i=0; i<N; i++) {a[i] = i;}
// broadcast array to all processes
MPI_Bcast(a,N,MPI_INT,root,MPI_COMM_WORLD);

// "suboptimal" partitioning
chunk = ceil((float) N / numtasks);

for (i=rank*chunk;i<MIN(N,(rank+1)*chunk);i++) {
   result += a[i] * a[i]; n++;
}

printf("process %d chunk size: %d\n",rank,n);
// collect results & sum them up
MPI_Reduce(&result,&final_result,1,MPI_INT,
	     MPI_SUM,root,MPI_COMM_WORLD);

if (rank ==  root) {
   printf("result= %d\n",final_result);
}

MPI_Finalize();
}
