#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param x int整型
# @return int整型
#
class Solution:
    def mysqrt(self , x: int) -> int:
        # write code here
        left=0
        right=x
        if x==1:
            return 1
        while(left<right):
            mid=int((left+right)/2)
            if mid<=x/mid and mid+1>x/(mid+1):
                return mid
            if mid>x/mid:
                right=mid-1
            else:
                left=mid+1
        return 0