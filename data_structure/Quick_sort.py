#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Time:2021/6/30 9:07
# @Author:ZhangFY
# @File:Quick_sort.py

# 快速排序python代码实现
import time
import random

# 自定义装饰器
def timer_count(f):
    def decor(*args,**kwargs):
        s_time = time.time()
        r = f(*args,**kwargs)
        e_time = time.time()
        print("{}函数耗时{}秒".format(f.__name__,e_time-s_time))
        return r
    return decor
'''
    快速排序思路：
        递归分治思想，每一轮循环都将待排序列表以某个值进行分割，然后依次递归处理
        实现代码如下：
'''

def quick_sort(l,start,end):
    i = start
    j = end
    # 凡是涉及到递归操作的函数，必须存在一个终止条件
    if i > j:
        return
    while i < j:
        pass
