import multiprocessing
import threading

def do_something(shared_value):	    

   print('BEFORE shared_value = {}'.format(shared_value.value))
   shared_value.value += 1
   print('AFTER shared value = {}\n'.format(shared_value.value))

if __name__ == '__main__':
    
    shared_value = multiprocessing.Value('i',0)

    print('INITIAL: shared_value={}\n'.format(shared_value.value))

    my_proc = multiprocessing.Process(target=do_something,args=(shared_value,))
    my_proc.start()
    my_proc.join()

    print('PROCESS: shared_value={}\n'.format(shared_value.value))    

    my_thread = threading.Thread(target=do_something,args=(shared_value,))
    my_thread.start()
    my_thread.join()

    print('THREAD shared_value={}\n'.format(shared_value.value))

    print('Done')
