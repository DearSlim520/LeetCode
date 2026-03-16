# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(-101)
        dummy.next = head
        left = dummy

        # find the spot to insert
        while left.next and left.next.val < x:
            left = left.next
        right = left.next
        if not right:
            return head

        # find targets
        prev = right
        while prev and prev.next:
            if prev.next.val < x:
                prev, left = self.switch(prev, left, right)
            else:
                prev = prev.next

        return dummy.next
        

    def switch(self, prev: ListNode, left: ListNode, right: ListNode) -> ListNode:
        target = prev.next
        prev.next = prev.next.next
        left.next = target
        target.next = right

        return prev, left.next