# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # before left 
        for _ in range(left - 1):
            prev = prev.next
        
        start = prev.next
        end = start
        # between
        for _ in range(right - left):
            end = end.next
        
        # after
        after = end.next
        end.next = None
        newHead = self.reverse(start, end)
        prev.next = newHead
        start.next = after

        return dummy.next

    def reverse(self, start: ListNode, end: ListNode):
        prev = None
        curr = start
        while prev != end:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev