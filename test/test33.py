from collections import deque
from idlelib.tree import TreeNode
from typing import List


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return int整型二维数组
#
class Solution:
    def Print(self , pRoot: TreeNode) -> List[List[int]]:
        # write code here
        if not pRoot:
            return []
        result=[]
        queue=deque([pRoot]) #BFS队列
        level=0 #标记每一层
        while queue:
            level_size=len(queue)#当前层的节点数
            level_val=[]
            # 遍历当前层所有节点的值
            for _ in range(level_size):
                # 从队头取出一个节点
                node=queue.popleft()
                level_val.append(node.val)
                #  把下一层的子节点加入队尾
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
             #奇数层（1, 3, 5...）反转
            if level%2==1:
                level_val.reverse()
            result.append(level_val)
            level+=1
        return result
