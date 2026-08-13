# 给你一个单链表的头节点
# head ，请你判断该链表是否为回文链表。如果是，返回
# true ；否则，返回 false 。
#
# 示例
# 1：
# 输入：head = [1, 2, 2, 1]
# 输出：true
# 示例
# 2：
# 输入：head = [1, 2]
# 输出：false
# Definition for singly-linked list.
from typing import Optional



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 判断是否非空
        if not head or not head.next:
            return True
        # 找中点（快慢指针）
        fast=None
        slow=None
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        # 反转后半段
        pre=None
        cur=slow
        while cur:
            cur_temp=cur.next
            cur.next=pre
            pre=cur
            cur=cur_temp
        # 判断左右是否相等
        left=head
        right=cur
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True