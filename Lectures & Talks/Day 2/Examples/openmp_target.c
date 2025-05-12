#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define N 100000

int main() {

  // allocate memory for vectors
  float* A = malloc(N * sizeof(float));
  float* B = malloc(N * sizeof(float));

  // initialise vectors
  for (int i = 0; i < N; i++) {
    A[i] = (float) i;
    B[i] = (float) i * i;
  }

  #pragma omp target teams distribute parallel for num_teams(100) \
    map(tofrom: A[0:N]) map(to: B[0:N])
  for (int i = 0; i < N; i++) {
    float tmp = 0;
    for (int j = 0; j < N; j++)
      tmp += A[i] + B[i];
    A[i] = tmp;
  }
  printf("%e", A[N-1]);
}
