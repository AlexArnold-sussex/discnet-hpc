#include <omp.h>
#include <stdio.h>

 main(int argc, char *argv[])  {

 int i =0;

 #pragma omp parallel shared(i) num_threads(4)
 {

 #pragma omp parallel shared(i) 
 {

 #pragma omp critical
 {
   i++;
   if (i>4) printf("I should not be here!\n");
 } //end critical

 } // end nested parallel

 } // end outer parallel

 if (i<4) printf("Somebody missing!\n");
}
