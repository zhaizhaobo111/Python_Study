import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
          n = len(nums)
          # 第 k 大 = 第 (n - k) 小（0-indexed）
          target = n - k
          def quickselect(left: int, right: int) -> int:
              """返回 nums 中第 target 小的元素"""
              if left == right:
                  return nums[left]

              # 随机选择 pivot
              pivot_idx = left + random.randint(0, right - left)
              pivot = nums[pivot_idx]

              # 三路分区：将数组分为 < pivot, == pivot, > pivot 三部分
              # [left, lt) < pivot
              # [lt, gt) == pivot
              # [gt, right] > pivot
              lt = left      # 小于 pivot 的右边界
              i = left       # 当前指针
              gt = right + 1 # 大于 pivot 的左边界

              while i < gt:
                  if nums[i] < pivot:
                      nums[lt], nums[i] = nums[i], nums[lt]
                      lt += 1
                      i += 1
                  elif nums[i] > pivot:
                      gt -= 1
                      nums[i], nums[gt] = nums[gt], nums[i]
                  else:
                      i += 1

              # 现在 [lt, gt) 是等于 pivot 的部分
              if target < lt:
                  return quickselect(left, lt - 1)
              elif target >= gt:
                  return quickselect(gt, right)
              else:
                  # target 在 [lt, gt) 范围内，直接返回 pivot
                  return pivot

          return quickselect(0, n - 1)