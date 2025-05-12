import multiprocessing
import time
 
def do_something(q):
    
    while True:
        data = q.get()
        time.sleep(1)
        print('data found to be PROCESSED: {}'.format(data))       
        q.task_done()
 
 
if __name__ == '__main__':

    q = multiprocessing.JoinableQueue()
   
    data = [pow(2,i) for i in range(10)]

    process_consumer = multiprocessing.Process(target=do_something, args=(q,))
    process_consumer.start()
     
    for d in data:
        q.put(d)

    q.join()

    process_consumer.terminate()

    print("Done")
