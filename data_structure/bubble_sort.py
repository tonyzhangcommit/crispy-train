#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Time:2021/7/6 10:58
# @Author:ZhangFY
# @File:bubble_sort.py
import random
import time
'''
    冒泡排序python实现
    基本实现原理：每一次遍历选出最大（最小）值
'''
# 自定义装饰器
def timer_count(f):
    def decor(*args,**kwargs):
        s_time = time.time()
        r = f(*args,**kwargs)
        e_time = time.time()
        print("{}函数耗时{}秒".format(f.__name__,e_time-s_time))
        return r
    return decor

l = [random.randint(0,30) for x in range(20)]

# 最普通冒泡排序，升序，数据随机
@timer_count
def bullle_way1(l):
    print('排序前',l)
    for i in range(len(l)-1):
        for j in range(i,len(l)):
            if l[i] > l[j]:
                t = l[i]
                l[i] = l[j]
                l[j] = t
    print('排序后',l)

# 对前方部分无序，到达某个值后有序的冒泡排序方法
@timer_count
def bullle_way2(l):
    print('排序前', l)
    for i in range(len(l)-1):
        for j in range(i,len(l)):
            onoff = True
            while onoff:
                onoff = False
                if l[i] > l[j]:
                    onoff = True
                    t = l[i]
                    l[i] = l[j]
                    l[j] = t
    print('排序后', l)


if __name__ == '__main__':
    bullle_way1(l)
    bullle_way2(l)
