#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Time:2021/7/6 17:25
# @Author:ZhangFY
# @File:insert_sort.py
import random
import time
'''
    插入排序 python 实现过程
    算法核心，单个元素可认为是有序队列,插入过程为单个元素操作
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

# 普通插入排序
def insert_way1(l):
    print('排序前',l)
    for i in range(1,len(l)):   # 当前第一个元素可认为有序序列
        j = i
        x = l[i]       # 待插入的数值
        while j > 0 and l[j-1] > x:
            l[j] = l[j-1]
            j -= 1
        l[j] = x
    print('排序后',l)



if __name__ == '__main__':
    insert_way1(l)