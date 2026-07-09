import heapq

n, k = map(int, input().split())
# 读取数组
arr = list(map(int, input().split()))

heap = []
total = 0
# 构建大根堆（存负数），同时计算原始总和
for num in arr:
    total += num
    heapq.heappush(heap, -num)

# 最多k次操作
while k > 0:
    cur = -heapq.heappop(heap)
    # 当前是奇数，无法再分割，全部数字都不能操作了，直接退出
    if cur % 2 != 0:
        heapq.heappush(heap, -cur)
        break
    # 操作一次，总和减少的数值
    diff = cur - cur // 2
    total -= diff
    new_num = cur // 2
    heapq.heappush(heap, -new_num)
    k -= 1

print(total)