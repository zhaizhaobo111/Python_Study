import sys

n, k = map(int, input().split())
arr = input().strip()
l = 0
count0 = 0
count1 = 0
toatl = 0
# 扩展右端点
for r in range(n):
    # 不产生 01
    if arr[r] == "0":
        count0 += 1
        # 产生 01
    else:
        count1 += 1
        toatl += count0
    while l < r and toatl > k:
        # 收缩左节点
        if arr[l] == "0":
            toatl -= count1
            count0 -= 1
        else:
            count1 -= 1
        l += 1
    if toatl == k:
        print(l + 1, r + 1)
        exit()
print(-1)




