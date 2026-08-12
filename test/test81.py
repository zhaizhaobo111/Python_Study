# 给你一个字符串
# s，请你将
# s
# 分割成一些
# 子串，使每个子串都是
# 回文串 。返回
# s
# 所有可能的分割方案。
#
#
#
# 示例
# 1：
#
# 输入：s = "aab"
# 输出：[["a", "a", "b"], ["aa", "b"]]
# 示例
# 2：
#
# 输入：s = "a"
# 输出：[["a"]]
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        res=[]
        def isBack(start,path):
            if start==n:
                res.append(path[:])
                return
            for end in range(start,n):
                sub=s[start:end+1]
                if sub==sub[::-1]:
                    path.append(sub)
                    isBack(n+1,path)
                    path.pop()
        isBack(0,[])
        return res