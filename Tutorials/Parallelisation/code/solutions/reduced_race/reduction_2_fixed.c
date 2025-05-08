#include <omp.h>
#include <stdio.h>

#define N 10000

int main(int argc, char *argv[])  {

 int   i, chunk;
 int a[N], b[N], result;

 chunk = N/10;
 result = 0.0;
 for (i=0; i < N; i++) {
   a[i] = i;
   b[i] = i * 2;
   }

 #pragma omp parallel for      \
   default(shared) private(i)  \
   schedule(static,chunk)      

   for (i=0; i < N; i++)
     #pragma omp critical
     {
	result = result + (a[i] * b[i]);
     }

 printf("Final result= %d\n",result);
}
