class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(l: int, r: int):
            while (l < r):
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        # 去掉多余整圈
        k %= n
        # [1,2,3,4,5,6,7]
        # 1.反转A[7,6,5]+B[4,3,2,1]
        reverse(0, n - 1)
        # 2.反转 A [5,6,7]
        reverse(0, k - 1)
        # 3.反转 B [1,2,3,4]
        reverse(k, n - 1)
