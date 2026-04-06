# 旋转字符串 最左边放到最右边
def roataeString(s,goal):
    if len(s)!=len(goal):
        return False
    return  goal in (s+s)
print(roataeString("abcde","bcdea"))