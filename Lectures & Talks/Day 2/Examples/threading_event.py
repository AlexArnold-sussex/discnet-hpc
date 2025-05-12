import threading
import queue
import time
 
def create(data, q):
    
    #Creates data to be consumed and waits for the consumer to finish processing
    
    print('Creating data and putting it on the queue')
    for item in data:
        time.sleep(0.5)
        q.put(item)
 
        print('data CREATED: {}'.format(item))        
 
 
def consume(q, evt):
    
    #Consumes some data and works on it
    #In this case, all it does is double the input
    
    while True:
        try:
            data = q.get(timeout=5)
        except:
            print('Timeout! No new data found!')
            evt.set()

        time.sleep(1)
        print('data found to be PROCESSED: {}'.format(data))
        processed = data * 2
        print(processed)	
 
if __name__ == '__main__':
    q = queue.Queue()
    evt = threading.Event()
   
    data = range(10)
    thread_creator = threading.Thread(target=create, args=(data, q))
    thread_consumer = threading.Thread(target=consume, args=(q, evt,))
    thread_consumer.daemon = True
    thread_creator.start()
    thread_consumer.start()
     
    time.sleep(2)
    evt.wait()
    print("Done")
