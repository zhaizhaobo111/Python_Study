# open打开一个文件
# f=open('d:/Download/文本文档.txt','r')
# print(f)
# print(type(f))
# \会被当作转义字符，要在前加入r
# f=open(r'd:\Download\文本文档.txt','r')
# print(f)
# print(type(f))
# f.close()

# f=open(r'd:\Download\文本文档.txt','w')
# f.write("helloword")
# f.close()


f=open(r'd:\Download\文本文档.txt','r',encoding='utf8')
# 指定读几个字符
# f.read(2)
# print(f)
lines=f.readlines()
print(lines)
f.close()
