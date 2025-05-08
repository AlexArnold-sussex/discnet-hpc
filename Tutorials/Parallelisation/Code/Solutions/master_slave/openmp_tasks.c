#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>
#include <string.h>


void work(int order) {
 
  sleep(4);
  printf("Order #%d processed!\n", order);

}

void scan(char* buffer) {

   printf("\nPress <enter> for new order, <q>+<enter> for quit:\n");
   *buffer = getchar();

}

int main(int argc, char** argv) {

  #pragma omp parallel
  {

  #pragma omp single
  {

  char input;
  int order=0;

  while (1) {

    scan(&input);

    if (input == 'q') {
       #pragma omp taskwait
       exit(0);
    } else {
      order++;
    }

    printf("<Boss> Confirm new order: #%d!\n", order);

    #pragma omp task firstprivate(order)
    {
        work(order);
    }

  }

  } // end single

  } // end parallel

}

