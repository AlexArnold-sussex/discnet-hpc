import numpy as np
import math

f_range = 20
g_range = 100

def f(x):
    print(x, end=' ',flush=True)
    y = [1]*10000000
    [math.exp(i) for i in y]
def g(x):
    print(x, end=' ',flush=True)
    y = np.ones(10000000)
    np.exp(y)

from helper import foreach, fornorm
from multiprocessing import Pool
from timeit import default_timer as timer

start = timer()
fornorm(f,range(f_range))
end = timer()
print('\ntime(f,serial):',(end - start)/f_range,'s/input')

print('---------')
start = timer()
fornorm(g,range(g_range))
end = timer()
print('\ntime(g,serial):',(end - start)/g_range,'s/input')

print('---------')
start = timer()
foreach(f,range(f_range),threads=2)
end = timer()
print('\ntime(f,2 threads):',(end - start)/f_range,'s/input')

print('---------')
start = timer()
foreach(g,range(g_range),threads=2)
end = timer()
print('\ntime(g,2 threads):',(end - start)/g_range,'s/input')

p = Pool(2)

print('---------')
start = timer()
p.map(f,range(f_range))
end = timer()
print('\ntime(f,2 processes):',(end - start)/f_range,'s/input')

print('---------')
start = timer()
p.map(g,range(g_range))
end = timer()
print('\ntime(g,2 processes):',(end - start)/g_range,'s/input')
