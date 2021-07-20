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
    核心思想：单个元素的列表可认为是有序列表，所谓分治，就是将大组无序队列按某种规则进行拆分，排序后在进行组合，类似相同思想有
    希尔排序，堆排序，还有当前的归并排序
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

# 递归分组函数，将原数据分为两块，然后一直往下进行划分
def mergeSort(l):
    if len(l) <= 1:
        # 涉及递归操作的函数，必须有停止递归条件
        return l
    middle = len(l) // 2
    left = mergeSort(l[:middle])
    right = mergeSort(l[middle:])
    return merge_list(left,right)

# 合并函数，将两个无序列表合并成一个有序列表
# 涉及到递归操作内部函数，不宜采用原列表元素互换方式，采用新建空列表进行保存
# 这里面进行合并的两个列表的特点，都是“有序”的，假如划分到最后，两边都只有一个元素，一个元素我们可以认为是有序的
def merge_list(left,right):
    l_sorted = []
    l = r = 0
    # 这里的循环基于两个有序列表合并较好理解（最开始执行是两个元素的执行）
    # 这里面l r 分别为索引
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            l_sorted.append(left[l])
            l += 1
        else:
            l_sorted.append(right[r])
            r += 1
    # 执行完此次循环，此时必定有一个列表中元素全部增加到l_sorted，而另外一个列表中只剩下最大的几项没有增加到l_sorted
    if l == len(left):
        # 代表left列表中元素全部合并完毕
        # 此时right还剩下若干元素没有合并，并且剩下的几个元素相对于其他为最大
        for i in right[r:]:
            l_sorted.append(i)
    else:
        for j in left[l:]:
            l_sorted.append(j)
    return l_sorted



if __name__ == '__main__':
    l = [random.randint(5,5000000) for x in range(80000)]
    print(l)
    new_l = mergeSort(l)
    print(new_l)