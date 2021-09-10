
# 本文件主要用Python实现几种基本的排序算法
import unittest
import time
from random import randint  # 使用randint产生随机整数


#冒泡排序的思想：第一个元素和第二个元素比较，如果大于/小于就交换，否则不变，
# 然后，第二个再开始和第三个比较，以此类推。

# 冒泡排序
def bubble_sort(list1):
    start = time.time() # 记录开始时间
    number = len(list1)  # 数组的长度
    has_changed = True  # 一趟遍历中是否发生过交换
    x = 0
    if number == 0:
        return none
    while has_changed:
        has_changed = False  # 每次循环复位
        for i in range(1, number - x):  # 每次循环减少一次，因为后面的数列已经是有序
            if list1[i - 1] > list1[i]:
                list1[i - 1], list1[i] = list1[i], list1[i - 1]  # 交换位置
                has_changed = True
        x += 1
    operation_time =time.time() - start
    return list1, operation_time

list1 = [123,324,44,2,24]
result = bubble_sort(list1)
# print(result)



#插入排序  假设原有数列是一个有序数列，插入一个值，让其符合原有顺序

def insertOrder(list):

    number = len(list1)
    if number == 0:
        return none
    for i in range(1,len(list)):
        j = i;
        while list[j-1] > list[j]:
            list[j-1],list[j] = list[j],list[j-1]
            j -=1
            if j < 1:
                break
    return list

list2 = [123,324,44,2,24]
result = insertOrder(list2)
# print(result)


#选择排序  选择排序是将列表遍历N-1遍，第一遍遍历N个元素，将min/max放在最左作为A1
#第二遍遍历剩下的N-1个，将min/max放在A1右边，以此类推

def quickOrder(list):

    if len(list) == 0:
        return none
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i] < list[j]:
                list[i],list[j] = list[j],list[i]
    return list



list3 = [123,324,44,2,24]
result = quickOrder(list3)
# print(result)


#归并排序  将一个列表通过递归切割成无法继续切割的多组左右两个部分（二叉树）
#然后将左右两个部分分别排序作为一个一个新的左或者右和上一层级的右或左继续排列
#最后将所有的结果合并
def merge_sort(lst):
    if len(lst) <= 1:
        return lst          # 从递归中返回长度为1的序列

    middle = int(len(lst) / 2)
    left = merge_sort(lst[:middle])     # 通过不断递归，将原始序列拆分成n个小序列
    right = merge_sort(lst[middle:])
    result = merge(left, right)
    return result
def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):  # 比较传入的两个子序列，对两个子序列进行排序
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1;
    result.extend(left[i:])         # 将排好序的子序列合并
    result.extend(right[j:])
    return result

list4 = [12,3,13,24,23,523,4,34123,34]
finalResult = merge_sort(list4)
print(finalResult)




