#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param mat int整型二维数组
# @param n int整型
# @return int整型二维数组
#
from typing import List

# 先交换上三角，在交换下三角，最后翻转
class Solution:
    def rotateMatrix(self , mat: List[List[int]], n: int) -> List[List[int]]:
        # write code here
        # 遍历矩阵的下三角矩阵，将其与上三角矩阵对应的位置互换
        # 其实就是数组下标交换后的互换
        for i in range(n):
            for j in range(i):
                temp=mat[i][j]
                mat[i][j]=mat[j][i]
                mat[j][i]=temp
        # 遍历矩阵每一行，将每一行看成一个数组使用reverse函数翻转
        for i in range(n):
            mat[i].reverse()
        return mat