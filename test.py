# def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# print(char2num('2'))



# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from functools import reduce

# def str2float(s):
#     def str2num(str):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[str]
#     s1=s.split('.')[0]
#     s2=s.split('.')[1]
#     L1 = list(map(str2num,s1))   
#     L2 = list(map(str2num,s2))   
#     def add2num(x,y):
#         return 10*x+y
#     return reduce(add2num,L2,0.0)*10**-len(L2)+reduce(add2num,L1,0.0)


# print(str2float('123.456'))
# print(str2float('123.45600'))
# print(str2float('0.1234'))
# print(str2float('.1234'))
# print(str2float('120.0034'))

# def not_empty(s):
#     return s and s.strip()

# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# def odd_list():
#     n=1
#     while True:
#         n=n+2
#         yield n

# def num_filter(n):
#     return lambda x:x % n>0

# def primes():
#     yield 2
#     it = odd_list()
#     while True:
#         n=next(it)
#         yield n
#         it=filter(num_filter(n),it)

# for n in primes():
#     if n<1000:
#         print(n)
#     else:
#         break


# print(list(
#     filter(lambda x:str(x)==str(x)[::-1], range(1, 1000))))

# def build(x,y): 
#     return lambda:x*x+y*y 
# f=build(1,2) 
# print(f())



# import functools
# def log(text=''):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kw):
#             print('%sbegin call %s:'%(text,func.__name__))           
#             func(*args,**kw)
#             print('%send call %s:'%(text,func.__name__))                     
#         return wrapper
#     return decorator

# @log('execute: ')  #等于wname=log(wname)
# def wname():
#     print("Huu is me")

# wname()


# import functools
# int2 = functools.partial(int,base=2)

# print(int2('101010'))


# class Student(object):
#     def __init__(self,name,score):
#         self.__name=name
#         self.__score=score
#     def print_score(self):
#         print(self.__name+':'+str(self.__score))
#     def get_name(self):
#         return self.__name
#     def get_score(self):
#         return self.__score

#     def get_grade(self):
#         if self.__score > 90:
#             print('A')
#         elif self.score >60:
#             print('B')
#         else:
#             print('C')



# Huu=Student('Huu',100)
# Huu2=Student('Huu',666)

# Huu2.print_score()
# print(Huu.get_name())
# print(Huu.get_score())
# Huu.get_grade()




# class Animal(object):
#     def run(self):
#         print('Animal is running')


# class Cat(Animal):
#     def run(self):
#         print('Cat is running')       
#     def eat(self):
#         print('Cat is eating')

# cat1 = Cat()
# cat1.run()
# cat1.eat()

# class ClassName(object):
#     """docstring for ClassName"""
#     def __init__(self, arg):
#         super(ClassName, self).__init__()
#         self.arg = arg

# class Myobject(object):
#     def __init__(self,x):
#         self.x=x

# class Myobject1(object):
#     def __init__(self,x):
#         self.__x=x

# obj = Myobject(11)
# obj1=Myobject1(11)

# setattr(Myobject,'test',lambda self,x:self.x*x)
# print(obj.test(3))

# print(hasattr(obj,'x'))
# print(getattr(obj,'x'))
# print(hasattr(obj1,'__x'))

# print(isinstance(1,int))


# class Student(object):
#     __slots__=('name','age','job')
#     studentsNum=0
#     def __init__(self,name):
#         self.name=name


# def register(name,**kw):
#     student = Student(name)
#     Student.studentsNum +=1
#     for k,v in kw.items():
#         setattr(student,k,v)
#     return student

# Huu=register('Huu',age=24,job='coder')
# Student.sch='njue'
# print(Student.sch)
# print(Huu.age)
# print(Huu.job)
# print(Student.studentsNum)



# class A(object):
#     def run(self):
#         print("A is runng")

# class BMixIn(object):
#     def eat(self):
#         print('B is eating')


# class C(A,BMixIn):
#     pass

# c=C()

# c.run()
# c.eat()



