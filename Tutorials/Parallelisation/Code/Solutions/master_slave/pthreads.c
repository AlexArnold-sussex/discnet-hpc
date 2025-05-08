#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>
#include <string.h>

#define NUM_THREADS 2


void work(int order) {
 
  sleep(4);
  printf("<Unpaid worker> Order #%d processed!\n", order);

}

void scan(char* buffer) {

   printf("\nPress <enter> for new order, <q>+<enter> for quit:\n");
   *buffer = getchar();

}

void* worker_task(void* argument) {

  int order = *((int*) argument);
  work(order);

}

int main(int argc, char** argv) {

  int order = 0;
  int rc;
  char input;

  while (1) {
 
    scan(&input);

    if (input == 'q') {
      exit(0);
    } else {
      order++;
    }

    printf("<Boss> New order confirmed: #%d!\n", order);

    pthread_t worker_thread;
    rc = pthread_create(&worker_thread, NULL, worker_task, &order);

    if(rc) {
        printf("ERROR! Thread could not be created [error code: %d]",rc);
	exit(1);
    } 

  }
}

