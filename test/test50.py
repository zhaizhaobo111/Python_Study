# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1=[]
        stack2=[]
        while l1:
            stack1.append(l1.val)
            l1=l1.next
        while l2:
            stack2.append(l2.val)
            l2=l2.next
        # 进位
        carry=0
        res=None
        while stack1 or stack2 or carry:
            val1=stack1.pop() if stack1 else 0
            val2=stack2.pop() if stack2 else 0
            tatl=val1+val2+carry
            carry=tatl//10
            cur=tatl%10

            new_node=ListNode(cur)
            new_node.next=res
            res=new_node
        return res
