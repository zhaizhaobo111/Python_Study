
# 给定一个整数数组，需要将数组分割成若干段连续子数组，满足每一段内部至少存在两个相同的数字。
# 要求输出：
# 第一行输出分段的总数量；
# 接下来每行输出一段的起始下标、结束下标，下标从 1 开始计数。
# 输入描述
# 输入一行整数，代表数组元素。
import sys
# 输出描述
# 第一行一个整数，表示分段总数；
# 之后每行两个整数，分别代表一段的起始、结束下标（下标从 1 开始）。
# 样例输入
# 1 2 1 3 3
# 样例输出
# plaintext
# 2
# 1 3
# 4 5
#
# 样例解释
# 第一段区间 [1,3]，对应元素 [1,2,1]，存在两个数字 1，满足条件；
# 第二段区间 [4,5]，对应元素 [3,3]，存在两个数字 3，满足条件；
# 总共分割为 2 段。
arr=list(map(int,sys.stdin.readline().split()))
res=[]
start=0
res_left=0
res_right=0
n=len(arr)
# 遍历所有分段
while start <n:
    end=start
    # 字典计算重复次数
    num_count ={}
    # 寻找重复的数
    find_num=False
    # 享有扩展,寻找第一个重复数
    while end<n:
        current_num=arr[end]
        # 如果当前数字已经在字典中，说明区间出现重复
        if current_num in num_count :
            find_num=True
        # 更新该数字的出现次数
        num_count[current_num]=num_count.get(current_num,0)+1
        if find_num:
            break
        end+=1
    res_left = start+1
    res_right = end+1
    # 将当前分段存入结果列表
    res.append([res_left,res_right])
    # 更新下一段的起点：当前段终点的下一个位置
    start = end + 1
print(len(res))
for i,j in res:
    print(i,j)