# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(-101)
        dummy.next = head
        prev = dummy

        while prev.next:
            cur = prev.next
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            # reverse
            if prev.next != cur:
                prev.next = cur.next
            else:
                prev = prev.next

        return dummy.next

