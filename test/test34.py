#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param S string字符串
# @param T string字符串
# @return string字符串
#
class Solution:
    def minWindow(self , s: str, t: str) -> str:
        from collections import Counter
        # write code here
        # 统计t中每个字符需要的个数
        need=Counter(t)
        # 需要的字符总数
        need_count=len(t)
        # 初始化窗口
        left=0
        min_len=float("1000")
        min_start=0
        # 右指针遍历s
        for right in range(len(s)):
            # right满足need其中一个
            if need[s[right]]>0:
                need_count-=1
                # 不管在不在t中都减
            need[s[right]]-=1
            while need_count==0:
                if right-left+1<min_len:
                    min_len=right-left+1
                    min_start=left
                need[s[left]]+=1
                 # 开始收缩左边界
                if need[s[left]]>0:
                     # 左指针右移，释放字符
                    need_count+=1
                left+=1
        if min_len==float("1000"):
            return ""
        return s[min_start:min_start+min_len]
