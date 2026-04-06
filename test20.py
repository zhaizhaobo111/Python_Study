# f=open('D:/record/文本文档.txt','w')
# f.write("怎么先炽热的却先变冷了"
#         "慢热的却停不了还在沸腾着"
#         "看时光任性快跑随意就转折"
#         "慢冷的人啊会自我折磨")
# f.close()


# # f.close()
# f=open('D:/record/文本文档.txt','r', encoding='utf-8')
# result=f.readlines()
# print(result)
# f.close()
with open('D:/record/文本文档.txt','r',encoding="utf-8")as f:
    result = f.readlines()
    print(result)