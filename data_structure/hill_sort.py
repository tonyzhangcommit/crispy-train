#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Time:2021/7/12 19:04
# @Author:ZhangFY
# @File:hill_sort.py

import random
import time

'''
    此文件为希尔排序的python实现
    希尔排序算法核心，是由简单的插入排序进阶改进，又称缩小增量排序，核心操作为首先将待排序队列
    依据某种增量值进行分组，每个分组都进行插入排序，直到增量值为1时，最后执行一遍插入排序完成排序
    希尔排序执行效率远高于普通插入排序
'''

def timer_count(f):
    def decor(*args,**kwargs):
        s_time = time.time()
        r = f(*args,**kwargs)
        e_time = time.time()
        print("{}函数耗时{}秒".format(f.__name__,e_time-s_time))
        return r
    return decor

# 插入排序功能函数,插入排序核心为：单个元素可认为是有序的
@timer_count
def insert_sort(l):
    print("排序前：",l)
    for i in range(1,len(l)):
        j = i
        temp = l[i]
        while j > 0 and l[j-1] > temp:    # 寻找插入位置
            l[j] = l[j-1]
            j -= 1
        l[j] = temp
    print("排序后：",l)

def insert_sort_inside(l):
    for i in range(1,len(l)):
        j = i
        temp = l[i]
        while j > 0 and l[j-1] > temp:    # 寻找插入位置
            l[j] = l[j-1]
            j -= 1
        l[j] = temp

# 这里定义增量为len(l)/2,len(l)/2/2,len(l)/2/2/2.....1
# 希尔排序主要逻辑
@timer_count
def hill_way(l):
    if isinstance(l,list):
        print("排序前",l)
        increment = len(l) // 2
        while increment > 0:
            # 获取当此循环分组个数，分组个数决定下方
            for index in range(increment):
                group_l = []
                index_l = []
                group_num = len(l) // increment  # 获取当前分组个数下每个组中元素个数

                for ti in range(group_num):
                    group_l.append(l[index + ti * increment])     # 根据组数，每个组元素个数，构建分组后的列表
                    index_l.append(index + ti * increment)        # 分组后列表对应原数据的索引，便于排序后逐个替换到原数据中

                insert_sort_inside(group_l)                       # 分组后数据排序
                i = 0
                for index_info in index_l:
                    l[index_info] = group_l[i]                    # 分组后数据替换
                    i += 1
            increment = increment // 2
            if increment == 1:
                insert_sort_inside(l)                             # 最后一轮
                break
        print("排序后",l)
    else:
        raise TypeError("函数hill_way参数类型有误")

if __name__ == '__main__':
    l = [random.randint(5,500) for x in range(250000)]
    import copy
    ll = copy.deepcopy(l)
    # 测试两块执行时间对比
    hill_way(l)
    insert_sort(ll)