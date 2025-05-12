from timeit import timeit
from numba import vectorize, float64, jit
import numpy as np

N = int(100)

# @vectorize([float64(float64, float64)])
# @jit
def f(x, y):
    tmp = x
    for i in range(N):
        tmp += y
    return tmp

# @jit
def g():
    for i in range(N):
        f(np.ones(i), np.arange(i))

# f(np.zeros(0), np.zeros(0)), g()

time = timeit(lambda: f(np.ones(N), np.arange(N)), number=N)
print(f"Done. time (f)={time:.4f}")

time = timeit(g, number=N)
print(f"Done. time (g)={time:.4f}")
