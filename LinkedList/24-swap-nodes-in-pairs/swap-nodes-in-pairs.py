# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            left = prev.next
            right = left.next

            left.next = right.next # (3: out)
            right.next = left # (2: middle)
            prev.next = right # (1: in)

            prev = left

        return dummy.next