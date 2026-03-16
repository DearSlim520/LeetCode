# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        lessDummy, moreDummy = ListNode(0), ListNode(0)
        less, more = lessDummy, moreDummy

        p = head
        while p:
            if p.val < x:
                less.next = p
                less = less.next
            else:
                more.next = p
                more = more.next
            p = p.next

        more.next = None
        less.next = moreDummy.next
        
        return lessDummy.next