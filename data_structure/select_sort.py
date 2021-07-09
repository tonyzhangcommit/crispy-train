#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Time:2021/7/6 10:59
# @Author:ZhangFY
# @File:select_sort.py

import random
import time

'''
    选择排序 python 实现方法
    算法核心，类似于冒泡排序算法，每次从无序数据中选出一个最大（小）值，插入到前方有序队列中去
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

def select_way1(l):
    print('排序前:',l)
    for i in range(len(l)-1):
        min = l[i]       # 每一轮循环的最小值
        index = i
        for j in range(i,len(l)):
            if l[j] < min:
                min = l[j]
                index = j
        l[i],l[index] = l[index],l[i]
    print("排序后:",l)


if __name__ == '__main__':
    l = [random.randint(10,100) for x in range(10)]
    select_way1(l)