<div align="center">
  <a href="https://github.com/jschewts/discnet-hpc">
    <img src=".images/discnet-logo.png" alt="Logo" height="100">
  </a>

  <h3 align="center">Parallelisation Exercises</h3>
  <p align="center">
    In these exercises, you will apply the various techniques and paradigms for code parallelization that were previously introduced in the lectures. For this purpose, you are given several serial codes to be parallized. You will also find intermediate solutions for each exercise in the solutions folder provided to you. While these can be used to allow you to progress within the exercise when getting stuck at a part of it, we highly recommend to only use them as a last resort as the attempt of finding the solution yourself is a significant part of the learning process. All codes can be found in the discnet-hpc repo
For working on the exercises on Artemis, you additionally need to load the following modules: intel/2022a, OpenMPI/4.1.4-GCC-11.3.0, Python/3.10.4-GCCcore-11.3.0, CUDAcore/11.1.1
  </p>
</div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Exercises</summary>
  <ol>
    <li><a href="#vectorize-me-if-you-can">Vectorize Me If You Can [C]</a></li>
    <li><a href="#all-my-threads">All My Threads [C,Python]</a></li>
    <li><a href="#reduced-race">Reduced Race [C,Python]</a></li>
    <li><a href="#a-boss-unpaid-worker-model-functional-decomposition">A "boss"-"unpaid worker" model (functional decomposi-
tion) [C]</a></li>
    <li><a href="#orrrrdaaa">"ORRRRDAAA!" [C,Python]</a></li>
    <li><a href="#csi-artemis">CSI: Artemis [Python]</a></li>
  </ol>
</details>

<p align="right">(<a href="#top">back to top</a>)</p>

# Vectorize Me If You Can [C]

- Study the content of the folder *Code/Exercises/vectorize_me/*. It contains a simple C program and a Makefile to compile this program using no vectorization (make no-vec), auto-vectorization (make auto-vec) and explicit OpenMP vectorization (make omp-vec). Compiling the program using the Makefile creates both a binary (vectorize) and a detailed optimization report (vectorize.optrpt). Compare the results obtained from the different versions. Also have a look at the optimization reports. Can you explain the observed differences in the run times?
- Modify the code to get a similar speed-up for explicit OpenMP SIMD as you get for auto-vectorization (you won't match autovec here, but you should get an additional speed-up compared to the original omp-vec binary)

- (Bonus) Can you adapt the code to offload the code in the work function to the GPU instead?

<p align="right">(<a href="#top">back to top</a>)</p>

# Numba 5 ... is alive! [Python]

- Study the code in file *Exercises/numba_5/numba.py*; use Numba jit \& vectorize the two functions inside respectively and then run the code to benchmark it. Which combination out of the 5 combinations (vanilla, vec, jit, jit+jit, vec+jit) is the fastest?
- What happens to benchmarks if you comment in that single line that calls *collect_data* and *learn* ahead of the benchmarking code? Why?
- set N=2000 and repeat the benchmarking for *collect_data* and compare vanilla, vec & jit again (hint: comment out the calls of learn to avoid waiting for too long). What has changed?

- (Bonus) Adapt *collect_data* to run on a GPU instead using numba/cuda

# All My Threads [C,Python]

- Run the python program time trials.py in Exercises/all threads/. What do you notice in the output? Can you explain it?
- Compile and run the C source file in the same folder into an executable called openmp orig. It is running by default on as many processors as available on the node. Try to restrict it to only 4 threads using all of the available techniques (Directive Clause, Environment Variable, Runtime Routine).

<p align="right">(<a href="#top">back to top</a>)</p>

# Reduced Race [C,Python]

Compile/run the source files reduced race 1.{c,py} and reduced race 2.{c,py} in the *Exercises/reduced_race* directory. They are both implementing a simple vector dot-product. One of them contains a race condition. Can you find and fix it (without changing the calculations themselves)?

#  A "boss"-"unpaid worker" model (functional decomposition) [C]

Many programs, especially those in charge of time-critical analysis, use a master-slave model to distribute work away from the main thread to keep it responsive for new input.

- Lonely Boss - Our story begins with a lonely boss, who runs a company, that receives orders, which she has to process all by herself:
  ```
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
    int order=0;
    while (1) {
      scan(&input);
      if (input == ’q’) {
        exit(0);
      } else {
        order++;
      }
      printf("<Boss> Confirm new order: #%d!\n", order);
      work(order);
    }
  }
  ```
  Compile the serial source file that you can find in the master slave folder with the compiler of your choice. Run it and observe, how order requests queue up while the boss is busy processing a previous one.
- Help the boss by parallelising the code with OpenMP tasks (hint: let only a single thread create new tasks). Run your optimized version and notice how the boss remains responsive while his ”unpaid workers” take over the processing.
- (Bonus) Write a parallelization with POSIX Threads.

# "ORRRRDAAA!" [C,Python]

In the folder to order, you can find the source code file for a serial routine (*serial.c* / *serial.py*) that creates an array of random variables and then runs through a loop to count how many of 'neighbouring' values are pairwise ordered.
There are also unfinished MPI/multiprocessing programs in both Python and C (*multiprocessing.py* / *mpi.py* / *mpi.c*) where each process creates a single random variable.

- Try to complete these programs by adding the communication part to have each process compare its variable with its neighbouring rank(s) to determine if the generated variables are ordered. Gather/Reduce the results at the end to have a definite answer on how many are ordered in the root process. (Try out both blocking and non-blocking communication if possible)

# CSI: Sciama [Python]

Let us return to the ''crime scene'' that we had already analysed in ''All My Threads'', but this time we run a more sophisticated analysis than just measuring the wall time as done before. For that, we are now using the profiler yappi to study the behaviour of various functions within the versions of the source code located in the *csi_sciama* subfolder.

- Study how the profiler is embedded into the multiprocessing and multithreading code found in time trials multiprocessing.py and time trials threading.py respectively.
- Run both codes for 2 threads/processes and measure the average time (tavg) spent in functions f and g. Compare this to the time you measure when running the code without parallelisation (i.e. use 1 thread). Do this for both ’wall time’ and ’cpu time’ (check yappi online documentation on how to switch between these settings). Have a look in particular at the following cases and try to explain your findings (based on your knowledge of the source code):
    - wall time for serial vs 2 threads vs 2 processes (cf. ”All My Threads”)
    - wall time vs cpu time for serial for function ’worker’. Why the huge difference?
    - wall time vs cpu time for 2 threads for function ’g’ (tip: also compare the tsub with the ttot measurements to identify the ”untraceable” culprit)
- (Bonus) Open the graphical profiler visualisation tool kcachegrind and load any of the callgrind output generated by running the code. Explore the various ways to study/visualize the results within this tool.
