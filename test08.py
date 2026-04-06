# 统计字符串前缀和
def countPrefixes(words:list,s:str):
    count=0
    for word in words:
        # s 是以 word开头
        if s.startswith(word):
            count+=1
    return count