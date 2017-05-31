# from multiprocessing import Process
# import os

# def run_proc(name):
#     print('Run child process \'%s\'(%s)...'%(name,os.getpid()))

# if __name__ == '__main__':
#     print('Parent process %s'% os.getpid())
#     p=Process(target=run_proc,args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end')


#Pool的使用

# from multiprocessing import Pool
# import time,os,random

# def run_sleep(name):
#     print('run task %s (%s)'%(name,os.getpid()))
#     start=time.time()
#     time.sleep(random.random()*3)
#     end=time.time()
#     print('Process %s runs  %.2f second'%(name,(end-start)))

# if __name__ == '__main__':
#     print('Parent process %s'%os.getpid())
#     p=Pool(4)
#     for x in range(8):
#         p.apply_async(run_sleep,args=(x,))
#     print('waiting for all subprocesses done...')
#     #对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
#     p.close()
#     p.join()
#     print('All processes  done')



# import subprocess
# print('$ nslookup www.python.org')
# r=subprocess.call(['nslookup','www.python.org'])
# print(r)

# import subprocess

# print('$ nslookup')
# p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code',p.returncode)

# import subprocess

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('GBK'))
# print('Exit code:', p.returncode)


from multiprocessing import Process,Queue
import time,random,os

def write(q):
    print('write process(%s) start'% os.getpid())
    for value in ['a','b','c']:
        print('put %s to queue'% value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('read process(%s) start'% os.getpid())
    while True:
        value=q.get(True)
        print('get %s from queue'%value)

if __name__ == '__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()