#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Time:2021/7/14 8:58
# @Author:ZhangFY
# @File:heap_sort.py

# 堆排序
# 堆排序为一种选择排序，最坏，最好，平均复杂度都是O(nlogn),不稳定排序

import random
import time

# 自定义装饰器，返回当前函数执行时间
def timing(func):
    def deact(*args,**kwargs):
        s_time = time.time()
        ref = func(*args,**kwargs)
        e_time = time.time()
        print("{} 函数 执行之间为{}".format(func.__name__,e_time-s_time))
        return ref
    return deact

def heap_sort(l):
    print('排序前：',l)


if __name__ == '__main__':
    l = [random.randint(5,100) for x in range(30)]
    heap_sort(l)