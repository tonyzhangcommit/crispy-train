#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Time:2021/7/19 16:20
# @Author:ZhangFY
# @File:merge_sort.py

'''
    此文件实现归并排序：
    归并排序（MERGE-SORT）是利用归并的思想实现的排序方法，
    该算法采用经典的分治（divide-and-conquer）策略（分治法将问题分(divide)成一些小的问题然后递归求解，
    而治(conquer)的阶段则将分的阶段得到的各答案"修补"在一起，即分而治之)。
'''

import time
import random

def timer(func):
    def deac(*args,**kwargs):
        s_time = time.time()
        re_func = func(*args,**kwargs)
        e_time = time.time()
        print('{}函数耗时{}秒'.format(func.__name__,e_time-s_time))
        return re_func
    return deac

@timer
def merge_way(l):
    print(l)

if __name__ == '__main__':
    l = [random.randint(5,150) for x in range(30)]
    merge_way(l)
