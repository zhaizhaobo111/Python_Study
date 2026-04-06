# 反转字符
def reverseword(s :str):
    # split分隔符，将字符串分割成字符
    alist=s.split()
    alist.reverse()
    # join方法通过空格拼接字符
    return ' '.join(alist)
print(reverseword("Hello word love you"))