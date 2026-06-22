from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        i, j = 0, n - 1
        for p in range(n - 1, -1, -1):
            x = nums[i] * nums[i]
            y = nums[j] * nums[j]
            # 更大的数放右边
            if x > y:
                ans[p] = x
                i += 1
            else:
                ans[p] = y
                j -= 1
        return ans
