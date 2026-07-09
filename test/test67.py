# 规定一种对于复合词的简写方式为只保留每个组成单词的首字母，并将首字母大写后再连接在一起
# 比如 “College English Test” 可以简写成 “CET”，“Computer Science” 可以简写为 “CS”，“I am Bob” 简写为 “IAB”
# # 输入一个长复合词（组成单词数 sum，sum ≥ 1 且 sum ≤ 100，每个单词长度 len，len ≥ 1 且 len ≤ 50），请你输出它的简写
# line=input()
# words=line.split()
# print(words)
# res=''
# for word in words:
#     # 字符串.upper()
#     # 会把字符串里所有小写英文字母全部转换成大写，数字、符号、大写字母不会发生变化。
#     res+=word[0].upper()
# print(res)

# 规定一种对于复合词的简写方式为只保留每个组成单词的首字母，并将首字母大写后再连接在一起
# 比如 “College English Test” 可以简写成 “CET”，“Computer Science” 可以简写为 “CS”，“I am Bob” 简写为 “IAB”

line=input()
words=line.split()
res=""
for word in words:
    res=word[0].upper()
print(res)