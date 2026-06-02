# 【小红的01子序列构造(easy)】https://www.nowcoder.com/practice/ee0b6c6baa2642c182df8b4390126f9a?tpId=386&tqId=11105316&sourceUrl=%2Fexam%2Foj%3FquestionJobId%3D10%26subTabName%3Donline_coding_page
import sys
n,k=map(int,input().split())
arr=input().strip()
l=0
count0=0
count1=0
total=0
for r in range(n):
    # 向右扩展
    if arr[r]=="0":
        count0+=1
    else:
        count1+=1
        #     产生01
        total+=count0
    while l<r and total>k:
        if arr[l]=="0":
            count0-=1
            total-=count1
        else:
            count1-=1
        l+=1
    if total==k:
        print(l+1,r+1)
        exit()
print(-1)