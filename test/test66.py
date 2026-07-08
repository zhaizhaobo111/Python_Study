# 最小楼梯书 dp
n=int(input())
cost=list(map(int,input().split()))
a=cost[0]
b=cost[1]
for i in range(2,n):
    c=min(a,b)+cost[i]
    a=b
    b=c
print(min(a,b))
