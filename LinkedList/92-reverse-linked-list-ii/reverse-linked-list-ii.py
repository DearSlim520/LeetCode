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
        
        newTail = prev.next
        end = newTail
        # between
        for _ in range(right - left):
            end = end.next
        
        # after
        after = end.next
        end.next = None
        prev.next = None
        self.reverse(newTail, end)
        prev.next = end
        newTail.next = after

        return dummy.next

    def reverse(self, newTail: ListNode, end: ListNode):
        prev = None
        curr = newTail
        while prev != end:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp