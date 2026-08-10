# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
# 示例 1：
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 示例 2：
#
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
# 示例 3：
#
# 输入：nums = [1,0,1,2]
# 输出：3
# 求最长连续序列
from typing import List


def long(nums:List[int])->int:
    # 定义哈希
    arr_set=set(nums)
    res=0
    for i in arr_set:
        # i-1不在哈希表中 i就是起点
        if i-1 not in arr_set:
            arr_nums=i
            arr_len=1
            # i+1在哈希表中，说明是连续序列
            while arr_nums+1 in arr_set:
                arr_nums+=1
                arr_len+=1
            res=max(res,arr_len)
    return res
