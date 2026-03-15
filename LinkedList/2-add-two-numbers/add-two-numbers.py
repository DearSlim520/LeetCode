# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        
        while p1 or p2 or carry:
            curVal = carry
            if p1:
                curVal += p1.val
                p1 = p1.next
            if p2:
                curVal += p2.val
                p2 = p2.next
            carry = 1 if curVal > 9 else 0
            cur.next = ListNode(curVal % 10)
            cur = cur.next
            
        return dummy.next