# import threading,time
# def loop():
#     print('thread %s is running.'%threading.current_thread().name)
#     for n in range(5):
#         print('thread %s >>>%s'%(threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s ended'%threading.current_thread().name)

# print('thread %s is running.'%threading.current_thread().name)
# t=threading.Thread(target=loop,name='loopthread')
# t.start()
# t.join()
# print('thread %s ended'%threading.current_thread().name)




# import threading
# money=0
# lock=threading.Lock()
# def change(n):
#     global money
#     money =money + n
#     money =money - n
# def run_thread(n):
#     for i in range(100000):
#         lock.acquire()
#         try:
#             change(n)
#         finally:
#             lock.release()
# t1=threading.Thread(target=run_thread,args=(5,))
# t2=threading.Thread(target=run_thread,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(money)



import threading
local_school=threading.local()

def student():
    std=local_school.student
    print('%s in %s'%(std,threading.current_thread().name))
def thread(name):
    local_school.student=name
    student()

if __name__ == '__main__':
    t1=threading.Thread(target=thread,args=('Huu1',),name='thread1')
    t2=threading.Thread(target=thread,args=('Huu2',),name='thread2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
