# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        nxt = dummy
        total = 0

        while nxt.next:
            nxt = nxt.next
            total += 1

        pre = dummy
        for _ in range(total - n):
            pre = pre.next
        
        # remove
        target = pre.next
        after = target.next if target.next else None
        target.next = None
        pre.next = after

        return dummy.next