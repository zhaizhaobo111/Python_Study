# n,x=map(int,input().split())
# a=list(map(int,input().split()))
# l=0
# sum=0
# min_len=float("inf")
# cur_len=0
# res_l=0
# res_r=0
# for r in range(n):
#     sum+=a[r]
#     while(sum>=x):
#         cur_len=r-l+1
#         if(cur_len<min_len):
#             min_len=cur_len
#             res_l=l
#             res_r=r
#         sum-=a[l]
#         l+=1
# print(res_l+1,res_r+1)
import sys

data=sys.stdin.read().split()
p=0
n=int(data[p])
p+=1
x=int(data[p])
p+=1

l=0
sum=0
min_len=float("inf")
cur_len=0
res_l=0
res_r=0
for r in range(n):
    num=int(data[p])
    p+=1
    sum+=num
    while sum>=x:
        cur_len=r-l+1
        if cur_len<min_len:
            min_len=cur_len
            res_l=l
            res_r=r
        left_num=int(data[p-cur_len])
        sum-=left_num
        l+=1
print(res_l+1,res_r+1)