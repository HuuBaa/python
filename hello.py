#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# name = input('please enter your name:')
# print ('hello,',name)

# a=100
# if a>=0:
#     print(a)
# else:
#     print(-a)

# print('''n=123
# f=456.789
# s1=\'Hello,world\'
# s2=\'Hello,\\\'Adam\\\'\'
# s3 = r\'Hello, \"Bart\"\'
# s4=r\'\'\'Hello,\nLisa!\'\'\'''')

# print("胡邦")

# def my_abs(x):
#     if not isinstance(x, (int,float)):
#         raise TypeError('bad operand type')
#     if x > 0:
#         return x
#     else:
#         return -x

import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('bad operand type')
    if not isinstance(b,(int,float)):
        raise TypeError('bad operand type')
    if not isinstance(c,(int,float)):
        raise TypeError('bad operand type')

    if a==0 and b!=0:
        return -c/b
    elif a==0 and b==0 and c==0:
        return '无穷多的解' 
    elif a==0 and b==0 and c!=0:
        return '无解'
    else:
        if b**2-4*a*c < 0:
            return '无实数根'
        if b**2-4*a*c == 0:
            x = (-b+math.sqrt(b*b-4*a*c))/(2*a)
            return x
        else:
            x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
            x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
            return x1 , x2

print(quadratic(0,2,3))
print(quadratic(0,0,0))
print(quadratic(0,0,1))
print(quadratic(2,3,4))
print(quadratic(1,2,1))
print(quadratic(1,2,0.5))
print(quadratic('h',1,2,))

