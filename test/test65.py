# 数组中两个字符串的最⼩距离（模拟 + 贪⼼）
n=int(input())
str_arr=input().split()
s1=str_arr[0]
s2=str_arr[1]
pre1=-1
pre2=-1
res=float('inf')
for i in range(n):
    s=input()
    if s==s1:
    # 当前匹配s1，若之前出现过s2计算距离
    if pre2!=-1:
        res=min(res,i-pre2)
    pre2=i
    if s == s2:
        # 当前匹配s1，若之前出现过s2计算距离
        if pre1 != -1:
            res = min(res, i - pre1)
    pre1 = i
print(-1 if res==float("inf")else res)