import multiprocessing
import time

def do_something(pipe):
    
   while True:
        value = pipe.recv()
        print('%s RECEIVED: %s\n' % (multiprocessing.current_process().name, value))
        time.sleep(1)
        pipe.send('ACK')

if __name__ == '__main__':

    data = [2,'Test',[1,2,3]]

    pipe1, pipe2 = multiprocessing.Pipe()
    my_proc = multiprocessing.Process(target=do_something,args=(pipe2,))
    my_proc.start()
    
    for d in data:
        pipe1.send(d)
        value = pipe1.recv()
        print('%s CONFIRMATION received: %s\n' % (multiprocessing.current_process().name, value))

    my_proc.terminate() 

    print('Done')
