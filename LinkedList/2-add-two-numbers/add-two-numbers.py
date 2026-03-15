# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        
        while l1 or l2 or carry:
            curVal = carry
            if l1:
                curVal += l1.val
                l1 = l1.next
            if l2:
                curVal += l2.val
                l2 = l2.next
            carry = 1 if curVal > 9 else 0
            cur.next = ListNode(curVal % 10)
            cur = cur.next
            
        return dummy.next