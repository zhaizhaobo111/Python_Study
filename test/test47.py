# 给定一个链表，删除链表的倒数第 n 个节点并返回链表的头指针
# 例如，
# 给出的链表为:
# 1
# →
# 2
# →
# 3
# →
# 4
# →
# 5
# 1→2→3→4→5,
# n
# =
# 2
# n=2.
# 删除了链表的倒数第
# n
# n 个节点之后,链表变为
# 1
# →
# 2
# →
# 3
# →
# 5
# 1→2→3→5.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可


# @param head ListNode类
# @param n int整型
# @return ListNode类

from test.test38 import ListNode


class Solution:
    def removeNthFromEnd(self , head: ListNode, n: int) -> ListNode:
        # write code here
        # 快慢指针
        res=ListNode(-1)
        res.next=head
        pre=head
        fast=head
        slow=head
        while n:
            fast=fast.next
            n=n-1
        while fast:
            fast=fast.next
            slow=slow.next
            pre=slow
        pre.next=slow.next
        return res.next