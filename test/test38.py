# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param x int整型
# @return ListNode类
#
# 这道题是分区（Partition）问题，用的是双链表拼接。
#
# 思路
#
# 原链表: 1 → 4 → 3 → 2 → 5 → 2, x = 3
#
# 创建两个虚拟头节点：
# - small: 存放 < x
# 的节点
# - large: 存放 >= x
# 的节点
#
# 遍历原链表：
# 1 < 3  → small: 1
# 4 >= 3 → large: 4
# 3 >= 3 → large: 4 → 3
# 2 < 3  → small: 1 → 2
# 5 >= 3 → large: 4 → 3 → 5
# 2 < 3  → small: 1 → 2 → 2
#
# 最后拼接：small → large
# 结果：1 → 2 → 2 → 4 → 3 → 5
class ListNode:
    pass


class Solution:
    def partition(self , head: ListNode, x: int) -> ListNode:
        # write code here
        small=ListNode(0)
        large=ListNode(0)
        s,l=small,large
        while head:
            if head.val<x:
                s.next=head
                s=s.next
            else:
                l.next=head
                l=l.next
            head=head.next
        #     拼接
        l.next=None
        s.next=large.next
        return small.next