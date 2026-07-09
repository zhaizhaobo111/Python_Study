n,x=map(int,input().split())
arr=list(map(int,input().split()))
# 区间内数字和
sum=0
left=0
res_left=0
res_right=0
cur_len=0
min_len=float("inf")
for right in range(n):
    sum+=arr[right]
    # 满足左边界
    while(sum>=x):
        cur_len=right-left+1
        if cur_len<min_len:
            min_len=cur_len
            res_left=left
            res_right=right
        # 左指针右移，把左边数字移出窗口，总和减小
        sum-=arr[left]
        left+=1
print(res_left+1,res_right+1)
