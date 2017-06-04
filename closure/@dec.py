
def dec(func):
    def in_dec(*args):
        if len(args)==0:
            return 0
        for val in args:
            if not isinstance(val,int):
                return 0
        return func(*args)
    return in_dec
@dec  #my_sum=dec(my_sum)
def my_sum(*args): #my_sum=in_dec
    return sum(args)
@dec
def my_average(*args):
    return sum(args)/len(args)

print(my_sum(1,2,3))
print(my_average(1,2,3,'1'))


def deco(func):
    def in_deco(x,y):
        print('in deco')
        func(x,y)
    print('call deco')
    return in_deco    
#deco(bar) => return in_deco 现在 bar=in_deco 
@deco
def bar(x,y):
    print('in bar',x+y)
#调用bar()就是 调用 in_deco() => in_deco中会接着调用原来作为参数传入的的bar
print(type(bar))
bar(1,2)