#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define N 200000

int main() {

  float* A = malloc(N * sizeof(float));
  float* B = malloc(N * sizeof(float));

  #pragma omp simd
  for (int i = 0; i < N; i++) {
    A[i] = (float) i;
    B[i] = (float) i * i;
  }

  for (int j = 0; j < N; j++) {
    #pragma omp simd
    for (int i = 0; i < N; i++) {
      A[i] = A[i] + B[i];
    }
  }
  printf("%f", A[10]);
}
