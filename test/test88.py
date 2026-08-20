from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        if m < n:
            return []

        p_count = [0] * 26
        window_count = [0] * 26

        # 统计 p 和第一个窗口
        for ch in p:
            p_count[ord(ch) - 97] += 1
        for i in range(n):
            window_count[ord(s[i]) - 97] += 1

        res = []
        if p_count == window_count:
            res.append(0)

        # 滑动窗口
        for i in range(n, m):
            # 加入新字符（窗口右端）
            window_count[ord(s[i]) - 97] += 1
            # 移除左端字符
            window_count[ord(s[i - n]) - 97] -= 1
            # 比较两个计数器
            if p_count == window_count:
                res.append(i - n + 1)
        return res