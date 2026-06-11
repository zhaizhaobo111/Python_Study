class Solution:
    def __init__(self, scores: list[int]):
        # 获取总人数
        self.total = len(scores)
        # 初始化为0
        self.pre = [0] * 751
        # 统计每个分数的人数
        for score in scores:
            self.pre[score] += 1
        # 计算前缀和
        for i in range(1, 751):
            self.pre[i] += self.pre[i - 1]

    def get_my_rank(self, score: int) -> int:
        """查询分数排名"""
        if score < 0 or score > 750:
            return -1
        # 排名 ：总人数-小于等于i +1
        return self.total - self.pre[score] + 1

    def get_rank_count(self, low: int, high: int) -> int:
        """查询区间人数"""
        if low > high:
            return 0
        low = max(0, low)
        high = min(750, high)
        return self.pre[high] - (self.pre[low - 1] if low > 0 else 0)


def test():
    scores = [600, 700, 550, 600, 650, 720, 580, 600, 500, 650]
    sol = Solution(scores)

    print("=" * 50)
    print("测试1：查询分数排名")
    print("=" * 50)
    assert sol.get_my_rank(720) == 1, "720分应该是第1名"
    assert sol.get_my_rank(700) == 2, "700分应该是第2名"
    assert sol.get_my_rank(650) == 3, "650分应该是第3名"
    assert sol.get_my_rank(600) == 5, "600分应该是第5名"
    assert sol.get_my_rank(580) == 8, "580分应该是第8名"
    assert sol.get_my_rank(550) == 9, "550分应该是第9名"
    assert sol.get_my_rank(500) == 10, "500分应该是第10名"
    print("✅ 排名测试通过")

    print()
    print("=" * 50)
    print("测试2：查询区间人数")
    print("=" * 50)
    assert sol.get_rank_count(600, 700) == 6, "600-700分应该有6人"
    assert sol.get_rank_count(600, 600) == 3, "600分应该有3人"
    assert sol.get_rank_count(650, 650) == 2, "650分应该有2人"
    assert sol.get_rank_count(500, 600) == 6, "500-600分应该有6人"
    assert sol.get_rank_count(0, 750) == 10, "0-750分应该有10人"
    print("✅ 区间测试通过")

    print()
    print("=" * 50)
    print("🎉 所有测试通过！")
    print("=" * 50)


if __name__ == "__main__":
    test()
