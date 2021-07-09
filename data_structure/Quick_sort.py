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
    if i >= j:
        return
    stand = l[i]      # 基准数值，一轮循环后以这个数为基准分为两部分，前方都比它小，后方都比它大
    while i < j:
        while i < j and l[j] >= stand:
            j -= 1
        # 这个小循环从后往前找，找到第一个比stand小的数，停止循环，输出当前的索引值
        l[i] = l[j]
        # 这里注意，这一次赋值后，列表中会出现两个l[j]的值，而l[i]被替换
        while i < j and l[i] <= stand:
            i += 1
        # 这个小循环从前往后找，找到第一个比stand大的数，停止循环，输出当前索引值
        l[j] = l[i]
        # 上一步赋值导致的列表中存在两个l[j]值，这一步赋值将后方的l[j]替换为l[i],最终列表中存在两个l[i]

    l[i] = stand
    quick_sort(l,start,i-1)
    quick_sort(l,i+1,end)

if __name__ == '__main__':
    l = [random.randint(10,99) for x in range(60000)]
    # ----------------------------本机测试超6万条数据就会出现栈溢出错误，待优化-----------------------------------------
    print("排序前:",l)
    s_time = time.time()
    quick_sort(l,0,len(l)-1)
    e_time = time.time()
    print("排序后:", l)
    print("{}程序耗时{}".format("快速排序",(e_time-s_time)))