# class Chain():
#     def __init__(self,path=''):
#         self._path=path
#     def __getattr__(self,path):
#         return Chain('%s/%s'%(self._path,path))
#     def __str__(self):
#         return self._path
#     def __len__(self):
#         return 6
#     __repr__=__str__

# ch=Chain()
# print(ch.list.huu.hereb,len(ch))




# class Fib(object):
#     def __getitem__(self,n):
#         if isinstance(n,int):
#             a,b=1,1
#             for i in range(n):
#                 a,b=b,a+b
#             return a
#         if isinstance(n,slice):
#             stop=n.stop
#             start=n.start
#             if start==None:
#                 start=0
#             a,b=1,1
#             l=[]
#             for i in range(stop):
#                 if i>=start:                   
#                     l.append(a)
#                 a,b=b,a+b   
#             return l

#     def __call__(self):
#         return print('My name is')

# fib=Fib()
# fib()
# print(fib[5:10])

# print(list(range(100))[5:10])



# from enum import Enum
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for member in Month.__members__.items():
#     print(member)
# Jan=Month.Jan
# print(Jan)



# class A():
#     pass




# def sayhi(self,name='world'):
#     print('Hi,%s'%name)

# Hello=type('Hello',(object,),dict(hello=sayhi)) 

# h=Hello()
# h.hello()



# age=20
# print(age.__class__)
# print(A.__class__)


# try:
#     b=int('b')
#     a= 10/b
#     print('redult:',a)
# except ZeroDivisionError as e:
#     print('error:',e)
# except ValueError as e:
#     print(e)
# finally:
#     print('end')




# import logging

# def A(s):
#     return 10/int(s)

# def B(s):
#     return A(s) *2

# def main(s):
#     try:
#         B(s)
#     except Exception as e:
#         logging.exception(e)

# main(0)
# print('end')



# class FooError(ValueError):
#     pass

# def bar(s):
#     if int(s)==0:
#         raise FooError('my error')
#     return 10/int(s)
# bar('0')



# def foo(s):
#     a=int(s)
#     if a==0:
#         raise ValueError('a can not be zero')
#     return 10/a

# def bar():
#    a=0
#    try:
#         foo(a)
#    except ValueError as e:
#         print('zero ERROR')
#         #raise
# bar() 


# import logging
# logging.basicConfig(level=logging.DEBUG)
# def foo(s):
#     a=int(s)
#     logging.debug('a=%d'%a)
#     logging.info('a=%d'%a)
#     logging.warning('a=%d'%a)
#     logging.error('a=%d'%a)  
#     return 10/a

# def main():
#     foo(0)

# main()



# import pdb
# s='0'
# n=int(s)
# pdb.set_trace()
# print(10/n)




# class Dict(dict):
#     def __init__(self,**kw):
#         super().__init__(self,**kw)
#     def __getattr__(self,key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict'object has no attribute '%s'"%key)
#     def __setattr__(self,key,value):
#         self[key]=value

# d=Dict(a=1,b=2)

# d.c=6

# if __name__ == '__main__':  
#     print(d['c'])




# print(os.name)
# #os.uname() #windows无效
# print(os.environ.get('x','default'))
# print(os.path.abspath('.'))

# mydir=os.path.join(os.path.abspath('.'),'testdir')
# print(mydir)

# dirlist=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
# print(dirlist)



# from datetime import datetime
# import os

# pwd = os.path.abspath('.')

# print('      Size     Last Modified  Name')
# print('------------------------------------------------------------')

# for f in os.listdir(pwd):
#     fsize = os.path.getsize(f)
#     mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
#     flag = '/' if os.path.isdir(f) else ''
# print('%10d  %s  %s%s' % (fsize, mtime, f, flag))


# import json
# d= dict(name='huu',age=24)
# f=open('HUU.txt','w')
# json.dump(d,f)
# f.close()
# print(json.dumps(d))

# f=open('HUU.txt','r')
# print(json.load(f))

# f.close()


passline = 60
def func(val):
    print('%x'%id(val))
    if val < 60:
        print('faile')
    if val >=60:
        print('pass')
    def in_func():
        print(val)
    in_func()
    return in_func

f=func(60)
f()
print(f.__closure__)