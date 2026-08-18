#最长无重复的字串
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口+双指针
        s_set=set()
        left=0
        max_len=0
        for right in range(len(s)):
            while s[right] in s_set:
                s_set.remove(s[left])
                left+=1
            s_set.add(s[right])
            max_len=max(max_len,right-left+1)
        return max_len