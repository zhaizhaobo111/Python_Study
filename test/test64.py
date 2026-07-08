import math
# 牛牛的快递
a,b=input().split()
weight=float(a)
res=0

if weight<=1:
    res=20
else:
    over=math.ceil(weight-1)
    res=20+over
if b=="y":
    res+=5
print(res)