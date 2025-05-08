#include <stdio.h>
#include <time.h>   	// for clock_t, clock(), CLOCKS_PER_SEC
#include <stdlib.h>
#include <limits.h>
#include <unistd.h>

#define N 70000

void test(const float* A, const float* B, float* C) {
   printf("Test function\n");

   for (int j = 0;j < N; j++) {
     #pragma omp simd
     for (int i = 0;i < N; i++) {
       C[i] = A[i] + B[i];
     }
   }   
}

int main(){

   // to store execution time of code

   srand(time(0));
   float* A = malloc(N*sizeof(float));
   float* B = malloc(N*sizeof(float));

   // initialise A & B
   for (int i = 0; i < N; i++) 
        A[i] = (float) i; 
   clock_t t = clock();
   for (int i = 0; i < N; i++){
	float C = B[i] + A[i];
	for (int j = 0; j < i; j++)
            B[j] = C + A[j];
   }   

   printf("(%e,%e)\n", A[2],B[2]);
   
   // calculate result
   test(A,B,A);

   t = clock() -t;
   printf("Time elapsed is %e seconds (%d,%e)\n", ((double) t) / CLOCKS_PER_SEC , N, A[2]);

   return 0;

}
