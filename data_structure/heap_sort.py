#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Time:2021/7/14 8:58
# @Author:ZhangFY
# @File:heap_sort.py

# 堆排序
# 堆排序为一种选择排序，最坏，最好，平均复杂度都是O(nlogn),不稳定排序
# 算法核心，从最后的子树开始递归，使得父节点的值最大，最后将首尾元素调换位置
# 算法核心类似希尔排序，只是分组形式不同，思想相同

import random
import time
new_l = []

# 自定义装饰器，返回当前函数执行时间
def timing(func):
    def deact(*args,**kwargs):
        s_time = time.time()
        ref = func(*args,**kwargs)
        e_time = time.time()
        print("{} 函数 执行之间为{}".format(func.__name__,e_time-s_time))
        return ref
    return deact

# 算法核心为递归待排序数据构建的完全二叉树的每个子树，使得每个父节点值为最大
def heap_sort(l):
    # 根据完全二叉树性质，得出所有父节点对应的待排序的数据的索引
    # 最后一个父节点索引为 len(l) // 2 - 1 ，所有父节点列表为 0 到 len(l) // 2 - 1
    # 父节点两个子节点索引值（如果存在的话）左子节点 2*i + 1,右子节点 2*i + 2 其中i 为父节点
    # 每一轮比较涉及所有树的的比较
    # 这里把完全二叉树所有非子叶节点和数组索引进行结合，不需要构造二叉树，但可以利用二叉树的特性进行排序
    global new_l
    last_p_index = len(l) // 2 - 1
    if len(l) == 0:
        return
    while last_p_index >= 0:
        if 2 * last_p_index + 2 < len(l) -1:  # 证明最后一个非子叶节点存在右孩子,此节点必定存在左孩子
            if l[2 * last_p_index + 2] > l[last_p_index]:
                l[2*last_p_index+2],l[last_p_index] = l[last_p_index],l[2*last_p_index+2]   # 交换右孩子
        if l[2 * last_p_index + 1] > l[last_p_index]:
            l[2 * last_p_index + 1], l[last_p_index] = l[last_p_index], l[2 * last_p_index + 1]  # 交换左孩子
        last_p_index -= 1
    new_l.insert(0,l[0])
    l = l[1:]
    heap_sort(l)

if __name__ == '__main__':
    l = [random.randint(5,100) for x in range(300)]
    print(l)
    heap_sort(l)
    print(new_l)
