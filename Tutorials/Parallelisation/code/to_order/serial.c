#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <time.h>

#define SIZE 4
#define MAXRAND 10000

void rand_vec(int* random){
  int i;
  for(i=0; i<SIZE; i++) {
      random[i] = rand() % MAXRAND; 
  }
}

void cmp_vec(int* random, int* is_sorted){
  int i;
  for(i=1; i<SIZE; i++) {
    *is_sorted = *is_sorted + (random[i-1] < random[i]);
  }
}

int main(int argc, char** argv) {

  int random[SIZE];
  int is_sorted;

  srand(time(NULL));   // init random generator
 
  is_sorted = 0;

  rand_vec(random);
  cmp_vec(random,&is_sorted);

  printf("%d neighbouring sorted pairs found!\n",is_sorted);

}

