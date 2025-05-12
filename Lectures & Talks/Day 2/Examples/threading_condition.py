import threading 
import time
 
def create(cond):
    
    while True:
        time.sleep(3)
        print('%s: New item PRODUCED\n' % (threading.current_thread().name))
	  
        with cond: 
                cond.notify() 
                time.sleep(3)
                print('%s: Item AVAILABLE\n' % (threading.current_thread().name))
  
def consume(cond):
    
    while True:
        with cond:
                print('%s: WAITING for new item ...\n' % (threading.current_thread().name))
                cond.wait()
                print('%s: CONSUMING new item\n' % (threading.current_thread().name))
        time.sleep(8)
 
if __name__ == '__main__':
    
    cond = threading.Condition()

    thread_producer = threading.Thread(target=create, name='producer',  
                                       args=(cond,))
    thread_consumer1 = threading.Thread(target=consume, args=(cond,))
    thread_consumer2 = threading.Thread(target=consume, args=(cond,))    

    thread_producer.start()
    thread_consumer1.start()
    thread_consumer2.start()
