class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # 按左端点从小到大排序
        intervals.sort(key=lambda x: x[0])
        # 初始化列表
        res = [intervals[0]]
        # c从第二个区间开始
        for start, end in intervals[1:]:
            # 最新的开头 结尾
            last_start, last_end = res[-1]
            if start <= last_end:
                res[-1][1] = max(end, last_end)
            else:
                res.append([start, end])
        return res

