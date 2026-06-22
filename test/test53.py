from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        swap = 1
        no_swap = 0

        for i in range(1, n):
            temp_no_swap = float('inf')
            temp_swap = float('inf')
            # 位置不交换
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                temp_no_swap = no_swap
                temp_swap = swap + 1

            # 位置交换
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                temp_no_swap = min(temp_no_swap, swap)
                temp_swap = min(temp_swap, no_swap + 1)

            no_swap, swap = temp_no_swap, temp_swap

        return min(no_swap, swap)