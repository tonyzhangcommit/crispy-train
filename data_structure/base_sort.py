#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Time:2021/7/20 18:20
# @Author:ZhangFY
# @File:base_sort.py

'''
    基数排序，核心思想仍然为大块划分小块进行排序
    实现方法：
    基数排序（radix sort）属于“分配式排序”（distribution sort），又称“桶子法”（bucket sort）或bin sort，
    顾名思义，它是通过键值的部份资讯，将要排序的元素分配至某些“桶”中，藉以达到排序的作用，基
    数排序法是属于稳定性的排序，其时间复杂度为O (nlog(r)m)，其中r为所采取的基数，
    而m为堆数，在某些时候，基数排序法的效率高于其它的稳定性排序法。（来源为百度百科）
'''


import time
import random
import math

# 封装计算函数执行时间装饰器
def calculate_time(func):
    def decor(*args,**kwargs):
        s_time = time.time()
        f = func(*args,**kwargs)
        e_time = time.time()
        print('{} 函数执行共耗时{}'.format(func.__name__,e_time-s_time))
        return f
    return decor

# 算法核心：将待排序整数列表进行循环分桶，分别以个，十，百，千等等顺序进行分组，分组后进行排序
# 实现难点：
# 1、判断当前列表中最大元素的位数（这里 ‘假设’不知道 python 列表 max 函数 或者math 第三方库应用 的前提）,最大位数决定循环次数
# 2、获取未知整数指定位数的数值
# 最低位优先法(Least Significant Digit first)
@calculate_time
def baseSortLSD(l):
    '''
    l：待排序数组
    barrel:桶的数量，默认为10，0 1 2 3 4 5 6 7 8 9
    '''
    # 这里使用python 实现桶排序，并且尽量不使用自带数据类型自带函数 嫌麻烦可以用max函数代替
    print('排序前:',l)
    max_num = 0
    for i in l:
        if i > max_num:
            max_num = i

    # 这里最大数值决定当前循环次数，主要是最大数的位数
    bit_num = 1
    while max_num >= 10**bit_num:
        bit_num += 1

    for bit_index in range(bit_num):
        base_list = [[] for i in range(10)]      # 分桶排序这边都是分为10个桶，0 1 2 3 4 5 6 7 8 9
        for data in l:
            bit_info = data//10**bit_index%10    # 获取指定位数的数值
            base_list[bit_info].append(data)     # 分桶
        l = []
        for base_index in base_list:             # 合并各个桶的数据
            l += base_index
    print('排序后',l)

if __name__ == '__main__':
    l = [random.randint(0,100000000) for x in range(10000000)]
    baseSortLSD(l)