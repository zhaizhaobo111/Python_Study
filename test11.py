# 操作excel
import xlrd
# 先打开xlsx文件
xlsx=xlrd.open_workbook('D:\代码\性能测试\论坛系统.csv')
# 获取到指定标签页
table=xlsx.sheet_by_index(0)
# 获取到表格多少行
row=table.nrows
# 进行循环统计
for i in range(1,row):
    print(table.cell_value(i, 0))