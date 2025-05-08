import threading
import numpy
import time

maxThreads = 4

N = 10000

chunk = int(N/10)
result = 0.0

a = numpy.array([i for i in range(N)])
b = numpy.array([i*2 for i in range(N)])

sem  = threading.Semaphore(maxThreads) # semaphore is used to ensure maximum amount of threads
lock = threading.Lock()

def calc(start, end):
    global result   
 
    tmp = numpy.sum(a[start:end] * b[start:end])
    with lock:
        result = result + tmp    

    sem.release()  # release / count down semaphore

if __name__ == '__main__':

    threads = []

    nRemain = N
    while nRemain>0:
        sem.acquire() # acquire / count up semaphore  
        start = N-nRemain
        end = min(N,N-nRemain+chunk)
        my_thread = threading.Thread(target=calc,args=(start,end,))
        my_thread.start()        
        threads.append(my_thread)
        nRemain -= end-start        

    for t in threads:
        t.join()

    print('Final result = %d' % (result))
        

    
