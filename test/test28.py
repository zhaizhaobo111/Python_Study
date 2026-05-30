# 最大子段和 ：
# https://www.nowcoder.com/practice/f04519cd1d904f50b68f4229a126ab08?
# tpId=389&tqId=10766281&sourceUrl=%2Fexam%2Foj
n=int(input())
arr=list(map(int,input().split()))
# 目前最大
cur_sum=arr[0]
# 最后最大的
max_sum=arr[0]
for i in range(1,n):
    #  cur_sum每次与现在的arr【i】比较，负数就重新选择，正数继续
    cur_sum=max(arr[i],cur_sum)
    # 取最后最大
    max_sum=max(cur_sum,max_sum)
print(max_sum)