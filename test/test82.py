# 给你单链表的头节点
# head ，请你反转链表，并返回反转后的链表。
#
# 示例
# 1：
#
# 输入：head = [1, 2, 3, 4, 5]
# 输出：[5, 4, 3, 2, 1]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional




class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        pre=None
        cur=head
        while cur:
            cur_temp=cur.next
            cur.next=pre
            pre=cur
            cur=cur_temp
        return pre