from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 给定一个
        # m
        # x
        # n
        # 的矩阵，如果一个元素为
        # 0 ，则将其所在行和列的所有元素都设为
        # 0 。请使用
        # 原地
        # 算法。
        #
        m=len(matrix)
        n=len(matrix[0])
        row=n*[False]
        cow=m*[False]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row=True
                    cow=True
        for i in range(m):
            for j in range(n):
                if row or cow:
                    matrix[i][j]=0
