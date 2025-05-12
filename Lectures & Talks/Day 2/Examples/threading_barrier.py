import threading
import time
import random

num = 4
bar = threading.Barrier(num)

def do_something():
    
   time.sleep(random.randrange(2, 20))
   print('%s REACHED the barrier\n' % (threading.current_thread().name))
   try:
      bar.wait()
   except:
      pass
   finally:
      print('%s PASSED the barrier\n' % (threading.current_thread().name))

if __name__ == '__main__':

    threads = []

    for i in range(10):
        my_thread = threading.Thread(
            target=do_something, args=())
        threads.append(my_thread)
        my_thread.start()

    time.sleep(30)    
    print("Release stuck jobs by breaking barrier…")
    bar.abort()
