from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        res=0
        # 以建造的桥右端点
        cur_end=0
        # 下一座桥的最大值
        next_end=0
        for i in range(len(nums)-1):
            # 遍历的过程中，记录下一座桥的最远点
            next_end=max(next_end,i+nums[i])
            if i==cur_end:# 无路可走，必须建桥
                cur_end=next_end
                res=res+1
        return res
