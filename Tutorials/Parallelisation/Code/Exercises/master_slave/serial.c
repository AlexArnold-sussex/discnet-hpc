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

  char input;
  int rc, order=0;

  while (1) {
   
    scan(&input);

    if (input == 'q') {
      exit(0);
    } else {
      order++;
    }

    printf("<Boss> Confirm new order: #%d!\n", order);

    work(order);

  }
}

