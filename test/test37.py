#字符串排序算法二：【字符串排序】https://www.nowcoder.com/practice/9ad2f07d6eb74a6e935e54279b29910d?tpId=182&diffculty=0&judgeStatus=&difficulty=&tags=&title=&sourceUrl=&gioEnter=menu
import functools
# ┌───────┬──────────────────────────────────────┐
# │ 规则  │                 说明                 │
# ├───────┼──────────────────────────────────────┤
# │ 规则1 │ 一个字符串是另一个的前缀，短的排前面 │
# ├───────┼──────────────────────────────────────┤
# │ 规则2 │ 逐字符比较，第一个不同的字符决定大小 │
# └───────┴──────────────────────────────────────┘
# 1. 读入自定义字母顺序
order=input()
# enumerate 表示 索引 字符
# 2. 构建映射: 字母 -> 排名(越小越大)
rank={c:i for i,c in enumerate(order)}
# 3. 读入字符串
n=int(input())
strings=[input() for _ in range(n)]
# 4. 自定义比较函数
def compare(s,r):
    min_len=min(len(s),len(r))
    for i in range(min_len):
        if rank[s[i]]<rank[r[i]]:
            return -1
        elif rank[s[i]]<rank[r[i]]:
            return -1
    return len(s)-len(r)
# 5. 排序
# functools.cmp_to_key 是一个转换器，把你写的比较函数变成 sort 能用的 key 函数
strings.sort(key=functools.cmp_to_key(compare()))
for i in strings:
    print(i)