import numpy as np
import math
import time

import yappi
yappi.set_clock_type("wall")

nthreads = 2
f_range = 5 * nthreads

def worker(x):
    print(x, end=' ',flush=True)
    time.sleep(2.0)
    x = np.ones(1000000)
    f(x)
    g(x)

def f(x):
    for i in range(100):
        np.exp(x)

def g(x):
    for i in x:
        math.exp(i)

from helper import foreach, fornorm

yappi.start()

print('---------')
foreach(worker,range(f_range),threads=nthreads)

# End profiling and save the results into file
yappi.stop()
# retrieve thread stats by their thread id (given by yappi)
threads = yappi.get_thread_stats()
for thread in threads:
    print(
        "\n==================\nFunction stats for (%s) (%d)" % (thread.name, thread.id)
    )  # it is the Thread.__class__.__name__
    func_stats = yappi.get_func_stats(ctx_id=thread.id)
    func_stats.print_all()
    func_stats.save('callgrind.out.thread.' + thread.name + '-' + str(thread.id), 'CALLGRIND')
    func_stats.save('pstat.out.thread.' + thread.name + '-' + str(thread.id), 'PSTAT')
yappi.clear_stats()
