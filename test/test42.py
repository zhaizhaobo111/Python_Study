#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型
#
class Solution:
    def rob(self , nums: List[int]) -> int:
        # write code here
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        def rob_line(start,end):
            # 前两个数之和
            p1=0
            # 前一个数之和
            p2=0
            for i in range(start,end+1):
                cur=max(p2,p1+nums[i])
                p1=p2
                p2=cur
            return p2
        return max(rob_line(0,n-2),rob_line(1,n-1))