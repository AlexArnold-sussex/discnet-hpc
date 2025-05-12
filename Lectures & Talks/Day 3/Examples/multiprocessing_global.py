import multiprocessing
import threading

def do_something():
	    
   global shared_value

   print('BEFORE shared_value = {}'.format(shared_value))
   shared_value += 1
   print('AFTER shared value = {}\n'.format(shared_value))

if __name__ == '__main__':

    global shared_value
    shared_value = 0

    print('INITIAL: shared_value={}\n'.format(shared_value))

    my_proc = multiprocessing.Process(target=do_something)
    my_proc.start()
    my_proc.join()

    print('PROCESS: shared_value={}\n'.format(shared_value))

    my_thread = threading.Thread(target=do_something)
    my_thread.start()
    my_thread.join()

    print('THREAD shared_value={}\n'.format(shared_value))

    print('Done')
