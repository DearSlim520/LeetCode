# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        remainer = 0
        dummy = ListNode(0)
        res = dummy
        
        while p1 or p2:
            curVal = remainer
            if p1:
                curVal += p1.val
                p1 = p1.next
            if p2:
                curVal += p2.val
                p2 = p2.next
            remainer = 1 if curVal > 9 else 0
            res.next = ListNode(curVal % 10)
            res = res.next

        if remainer:
            res.next = ListNode(remainer)
            
        return dummy.next