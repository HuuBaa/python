import random,queue,time
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support


task_queue=queue.Queue()
result_queue=queue.Queue()

def r_task_queue():
    return task_queue
def r_result_queue():
    return result_queue
class QueueManager(BaseManager):
    pass

def test():
    QueueManager.register('get_task_queue',callable=r_task_queue)
    QueueManager.register('get_result_queue',callable=r_result_queue)

    manager=QueueManager(address=('127.0.0.1',5000), authkey=b'huu')
    manager.start()
    task = manager.get_task_queue()
    result= manager.get_result_queue()
    
    for i in range(10): 
        n=random.randint(0,10000)
        print('Put task%s'%n)
        task.put(n)
    print('Try get result...')

    for i in range(10):
        r=result.get(timeout=10)
        print('result: %s'%r)
    manager.shutdown()
    print('manager exit')


if __name__ == '__main__':
    #freeze_support()
    test()