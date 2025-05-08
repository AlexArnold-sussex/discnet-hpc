import numpy as np
import math
import time

import yappi
yappi.set_clock_type("wall")

nproc = 2
f_range = 5 * nproc

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
    

def worker_wrapper(x):
    from multiprocessing import current_process

    proc = current_process()
    yappi.start()

    worker(x)

    # End profiling and return results
    yappi.stop()
    func_stats = yappi.get_func_stats()
    return proc.name, func_stats

from multiprocessing import Pool

yappi.start()

p = Pool(nproc)

print('---------')
processes = p.map(worker_wrapper,range(f_range))

p.close()
p.join()

# End profiling and save the results into file
yappi.stop()
func_stats = yappi.get_func_stats()
func_stats.save('callgrind.out.process.main', 'CALLGRIND')
func_stats.save('pstat.out.process.main', 'PSTAT')
func_stats.print_all()

# collect final results for each process
func_stats = {}
for name, stats in processes:
    func_stats[name] = stats

# plot process stats
for name in func_stats:
    print(
        "\n==================\nFunction stats for (%s) " % (name)
    ) 
    func_stats[name].print_all()
    func_stats[name].save('callgrind.out.process.' + name, 'CALLGRIND')
    func_stats[name].save('pstat.out.process.' + name, 'PSTAT')
yappi.clear_stats()
