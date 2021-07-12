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
'''
# 这里定义增量为len(l)/2,len(l)/2/2,len(l)/2/2/2.....1
# 希尔排序主要逻辑
def hill_way(l):
    Increment = len(l) // 2
    while Increment > 0:

        Increment = Increment // 2
        if Increment == 1:
            break

# 插入排序功能函数,插入排序核心为：单个元素可认为是有序的
def insert_sort(l):
    for i in range(1,len(l)):
        pass

if __name__ == '__main__':
    l = [random.randint(5,50) for x in range(30)]