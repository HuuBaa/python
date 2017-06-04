 
# passline = 60
# def func(val):
#     print('%x'%id(val))
#     if val < passline:
#         print('faile')
#     if val >=passline:
#         print('pass')
#     def in_func():
#         print(val)
#     in_func()
#     return in_func

# f=func(60)
# f()
# print(f.__closure__)





# def func_150(val):
#     passline=90
#     if val < passline:
#         print('%d faile'%val)
#     if val >=passline:
#         print('%d pass'%val)
# def func_100(val):
#     passline=60
#     if val < passline:
#         print('%d faile'%val)
#     if val >=passline:
#         print('%d pass'%val)

# func_150(89)
# func_100(89)


def set_passline(passline):
    def comp(val):#把passline添加到__closure__中
        if val>=passline:
            print('pass')
        else:
            print('faile')
    return comp
f_100=set_passline(60)
f_150=set_passline(90)
#print(type(f_100))
#print(f_100.__closure__)#passline60
f_100(89)
f_100(59)

f_150(89)



def my_sum(*args):
    return sum(args)
def my_average(*args):
    return sum(args)/len(args)
def dec(func):
    def in_dec(*args):
        if len(args)==0:
            return 0
        for val in args:
            if not isinstance(val,int):
                return 0
        return func(*args)
    return in_dec
my_sum = dec(my_sum)
my_average=dec(my_average)
print(my_sum(1,2,3,4,5))
print(my_sum(1,2,3,4,5,'6'))
print(my_average(1,2,3,4,5))
print(my_average())


def outer(val):
    print("val's id:%x"%id(val))
    def inner():
        print(val)
    return inner
f=outer(1)
print(f.__closure__)
