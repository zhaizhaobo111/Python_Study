# 题目一：【合并k个已排序的链表】https://www.nowcoder.com/practice/65cfde9e5b9b4cf2b6bafa5f3ef33fa6?tpId=196&tqId=37081&rp=1&sourceUrl=%2Fexam%2Foj%3FquestionJobId%3D10%26subTabName%3Donline_coding_page&difficulty=undefined&judgeStatus=undefined&tags=&title=
# class ListNode:
#     def __init__(self, x):
#         self.x = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param lists ListNode类一维数组
# @return ListNode类
#
from typing import List


class Solution:
    def mergeKLists(self , lists: List[ListNode]) -> ListNode:
        # write code here
        if not lists:
            return None
        while len(lists)>1:
            merged=[]
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(self.mergeTwoLists(l1, l2))
            lists=merged
        return lists[0]
    def mergeTwoLists(self,l1,l2):
        dummy=ListNode(0)
        cur=dummy
        while l1 and l2:
            if l1.val<l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        cur.next=l1 or l2
        return dummy.next